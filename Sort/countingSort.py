#project name: counting sort
#function: make list nums arrange from min to max
#info:choose one base in ilist and find num of which smaller than base,then put base in a new list where index=num

from randomList import randomList
import timeit

iList = randomList(20)

def countingSort(iList):
    
    if len(iList) <= 1:
        #check if list has one num
        return iList
    
    iLen = len(iList)   #make a new list, len=ilist
    rList = [None]*iLen
    
    for i in range(iLen):
        small = 0      
        same = 0      #if same?
        
        for j in range(iLen):            #count the num of smallers
            if iList[j] < iList[i]:
                small += 1
            elif iList[j] == iList[i]:
                same += 1
                
        for k in range(small,small+same):
            rList[k] = iList[i]
                
        #print (rList) 
        
    return rList

if __name__ ==  '__main__':
    print(iList)
    print(countingSort(iList))
    print(timeit.timeit("countingSort(iList)","from __main__ import countingSort,iList",number=100))
                