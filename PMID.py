#读取pmid
from re import*
file1='D:/NPL/Pm.txt'
file2='D:/NPL/pmid.txt'
pat=compile('PMID-')
pat1=compile('\d+')
file1_object=open(file1,'r')
file2_object=open(file2,'w')
for eachline in file1_object:
    k=search(pat,eachline)
    if k != None:
        result=search(pat1,eachline)
        n=result.group()
        file2_object.write(n+'\n')
file1_object.close()
file2_object.close()
        
 
