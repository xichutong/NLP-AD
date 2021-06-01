#网络图绘制
from re import*

file1='D:/NPL/mark.txt'
file2='D:/NPL/graph.txt'
file1_object=open(file1,'r')
file2_object=open(file2,'w')

key={}
for line in file1_object:
    lis=split(compile('\t'),line)
    relation=split(':',lis[3],(int(lis[1])-1))
    relation[-1]=relation[-1].strip()
    if relation[0] in key:
       pass
    else:
        key[relation[0]]={}
    for i in range(1,len(relation)):
           if relation[i] in key[relation[0]]:
               key[relation[0]][relation[i]]=key[relation[0]][relation[i]]+1
           else:
               key[relation[0]][relation[i]]=1
node=key.keys()
for node1 in node:
    node2='\t'.join(key[node1].keys())
    lw=str(node1)+'\t'+'relation'+'\t'+str(node2)+'\n'
    file2_object.write(lw)
file1_object.close()
file2_object.close()
    
    

        