#!/usr/bin/env python
# coding: utf-8

# In[65]:


def classic_sampling(N_sample,c,edge,p,node):
    import Modularity
    import importlib
    importlib.reload(Modularity)
    from Modularity import modularity_deter
    import networkx as nx
    import random
    '''
    we first generate N_sample samples from the probability distribution over the possible worlds, then calculate
    modularity for each sample graph and compute the average modularity
    
    input: 
    N_sample: the number of samples
    c: communities e.g., c=[0,1,1,0,2]
    edge: e.g., edge=[(0,1),(2,3),(0,4)]
    p: edge probabilities e.g., p=[0.2,0.4,0.4]
    node: #nodes in a probabilistic graph
    
    
    output:
    Q: average modularity by sampling method
    '''
    
    
    
    edge_n=len(edge)
   
    #initialize 
    
    Samp=[]
    
    # choose samples from all possible worlds
       
    while (len(Samp)<N_sample):
        pw_lst=[]

        for j in range(edge_n):
            p_r=random.random()
            if p_r<=p[j]:
                pw_lst.append(edge[j])
            #else:
                #pw_lst.append()
        #print(pw_lst)
        Samp.append(pw_lst)

    # calculate modularity 
    
    Q=0
    
    for samp in Samp:
        g=nx.Graph()
        g.add_nodes_from(list(range(node)))
        g.add_edges_from(samp)
        #Q+=modularity_deter(c,node,samp,edge)
        Q+=nx.community.modularity(g,c)
    # average modularity
    
    Q/=len(Samp)
        
    
    return Q