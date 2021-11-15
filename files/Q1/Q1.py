import sys
import os

debug = False

# convert the line into float points x and y
def point_read(point):
    pt = point.strip().split(" ")
    
    for i in range(len(pt)):
        pt[i] = float (pt[i])
    
    return pt


def find_single_link_distance(cluster1,cluster2):
    
    dis = -1
    
    if(debug):
        print(cluster1,cluster2,end=" ")
    
    for i in cluster1:
        for j in cluster2:
            dis_tmp = ((i[0]-j[0])**2 + (i[1]-j[1])**2)**(.5)
            
            if(dis==-1 or dis>dis_tmp):
                dis = dis_tmp
    
    if(debug):
        print(dis)   
    
    return dis

# open the file
read_f = open(sys.argv[1],'r')

# read the line from the file
read_l = read_f.readline()

points = []

while(read_l):
    points.append([point_read(read_l)])
    read_l = read_f.readline()
    


#   points is a list of list of list
print(points)

# start the algorithm

while(len(points)>1):
    cluster1 = -1
    cluster2 = -1
    distance = -1
    
    for i in range(len(points)-1):
        for j in range(i+1,len(points)):

            dis = find_single_link_distance(points[i],points[j])

            if (distance == -1 or distance>dis):
                distance = dis
                cluster1 = i
                cluster2 = j
                
    print("distance :",distance)
    print("points :")
    print(cluster1,points[cluster1])
    print(cluster2,points[cluster2])
    
    new_cluster = points[cluster1]+points[cluster2]
    print("new cluster :",new_cluster)
    
    
    points_tmp = []
    for ii in range(len(points)):
        if(ii!=cluster1 and ii!=cluster2):
            points_tmp.append(points[ii])
    
    
    if (debug):
        print(points_tmp)
    points_tmp.append(new_cluster)
    
    points = points_tmp
    
    print("----------------------------------")
    print(points)