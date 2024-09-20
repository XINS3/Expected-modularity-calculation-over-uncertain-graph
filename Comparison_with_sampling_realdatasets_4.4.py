import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import time
from Algorithms import APWP,PWP, Trans_C1,Trans_C2
from Save_Load import save_graph,load_graph,save_com,load_com

'''
loading graph and communities.
graph files:
- collaboration_sampling.npy
- facebook2_sampling.npy
- TAP_sampling.npy
- Enron_sampling.npy
- lesmis.gml
cluster file:
- collaboration_sampling_com.txt
- facebook2_sampling_com.txt
- TAP_sampling_com.txt
- Enron_sampling_com.txt
- lesmis_com.txt
'''


node, edge_position, edge_possibility=load_graph('datasets//facebook2_sampling.npy')
cluster=[]
with open("datasets//facebook2_sampling_com.txt", 'r') as file:
    # Read all the lines of the file into a list
    lines = file.readlines()
    for i in lines:
        l=i[1:-2]
        k=l.split(',')
        ll=[]
        for j in k:
            
            ll.append(int(j))
        
        cluster.append(ll)

start1=time.time()
s1=APWP(edge_position,edge_possibility,cluster)#older version com is wrong
end1=time.time()
print('time',end1-start1)
print('facebook2',s1)

from Classic_Sampling import classic_sampling
t=[]
s=[]
for i in np.arange(5000,41000,5000):

    t1=[]
    s1=[]
    for k in range(10):
        
        N_sample=i

        start=time.time()
 
        Q_2=classic_sampling(N_sample,cluster,edge_position,edge_possibility,node)
        
        end=time.time()
        s1.append(Q_2)
        t1.append(end-start)
        
        
    s.append(s1)
    t.append(t1)
    print(s)
    print(t)


for i in np.arange(500,5000,500):

    t1=[]
    s1=[]
    for k in range(10):
        
        N_sample=i

        start=time.time()
 
        Q_2=classic_sampling1(N_sample,cluster,edge_position,edge_possibility,node)
        
        end=time.time()
        s1.append(Q_2)
        t1.append(end-start)
        
        
    s.append(s1)
    t.append(t1)
    print(s)
    print(t)

    fig, ax = plt.subplots()

for i in range(len(s)):
    for j in range(len(s[i])-1):
            
   
        plt.plot(t[i][j],s[i][j],'o',mfc='red',mec='black')
plt.plot(t[i][j],s[i][j],'o',mfc='red',mec='black',label='NMC')

col=['lightcoral','coral','greenyellow','turquoise','cyan','indigo','fuchsia','plum','steelblue','magenta','blueviolet']
ax.axvline(x =end1-start1, color = 'blue',ls=':',linewidth=3)
ax.axhline(y=0.5945533518755468, color='blue',ls=':',linewidth=3)
plt.plot(end1-start1,0.5945533518755468,'o',mfc='blue',
     mec='black',markersize=8,label=r'$APWP^{EMOD}$')
plt.ylabel('Value of expected modularity')
plt.xlabel('Time [s]')

ax.set_xlim(xmin=0)

ax.set_xlim([0.1,250])
ax.set_ylim([0.5930,0.596])
ax.set_xscale('log')

ax.annotate('({}, {})'.format(round(end1-start1,3),round(0.5945533518755468,3) ), xy=(2,1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.legend(loc='upper right', bbox_to_anchor=(1, 0.9),prop={'size': 8})
#plt.title('Entropy ratio=0.48')
#plt.savefig('enron_sampling.pdf')
plt.show()

