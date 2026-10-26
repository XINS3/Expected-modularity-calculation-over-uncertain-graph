#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import time

# ------------------------------------
from Classic_Sampling import classic_sampling
from Brute_Force import brute_force
from Algorithms import APWP,PWP, Trans_C1,Trans_C2
from Probabilities import PB,DFT
from Network_Generator import rand_graph, rand_graph_com,entropy_
from Communities import Random_Community,SizeVariance_Commuinity
from Threshold import threshold
from Save_Load import save_graph,load_graph,save_com,load_com


# In[14]:


n=100
N_c=5

com = Random_Community(N_c,n)
com=Trans_C1(com)
t=[]
for i in np.arange(200,1100,100):
    #construct network
    
    m=i
    edge_position,edge_possibility,node,nocom=rand_graph(n,m)
    entropy=0.4*m
    edge_possibility=entropy_(entropy,len(edge_possibility))
    edge_possibility=edge_possibility[0]
    random.shuffle(edge_possibility)
    
    #
    T=[]
    for ti in range(3):
        start1=time.time()
        s1=APWP(edge_position,edge_possibility,com)
        end1=time.time()
    T.append(end1-start1)
    
    #
    t.append(np.mean(T))
    print(s1)
    





# In[18]:


for i in np.arange(1100,2600,500):
    #construct network
    
    m=i
    edge_position,edge_possibility,node,nocom=rand_graph(n,m)
    entropy=0.4*m
    edge_possibility=entropy_(entropy,len(edge_possibility))
    edge_possibility=edge_possibility[0]
    random.shuffle(edge_possibility)
    
    #
    T=[]
    for ti in range(3):
        start1=time.time()
        s1=APWP(edge_position,edge_possibility,com)
        end1=time.time()
    T.append(end1-start1)
    
    #
    t.append(np.mean(T))
    print(s1)


# In[19]:


print(t)


# # Comparison

# In[21]:


n=10
N_c=5
t_our=[]
t_brute=[]
t_no_app=[]
com=Random_Community(N_c,n)

for i in np.arange(10,25,5):
    #construct network
    
    m=i
    edge_position,edge_possibility,node,nocom=rand_graph(n,m)
    entropy=0.4*m
    edge_possibility=entropy_(entropy,len(edge_possibility))
    edge_possibility=edge_possibility[0]
    random.shuffle(edge_possibility)
    
    #
    Tapwp=[]
    Tpwp=[]
    Tbrute=[]
    for ti in range(3):
        start1=time.time()
        s1=APWP(edge_position,edge_possibility,Trans_C1(com))
        end1=time.time()
        
        #
        Tapwp.append(end1-start1)
        
        
        
        #
        
        start2=time.time()
        s2=brute_force(edge_possibility,com,n,edge_position)
        end2=time.time()
        
        Tbrute.append(end2-start2)
        
        
        #
        start3=time.time()
        s3=PWP(edge_position,edge_possibility,Trans_C1(com))
        end3=time.time()

        Tpwp.append(end3-start3)
        
        t_no_app.append(end3-start3)
    t_our.append(np.mean(Tapwp)  )
    t_brute.append(np.mean(Tbrute))
    t_no_app.append(np.mean(Tpwp))
    
print('T our',t_our, 'T_brute',t_brute,'T_noAppr',t_no_app)




for i in np.arange(21,24,1):
    #construct network
    
    m=i
    edge_position,edge_possibility,node,nocom=rand_graph(n,m)
    entropy=0.4*m
    edge_possibility=entropy_(entropy,len(edge_possibility))
    edge_possibility=edge_possibility[0]
    random.shuffle(edge_possibility)
    
    
    Tapwp=[]
    Tpwp=[]
    Tbrute=[]
    for ti in range(3):
    
    #
    
        start2=time.time()
        s2=brute_force(edge_possibility,com,n,edge_position)
        end2=time.time()
        
        Tbrute.append(end2-start2)
        
        
        #
        
        start1=time.time()
        s1=APWP(edge_position,edge_possibility,Trans_C1(com))
        end1=time.time()
        
        #
        Tapwp.append(end1-start1)
        
        #
        
        start3=time.time()
        s3=PWP(edge_position,edge_possibility,Trans_C1(com))
        end3=time.time()
        
        Tpwp.append(end3-start3)
    
    t_our.append(np.mean(Tapwp)  )
    t_brute.append(np.mean(Tbrute))
    t_no_app.append(np.mean(Tpwp))
    
print('T our',t_our, 'T_brute',t_brute,'T_noAppr',t_no_app)


import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

#data store

x=[10,15,20,23]+list(np.arange(200,1100,100))+list(np.arange(1100,2700,500))
print(x)
t=[0.000538,0.0012652,0.002458,0.0034940,2.777,9.779,24.265,47.686,83.091,155.835,233.461,288.008,443.471,534.077,1787.5306,3972.3575, 7553.0115]
plt.plot(x,t,'go--',color='r',linewidth=2,markersize=10,mfc='none',label=r'$APWP^{EMOD}$')
t2=[0.3813,14.759,560.034,5125.3251]
x2=[10,15,20,23]

# In[41]:


import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

#data store

x=[10,15,20,23]+list(np.arange(200,1100,100))+list(np.arange(1100,2600,500))
print(x)
t=[0.00014551480611165365,0.0003361701965332031,0.0005671977996826172,0.000774383544921875,0.28861451148986816,0.9623647530873617,2.3003076712290444,4.575117746988933,8.229190587997437,13.323678175608316,19.699, 27.987346569697063, 38.75501505533854, 51.85535987218221, 166.17688488960266, 389.678373336792]
plt.plot(x,t,'go--',color='r',linewidth=2,markersize=10,mfc='none',label=r'$APWP^{EMOD}$')
t2=[0.3813,14.759,560.034,5125.3251]
x2=[10,15,20,23]

x3=[10,15,20,25]
t3=[0.0054061,0.050260305,0.4887776374816,9.117868105570475]

plt.plot(x3,t3,ls='--',marker='v',color='black',linewidth=2,markersize=10,mfc='none',label=r'$PWP^{EMOD}$')
plt.plot(x2,t2,ls='--',marker='d',color='b',linewidth=2,markersize=10,mfc='none',label='BF')
plt.ylabel('Time [s]')
plt.xlabel('Networks size [edges]')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(xmin=0)
plt.legend()
plt.title('Time comparison according to different sizes of networks')
plt.savefig('size_Net_v2.pdf')
plt.show()


# In[ ]:





plt.plot(x3,t3,ls='--',marker='v',color='black',linewidth=2,markersize=10,mfc='none',label=r'$PWP^{EMOD}$')
plt.plot(x2,t2,ls='--',marker='d',color='b',linewidth=2,markersize=10,mfc='none',label='BF')
plt.ylabel('Time [s]')
plt.xlabel('Networks size [edges]')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(xmin=0)
plt.legend()
plt.title('Time comparison according to different sizes of networks')
plt.savefig('size_Net_v2.pdf')
plt.show()


# In[ ]:









