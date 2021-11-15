# import the modules

import torch
import torch.nn as nn
# import networkx as nx
import numpy as np
import torch.nn.functional as F
from torch_geometric.datasets import Planetoid
import os
import sys


###
#  python3 Q2.py <number of epochs> <learning rate> <num_train_per_class> <model name>
###

debug = True

# Loading the dataset
#dataset = Planetoid("","Cora",num_train_per_class= 150,split= 'random' ,num_test = 1000)
dataset = Planetoid("","Cora",num_train_per_class= int(sys.argv[3]),split= 'random' ,num_test = 1000)

# Selecting the edges and vertices
edges = dataset[0].edge_index
vertices = dataset[0].train_mask.shape[0]
edges = edges.T

# Making the adjacency matrix
adjacency = np.zeros((vertices,vertices),dtype=np.float)
for edge in edges:
    adjacency[edge[0]][edge[1]] = 1.00
    adjacency[edge[1]][edge[0]] = 1.00
    
# Normalization of the data
diag = np.diag(np.sum(adjacency,axis=0))
Transition = np.dot(np.linalg.inv(diag),adjacency)

def matexpo(mat,power):
    result = np.identity(mat.shape[0])
    while (power!=0):
        result = np.dot(result,mat)
        power -= 1
    return result

# RWR
Transition_fin = matexpo(Transition,0)+ matexpo(Transition,1) + matexpo(Transition,2) + matexpo(Transition,3)+ matexpo(Transition,4)
Transition_fin = Transition_fin / 5.00



#Preparation of train_data
x_train = []
y_train = []
train_vertices = np.where(dataset[0].train_mask==True)
for i in range(0,len(train_vertices[0])):
    # remaining= np.delete(train_vertices[0],i)
    store_vec = np.zeros(vertices)
    store_vec[train_vertices[0][i]]=1 
    distances = np.dot(Transition_fin,store_vec).reshape(-1)
    non_zero_sample = np.where(distances>0)
    zero_sample =  np.where(distances==0)
    random_sample = np.concatenate((np.random.choice(non_zero_sample[0],15),np.random.choice(zero_sample[0],15)))
    for j in range(0,30):
        x_train.append([train_vertices[0][i],random_sample[j]])
        y_train.append(distances[random_sample[j]])

x_train = np.array(x_train)
y_train = np.array(y_train)

#Preparation of valid_data
x_val = []
y_val = []
val_vertices = np.where(dataset[0].val_mask==True)
for i in range(0,len(val_vertices[0])):
    # remaining= np.delete(val_vertices[0],i)
    store_vec = np.zeros(vertices)
    store_vec[val_vertices[0][i]]=1 
    distances = np.dot(Transition_fin,store_vec).reshape(-1)
    non_zero_sample = np.where(distances>0)
    zero_sample =  np.where(distances==0)
    random_sample = np.concatenate((np.random.choice(non_zero_sample[0],5),np.random.choice(zero_sample[0],5)))
    for j in range(0,10):
        x_val.append([val_vertices[0][i],random_sample[j]])
        y_val.append(distances[random_sample[j]])

x_val = np.array(x_val)
y_val = np.array(y_val)

#Preparation of test_data
x_test = []
y_test = []
test_vertices = np.where(dataset[0].test_mask==True)
for i in range(0,len(test_vertices[0])):
    # remaining= np.delete(test_vertices[0],i)
    store_vec = np.zeros(vertices)
    store_vec[test_vertices[0][i]]=1 
    distances = np.dot(Transition_fin,store_vec).reshape(-1)
    non_zero_sample = np.where(distances>0)
    zero_sample =  np.where(distances==0)
    random_sample = np.concatenate((np.random.choice(non_zero_sample[0],5),np.random.choice(zero_sample[0],5)))
    for j in range(0,10):
        x_test.append([test_vertices[0][i],random_sample[j]])
        y_test.append(distances[random_sample[j]])

x_test = np.array(x_test)
y_test = np.array(y_test)

# creating the model
from torch_geometric.nn import GATConv
from torch.nn.functional import leaky_relu

class GAT(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = GATConv(in_channels= -1, out_channels= 250)
        self.conv2 = GATConv(in_channels= (250,250), out_channels= 250, concat=False)
        
    def forward(self,data):
        x, edge_index = data.x, data.edge_index
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        # x = F.log_softmax(x,dim=1)
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

model_fin = combined_model(500,400)
model_fin = model_fin.to(device)

#Training and testing
data1 = dataset[0].to(device)
loss_func = nn.MSELoss()
#optimizer = torch.optim.Adam(model_fin.parameters(), lr=0.0001,weight_decay=1e-5)
optimizer = torch.optim.Adam(model_fin.parameters(), lr=float(sys.argv[2]),weight_decay=1e-5)
scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.5, verbose=True)

#epoch = 100
epoch = int(sys.argv[1])

x_train_fin = torch.from_numpy(x_train)
x_train_fin = x_train_fin.to(device)
y_train_fin = torch.from_numpy(y_train)
y_train_fin = y_train_fin.to(device)

x_val_fin = torch.from_numpy(x_val)
x_val_fin = x_val_fin.to(device)
y_val_fin = torch.from_numpy(y_val)
y_val_fin = y_val_fin.to(device)

x_test_fin = torch.from_numpy(x_test)
x_test_fin = x_test_fin.to(device)
y_test_fin = torch.from_numpy(y_test)
y_test_fin = y_test_fin.to(device)

val_loss = None
val_acc = []
best_model = None
patience_count= 0

for i in range(0,epoch):
    pred_val = model_fin(data1,x_train_fin).flatten()
    y_train_fin= y_train_fin.float()
    loss1 = loss_func(pred_val,y_train_fin)
    if (debug):
        print(f"Value of training loss for epoch {i} is: ",loss1.item())
    optimizer.zero_grad()  
    loss1.backward()
    optimizer.step()

    pred_val = model_fin(data1,x_val_fin).flatten()
    y_val_fin = y_val_fin.float()
    loss1 = loss_func(pred_val,y_val_fin)
    val_acc.append(loss1.item())
    
    if(debug):
        print(f"Value of validation loss for epoch {i} is: ",loss1.item())    
    if best_model is None:
        best_model = model_fin
        val_loss = loss1.item()
        patience_count = 0

    elif loss1.item() < val_loss:
        best_model = model_fin
        val_loss = loss1.item()
        patience_count = 0
    
    else:
        patience_count += 1

    if(patience_count == 10):
        patience_count = 0
        scheduler.step()

torch.save(best_model,sys.argv[4]+"_model_class_"+sys.argv[3]+"_lt_"+sys.argv[2]+"_epoch_"+sys.argv[1])

if(debug):
    print("Training Done.")

# plot of the validation accuracy
import matplotlib.pyplot as plt

val_acc = np.array(val_acc)
x_axis = [i for i in range(0,100)]
plt.plot(x_axis,val_acc)
plt.savefig("plots/plt_gatconv_class_"+sys.argv[3]+"_lt_"+sys.argv[2]+"_epoch_"+sys.argv[1]+".png")
plt.show()


# loss value
pred_test = best_model(data1,x_test_fin).flatten()
y_test_fin = y_test_fin.float()
loss1 = loss_func(pred_test,y_test_fin)
test_loss = loss1.item()

print("Loss on test data is: ",loss1.item())
