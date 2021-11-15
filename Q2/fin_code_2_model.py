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

x_train = []
y_train = []
train_vertices = np.where(dataset[0].train_mask==True)
for i in range(0,len(train_vertices[0])):
    remaining= np.delete(train_vertices[0],i)
    store_vec = np.zeros(vertices)
    store_vec[train_vertices[0][i]]=1 
    distances = np.dot(Transition_fin,store_vec).reshape(-1)
  #  non_zero_sample = np.where(distances>0)
  #  zero_sample =  np.where(distances==0)
  #  random_sample = np.concatenate((np.random.choice(non_zero_sample[0],10),np.random.choice(zero_sample[0],20)))
    for j in range(0,len(train_vertices[0])):
        x_train.append([train_vertices[0][i],train_vertices[0][j]])
        y_train.append(distances[train_vertices[0][j]])

x_train = np.array(x_train)
y_train = np.array(y_train)

x_val = []
y_val = []
val_vertices = np.where(dataset[0].val_mask==True)
for i in range(0,len(val_vertices[0])):
    remaining= np.delete(val_vertices[0],i)
    store_vec = np.zeros(vertices)
    store_vec[val_vertices[0][i]]=1 
    distances = np.dot(Transition_fin,store_vec).reshape(-1)
#    non_zero_sample = np.where(distances>0)
#    zero_sample =  np.where(distances==0)
#    random_sample = np.concatenate((np.random.choice(non_zero_sample[0],5),np.random.choice(zero_sample[0],5)))
    for j in range(0,len(val_vertices[0])):
        x_val.append([val_vertices[0][i],val_vertices[0][j]])
        y_val.append(distances[val_vertices[0][j]])

x_val = np.array(x_val)
y_val = np.array(y_val)

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

best_model = torch.load("model")

import matplotlib.pyplot as plt
val_acc = np.array(val_acc)
x_axis = [i for i in range(0,10)]
plt.plot(x_axis,val_acc)
plt.show()

pred_test = best_model(data1,x_test_fin).flatten()
y_test_fin = y_test_fin.float()
loss1 = loss_func(pred_test,y_test_fin)
test_loss = loss1.item()
print("Loss on test data is: ",loss1.item())
