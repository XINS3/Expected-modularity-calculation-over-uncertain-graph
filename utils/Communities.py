#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Random_Community(N,node):
    import random
    '''
    Generate randomly communities
    
    input:
    N: #clusters
    node: #nodes
    
    output: 
    c: communities e.g., c=[0,0,0,1,1,2,2,1]
    '''
    
    # initialization
    
    c1=[]
    c2=[]
    c=[]
    
    c1=random.sample(range(1,N+1),N)
    c=c1+c2
    
    while(len(c)<node):
        c.append(random.randint(1,N))
    
    return c


# In[3]:


def SizeVariance_Commuinity(N_c, N_node ,N_clustering):
    import numpy as np
    import itertools
    '''
    we want to show the performance of APWP with the same number of communities but different community 
    size distributions. 
    
    input:
    N_c: #communities
    N_clustering: #sets of communities
    N_node: #nodes in probabilistic graph G
    
    output:
    c: communities e.g., c=[2,2,1,1,2,3,2,3,3]
    '''
    #initialization
    
   
    size=int(N_node/N_c)
    
    
    node=list(range(N_node))
    #check N_c reasonable
    if size-(N_clustering -1 )<2:
        print('input (N_c) is unavailble, try to input a smaller N_c.')
        return
    #create empty list
    c=[]
    ave_s=size
    #create average size clustering
    
    while(N_clustering):
        
        c1=[node[x:x+size] for x in np.arange(0, len(node[:(N_c-1)*size]), size)]
        
        c2=list(set(node)-set(node[:(N_c-1)*size]))
        
        c1.append(c2)
        
        c.append(c1)
        size-=1
        N_clustering-=1
        
    return c
            
        


        

