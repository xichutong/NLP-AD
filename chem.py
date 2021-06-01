#检索固定药物的相关信息
from re import*

file1='D:/NPL/mark.txt'
file2='D:/NPL/rode.txt'
file3='D:/NPL/three_chem.txt'

file1_object=open(file1,'r')
file2_object=open(file2,'r')
file3_object=open(file3,'w')
data1=[]
data2=[]
chem=['Donepezil','Rivastigmine','Memantine']
i=0
for line in file2_object:
    lis=split('\t',line)
    data2.append(lis[3].strip())
for line in file1_object:
    lis=split(compile('\t'),line)
    relation=split(':',lis[3],(int(lis[1])-1))
    relation[-1]=relation[-1].strip()
    for word in relation:
        if word.capitalize() in chem:
            lw=str(line.strip())+'\t'+data2[i]+'\n'
            file3_object.write(lw)
    i=i+1
file1_object.close()
file2_object.close()
file3_object.close()


    
    

        

    
    