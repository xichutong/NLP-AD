#从筛序句子中获取药物与基因的信息
from re import*
import spacy

file1='D:/NPL/shai2.txt'
file2='D:/NPL/chemical.txt'
file3='D:/NPL/gene.txt'
file4='D:/NPL/cellline.txt'
#file5='D:/NPL/disease.txt'
file6='D:/NPL/mutation.txt'
file7='D:/NPL/mark.txt'
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
nlp = spacy.load("en_core_web_sm")
file2_object.close()
file3_object.close()
file4_object.close()
file6_object.close()
i=1
for line in file1_object:
    relation=''
    key={}
    n=0
    doc=nlp(line)
    for taken in doc:
        if taken.dep_ in bio:
            if taken.text in chemical:
                if taken.text in key:
                    pass
                else:
                    key[taken.text]=1
                    relation=relation+'-'+'chemical'
            if taken.text in gene:
                if taken.text in key:
                    pass
                else:
                    key[taken.text]=1
                    relation=relation+'-'+'gene'
            if taken.text in cellline:
                if taken.text in key:
                    pass
                else:
                    key[taken.text]=1
                    relation=relation+'-'+'cellline'
            if taken.text in mutation:
                if taken.text in key:
                    pass
                else:
                    key[taken.text]=1
                    relation=relation+'-'+'mutation'
    if len(key)>1:
       key_list=':'.join(key.keys())
       result=str(i)+'\t'+str(len(key))+'\t'+relation+'\t'+str(key_list)+'\n'
       file7_object.write(result)
    i=i+1
file1_object.close()
file7_object.close()
            