import numpy as np
from random import randint
import networkx as nx
import matplotlib.pyplot as plt

    
def draw_graph(relation,color): #to visualize the graph
    G=nx.Graph()
    G.add_edges_from(relation)
    co = [color[i] for i in G.nodes()]
    nx.draw(G, node_size=1000/(len(relation)/10),node_color=co,
            with_labels=True,font_color='white')
    plt.show()

def generateRandomGraph(nodes,a,b): #to generate random graph
    L = np.zeros((node,node),dtype=int)
    for i in range(nodes):
        for j in range(nodes):
            if i != j and L[i][j] == 0:
                v = int(np.random.choice(2, 1,p=[a,b]))
                if v == 1 :
                    L[i][j] = v
                    L[j][i] = v
    return L
#-------------------------- main program begin -------------------------    
def isSafe(co,list_color,n):
    for i in range(node-1):
        if adj_mtx[n][i] == 1 and list_color[i] == co:
            return False
    return True

def findSolution(list_color,n):
    if(n == node):
        return True
    for co in range(1,mc+1):
        if(isSafe(co,list_color,n)): 
            list_color[n] = co 
            if findSolution(list_color,n+1): 
                return True
            list_color[n] = 0 
    return False

def graphColoring(mtx,mc):
    list_color = np.zeros(node,dtype=int)
    print('>> Maximum color :', mc)
    if not(findSolution(list_color,0)):
        print('>> Solution not found')
        return False
    print('>> Solution Found :',list_color)
    print('>> Minimum color needed :', max(list_color))
    draw_graph(relation,list_color)
    
#-------------------------- inti program ends ------------------------------
    
node = int(input("Generate Random Graph, numebr of nodes : "))
#the greater the probability, the more edges
p = float(input("probabilitas terbentuk koneksi (0.1 - 0.9): "))  #auto matically generates an edges with probabilities
adj_mtx = generateRandomGraph(node,1-p,p)
print(adj_mtx)
#find relation
relation = []
for i in range(len(adj_mtx)):
    for j in range(len(adj_mtx[i])):
        if adj_mtx[i][j] == 1 and (i,j) not in relation and (j,i) not in relation:
            relation.append((i,j))
            
mc = node #max color 
graphColoring(adj_mtx,mc)
