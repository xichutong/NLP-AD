#对成对关系进行依存路径分析

import spacy
import networkx as nx
from re import*

file1='D:/NPL/mark.txt'
file2='D:/NPL/shai2.txt'
file3='D:/NPL/rode.txt'
file1_object=open(file1,'r')
file2_object=open(file2,'r')
file3_object=open(file3,'w')
i=[]
n=[]
key=[]
lines=-1
data=[]
for line in file1_object:
    lis=split(compile('\t'),line)
    i.append(lis[0])
    n.append(lis[1])
    key.append(split(':',lis[3],(int(lis[1])-1)))
    lines=lines+1
for line in file2_object:
    data.append(line)
nlp = spacy.load("en_core_web_sm")
for m in range(0,(lines+1)):
    l=data[(int(i[m])-1)]
    doc=nlp(l)
    edges=[]
    for token in doc:
        for child in token.children:
            edges.append(('{0}'.format(token.lower_),'{0}'.format(child.lower_)))
    graph = nx.Graph(edges)
    entity1 = (key[m][0]).lower()
    entity2 = (key[m][-1].strip()).lower()
    #print(nx.shortest_path_length(graph, source=entity1, target=entity2))
    rode=nx.shortest_path(graph, source=entity1, target=entity2)
    lw=str(i[m])+'\t'+str(n[m])+'\t'+str(':'.join(key[m]).strip())+'\t'+str(' '.join(rode))+'\n'
    file3_object.write(lw)
file1_object.close()
file2_object.close()
file3_object.close()
    
    
    
    

    


