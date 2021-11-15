import torch
import torch.nn as nn
import networkx as nx
import numpy as np
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid

dataset = Planetoid("","Cora",num_train_per_class= 150,split= 'random' ,num_test = 1000)

edges = dataset[0].edge_index
vertices = dataset[0].train_mask.shape[0]
edges = edges.T

adjacency = np.zeros((vertices,vertices),dtype=np.float)
for edge in edges:
    adjacency[edge[0]][edge[1]] = 1.00
    adjacency[edge[1]][edge[0]] = 1.00

diag = np.diag(np.sum(adjacency,axis=0))
Transition = np.dot(np.linalg.inv(diag),adjacency)

def matexpo(mat,power):
    result = np.identity(mat.shape[0])
    while (power!=0):
        result = np.dot(result,mat)
        power -= 1
    return result

Transition_fin = matexpo(Transition,0)+ matexpo(Transition,1) + matexpo(Transition,2) + matexpo(Transition,3)+ matexpo(Transition,4)
Transition_fin = Transition_fin / 5.00


#Preparation of test_data
x_test = []
y_test = []
test_vertices = np.where(dataset[0].test_mask==True)
for i in range(0,len(test_vertices[0])):
    remaining = np.delete(test_vertices[0],i)
    store_vec = np.zeros(vertices)
    store_vec[test_vertices[0][i]]=1 
    distances = np.dot(Transition_fin,store_vec).reshape(-1)
    random_sample = np.random.choice(test_vertices[0],10)
#    non_zero_sample = np.where(distances>0)
#    zero_sample =  np.where(distances==0)
#    random_sample = np.concatenate((np.random.choice(non_zero_sample[0],1),np.random.choice(zero_sample[0],9)))
    for j in range(0,10):
        x_test.append([test_vertices[0][i],random_sample[j]])
        y_test.append(distances[random_sample[j]])

x_test = np.array(x_test)
y_test = np.array(y_test)


from torch_geometric.nn import GATConv,GATv2Conv,MemPooling
class GAT(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = GATv2Conv(in_channels= -1, out_channels= 250)
        self.conv2 = GATv2Conv(in_channels= 250, out_channels= 250, concat=False)
        
    def forward(self,data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        return x
   
class combined_model(nn.Module):
    def __init__(self,input_dim,hidden_dim):
        super().__init__()
        self.layer1 = GAT()
        self.mlp1 = nn.Linear(input_dim,hidden_dim)
        self.mlp2 = nn.Linear(hidden_dim,1)

    def forward(self,data,x):
        embeddings = self.layer1(data)
        x1 = torch.index_select(embeddings,0,x.T[0].flatten())
        y1 = torch.index_select(embeddings,0,x.T[1].flatten())
        store = torch.cat((x1,y1),dim=1)
        store = self.mlp1(store)
        store = F.relu(store)
        store = self.mlp2(store)
        store = F.relu(store)
        return store

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
data1 = dataset[0].to(device)
best_model = torch.load("model")
loss_func = nn.MSELoss()

x_test_fin = torch.from_numpy(x_test)
x_test_fin = x_test_fin.to(device)
y_test_fin = torch.from_numpy(y_test)
y_test_fin = y_test_fin.to(device)


pred_test = best_model(data1,x_test_fin).flatten()
y_test_fin = y_test_fin.float()
loss1 = loss_func(pred_test,y_test_fin)
test_loss = loss1.item()
print("Loss on test data is: ",loss1.item())
