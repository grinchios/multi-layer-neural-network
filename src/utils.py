from random import randint
import sys

#  return data from file
def getData():
    arr = []
    
    dataFile = open('database/data.txt','r').readlines()
    
    for line in dataFile:    
        tmpArr = []
        line = line.replace('\n','')
        
        for i in line:        
            tmpArr.append(int(i))
            
        arr.append(tmpArr)
        
    #  print(arr)
    return arr
    
   
#  return answer file 
def getAns():
    arr = []
    ansFile = open('database/ans.txt', 'r').readlines()
    
    for line in ansFile:
        arr.append(int(str(line).replace('\n','')))
        
    #  print(arr)
    return arr
    
    
# create answer and data files
def maker(dataNum):
    dataFile = open('database/data.txt','w')
    ansFile = open('database/ans.txt','w')
    
    for i in range(0,dataNum):
        num1,num2 = randint(0,1),randint(0,1)
        num3,num4 = randint(0,1),randint(0,1)
        dataFile.write(str(num1)+str(num2)+str(num3)+str(num4)+'\n')
        
        if (num1 ^ num2) == 0:
            ansFile.write('0\n')
            
        else:
            ansFile.write('1\n')
            
    dataFile.close()
    ansFile.close()

    
#  return a progress bar
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 5)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s]%s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()
