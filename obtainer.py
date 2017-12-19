from random import randint
from numpy import array

#  array(map(int,obtainer.getData()))

def getData():
    arr = []
    
    dataFile = open('data.txt','r').readlines()
    
    for line in dataFile:    
        tmpArr = []
        line = line.replace('\n','')
        
        for i in line:        
            tmpArr.append(int(i))
            
        arr.append(tmpArr)
        
    #  print(arr)
    return arr
    
    
def getAns():
    arr = []
    ansFile = open('ans.txt','r').readlines()
    
    for line in ansFile:
        arr.append(int(str(line).replace('\n','')))
        
    #  print(arr)
    return arr
    
    
def maker(dataNum):
    dataFile = open('data.txt','w')
    ansFile = open('ans.txt','w')
    
    for i in range(0,dataNum):
        num1,num2,num3 = randint(0,1),randint(0,1),randint(0,1)
        dataFile.write(str(num1)+str(num2)+str(num3)+'\n')
        
        if (num1 ^ num2) == 0:
            ansFile.write('0\n')
            
        else:
            ansFile.write('1\n')
            
    dataFile.close()
    ansFile.close()
