#筛选含有至少两个实体信息的句子
from re import*
import spacy
#import networkx as nx

nlp = spacy.load("en_core_web_sm")
file1='D:/NPL/result__Pmid.txt'
file2='D:/NPL/chemical.txt'
file3='D:/NPL/gene.txt'
file4='D:/NPL/cellline.txt'
#file5='D:/NPL/disease.txt'
file6='D:/NPL/mutation.txt'
file7='D:/NPL/shai3.txt'
file1_object=open(file1,'r')
file2_object=open(file2,'r')
file3_object=open(file3,'r')
file4_object=open(file4,'r')
#file5_object=open(file5,'r')
file6_object=open(file6,'r')
file7_object=open(file7,'w')

chemical=[]
gene=[]
cellline=[]
mutation=[]
bio=['nsubj','nsubjpass','dobj','pobj']
for line in file2_object:
    list=split(compile('\t'),line)
    chemical.append(list[0])
for line in file3_object:
    list=split(compile('\t'),line)
    gene.append(list[0])
for line in file4_object:
    list=split(compile('\t'),line)
    cellline.append(list[0])
for line in file6_object:
    list=split(compile('\t'),line)
    mutation.append(list[0])
file2_object.close()
file3_object.close()
file4_object.close()
file6_object.close()

for line in file1_object:
    k=search(compile('\|a\|'),line)
    if k!=None:
        list=split(compile('\|a\|'),line)
        list=split(compile('\.\s{1}'),list[1])
        for l in list:
             doc = nlp(l)
             n=0
             m=0
             for taken in doc:
                if taken.dep_ in bio:
                    if taken.text in chemical:
                        m=m+1
                    if taken.text in gene:
                        n=n+1
                    if taken.text in mutation:
                        n=n+1
             if n>0 and m>0 :
                lw=str(l)+'\n'
                file7_object.write(lw)
file1_object.close()
file7_object.close()
            


 
