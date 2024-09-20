#!/usr/bin/env python
# coding: utf-8

# # Forest Fire Network Model

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import time
import csv
from collections import defaultdict


# ------------------------------------
from Classic_Sampling import classic_sampling
from Brute_Force import brute_force
from Algorithms import APWP,PWP, Trans_C1,Trans_C2
from Probabilities import PB,DFT
from Network_Generator import rand_graph, rand_graph_com,entropy_
from Communities import Random_Community,SizeVariance_Commuinity
from Threshold import threshold
from Save_Load import save_graph,load_graph,save_com,load_com

# read edges of FFN 

filename='ffn.csv'
f=open(filename,"r")
lines=f.readlines()
edge_position_ffn=[]

for x in lines:
    node1=int(x.split(' ')[0])
    node2=int(x.split(' ')[1].split('\n')[0])
 
    edge_position_ffn.append((node1,node2))
    
f.close()

#generate edge probabilities

entropy=0.4
edge_possibility_FFN=entropy_(entropy*len(edge_position_ffn),len(edge_position_ffn))
edge_possibility_FFN=edge_possibility_FFN[0]

columns = defaultdict(list) # each value in each column is appended to a list

#open community file to read the number of communities
'''
#c = 4: cluster_ffn_c=4.csv
#c = 5: cluster_ffn_c=5.csv
#c = 6: cluster_ffn_c=6.csv
'''

with open('cluster_ffn_c=6.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

c=[]
for i in range(len(columns['Id'])):
    c.append([int(columns['Id'][i]),int(columns['modularity_class'][i])])
c=sorted(c,key=lambda l:l[1])

com=[]
front_point=0
c1=[]
c1.append(c[0][0])
for i in range(1,len(c)):
    
    later_point=i
    if c[later_point][1]==c[front_point][1]:
        c1.append(c[later_point][0])
        
    else:
        com.append(c1)
        
       
        c1=[]
        c1.append(c[later_point][0])
    
    if later_point==len(c)-1:
        
        com.append(c1)
        
        
    front_point=later_point
    
ss=0
for i in com:
    ss+=len(i)

#shuffle edges

random.shuffle(edge_possibility_FFN)
plt.plot(edge_possibility_FFN)

#Calculate APWP
T_ffn=[]
for ti in range(3):
    start1=time.time()
    s1=APWP(edge_position_ffn,edge_possibility_FFN,com)#older version com is wrong
    end1=time.time()
    
    T_ffn.append(end1-start1)

#  Barabási-Abert

# read edges

filename='ba.csv'
f=open(filename,"r")
lines=f.readlines()
edge_position_BA=[]
for x in lines:
    node1=int(x.split(' ')[0])
    node2=int(x.split(' ')[1].split('\n')[0])
    edge_position_BA.append((node1,node2))
    
f.close()

columns = defaultdict(list) # each value in each column is appended to a list

# open file to read number of communities

'''
#c = 4: cluster_ba_c=4.csv
#c = 5: cluster_ba_c=5.csv
#c = 6: cluster_ba_c=6.csv
'''

with open('cluster_ba_c=6.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

print(len(columns['Id']))
print(columns['modularity_class'])

c=[]
for i in range(len(columns['Id'])):
    c.append([int(columns['Id'][i]),int(columns['modularity_class'][i])])
c=sorted(c,key=lambda l:l[1])

c
com=[]
front_point=0
c1=[]
c1.append(c[0][0])
for i in range(1,len(c)):
    
    later_point=i
    if c[later_point][1]==c[front_point][1]:
        c1.append(c[later_point][0])
        
    else:
        com.append(c1)
        
       
        c1=[]
        c1.append(c[later_point][0])
    
    if later_point==len(c)-1:
        
        com.append(c1)
        
        
    front_point=later_point
    
ss=0
for i in com:
    ss+=len(i)

#To control the edge probabilities in BA is similar in FFN

edge_possibility_BA=[]
for i in range(len(edge_position_BA)):
    edge_possibility_BA.append(edge_possibility_FFN[i])

# calculate APWP
T_ba=[]
for ti in range(3):
    start1=time.time()
    s1=APWP(edge_position_BA,edge_possibility_BA,com)
    end1=time.time()
    T_ba.append(end1-start1)
    

#  ER model

# read edges

filename='er.csv'
f=open(filename,"r")
lines=f.readlines()
edge_position_ER=[]
for x in lines:
    node1=int(x.split(' ')[0])
    node2=int(x.split(' ')[1].split('\n')[0])
    edge_position_ER.append((node1,node2))
    
f.close()

columns = defaultdict(list) # each value in each column is appended to a list

# open file to read communities
'''
#c = 4: cluster_er_c=4.csv
#c = 5: cluster_er_c=5.csv
#c = 6: cluster_er_c=6.csv
'''

with open('cluster_er_c=6.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k


c=[]
for i in range(len(columns['Id'])):
    c.append([int(columns['Id'][i]),int(columns['modularity_class'][i])])
c=sorted(c,key=lambda l:l[1])

com=[]
front_point=0
c1=[]
c1.append(c[0][0])
for i in range(1,len(c)):
    
    later_point=i
    if c[later_point][1]==c[front_point][1]:
        c1.append(c[later_point][0])
        
    else:
        com.append(c1)
        
       
        c1=[]
        c1.append(c[later_point][0])
    
    if later_point==len(c)-1:
        
        com.append(c1)
        
        
    front_point=later_point
    
ss=0
for i in com:
    ss+=len(i)

#To control edge probabilities in ER is similar in FFN and BA

edge_possibility_ER=[]
for i in range(len(edge_possibility_FFN)):
    edge_possibility_ER.append(edge_possibility_FFN[i])
while(len(edge_possibility_ER)<len(edge_position_ER)):
    edge_possibility_ER.append(random.random())
    
# calculate APWP
T_er=[]
for ti in range(3):
    start1=time.time()
    s1=APWP(edge_position_ER,edge_possibility_ER,com)
    end1=time.time()
    T_er.append(end1-start1)

# Small world

# read edges

filename='sw.csv'
f=open(filename,"r")
lines=f.readlines()
edge_position_SW=[]
for x in lines:
    node1=int(x.split(' ')[0])
    node2=int(x.split(' ')[1].split('\n')[0])
    edge_position_SW.append((node1,node2))
    
f.close()

# To control edge probabilities in SW is similar in ER, FFN, and BA

edge_possibility_SW=[]
for i in edge_possibility_ER:
    edge_possibility_SW.append(i)
while(len(edge_possibility_SW)<len(edge_position_SW)):
    edge_possibility_SW.append(random.random())

columns = defaultdict(list) # each value in each column is appended to a list

# open file to read communities
'''
#c = 4: cluster_sw_c=4.csv
#c = 5: cluster_sw_c=5.csv
#c = 6: cluster_sw_c=6.csv
'''
with open('cluster_sw_c=6.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

c=[]
for i in range(len(columns['Id'])):
    c.append([int(columns['Id'][i]),int(columns['modularity_class'][i])])
c=sorted(c,key=lambda l:l[1])

com=[]
front_point=0
c1=[]
c1.append(c[0][0])
for i in range(1,len(c)):
    
    later_point=i
    if c[later_point][1]==c[front_point][1]:
        c1.append(c[later_point][0])
        
    else:
        com.append(c1)
        
       
        c1=[]
        c1.append(c[later_point][0])
    
    if later_point==len(c)-1:
        
        com.append(c1)
        
        
    front_point=later_point
    
ss=0
for i in com:
    ss+=len(i)

# calcualte APWP
T_sw=[]
for ti in range(3):
    start1=time.time()
    s1=APWP(edge_position_SW,edge_possibility_SW,com)
    end1=time.time()
    T_sw.append(end1-start1)

# ____________________________
# CCS graph
'''
edge=593, node=200
#cluster=6  'com_ccs_593_c=6.npy' && 'graph_ccs_593_c=6.npy'
#cluster=5  'com_ccs_593_c=5.npy' && 'graph_ccs_593_c=5.npy'
#cluster=4  'com_ccs_593_c=4.npy' && 'graph_ccs_593_c=4.npy'
'''
com_5=np.load('com_ccs_593_c=5.npy',allow_pickle=True)

node_ccs5, edge_position_ccs5, edge_possibility_ccs5=load_graph('graph_ccs_593_c=5.npy')
# calcualte APWP
T_c4=[]
for ti in range(3):
    start1=time.time()
    s1=APWP(edge_position_ccs5, edge_possibility_ccs5,com_5)
    end1=time.time()
    T_c4.append(end1-start1)
np.mean(T_c4)




# save data and draw

from matplotlib.patches import Rectangle
species = ("C=4", "C=5", "C=6")

width=0.25
patterns = [ "/" , "\\" , "|" , "-" , "+" , "x", "o", "O", ".", "*" ]
fig, ax = plt.subplots()
x = np.arange(len(species)) 



re1=ax.bar(x+0.1,[11.027,13.869,15.738],width=0.12,label='FFN',hatch='///',color='white',edgecolor='black')
ax.bar_label(re1,size=8)
re2=ax.bar(x+0.25,[9.474,11.943,13.614],width=0.12,label='BA',hatch='|||',color='white',edgecolor='black')
ax.bar_label(re2,size=8)
re3=ax.bar(x+0.4,[9.950,11.713,13.255],width=0.12,label='ER',hatch='--',color='white',edgecolor='black')
ax.bar_label(re3,size=8)
re4=ax.bar(x+0.55,[7.374,9.858,12.143],width=0.12,label='SW',hatch='xx',color='white',edgecolor='black')
ax.bar_label(re4,size=8)
re5=ax.bar(x+0.7,[9.863,11.126,11.974],width=0.12,label='CCS graph',hatch='..',color='white',edgecolor='black')
ax.bar_label(re5,size=8)


ax.set_xticks(x + width, species,size=15)
plt.yticks(fontsize=15)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5,frameon=False,fontsize=15)
ax.set_ylabel('Time (s)',fontsize=15)
ax.set_title('Computation time in different networks',fontsize=15)
fig.set_figheight(6)
fig.set_figwidth(10)
plt.savefig('partition_time.pdf')

