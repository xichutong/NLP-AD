#根据pubtator的数据，抽取相应生物学名词存入文件中
from re import*
        
file1='D:/NPL/result__Pmid.txt'
#file2='D:/NPL/chemical.txt'
#file2='D:/NPL/gene.txt'
#file2='D:/NPL/cellline.txt'
#file2='D:/NPL/disease.txt'
file2='D:/NPL/mutation.txt'

file1_object=open(file1,'r')
file2_object=open(file2,'w')
#pat=compile('Chemical')
#pat=compile('Gene')
#pat=compile('CellLine')
#pat=compile('Disease')
pat=compile('Mutation')
dict={}
for line in file1_object:
       k=search(pat,line)
       if k!= None:
          list=split(compile('\s+'), line)
          name=list[3]
          if dict.get(name,0) ==0:
             dict[name]=1
          else:
             dict[name]+=1

    
for key in dict.keys():
    if dict[key] > 10:
       text=str(key) + '\t' + str(dict[key]) + '\n'
       file2_object.write(text)
file1_object.close()
file2_object.close()

