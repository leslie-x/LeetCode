#project name: Insert sort
#function: make list nums arrange from min to max
#info:divide list to left&right,then right insert to left by arrange

from randomList import randomList
import timeit

iList = randomList(20)

def insertionSort(iList):
    
    if len(iList) <= 1:
        #check if list has one num
        return iList
        
    for right in range(1,len(iList)):
        #right start with ls[1],target is num which ready to insert 
        target = iList[right]
        for left in range(0,right):           #left is ls[0,right]
            if target <= iList[left]:         #if left >= right ,then exchange
                iList[left+1:right+1] = iList[left:right]   #move left to right by 1 step
                iList[left] = target
                break                          #once insert then break to next right
        #print(f"the {right} turn resolt {iList}")
        
    return iList

if __name__ ==  '__main__':
    print(iList)
    print(insertionSort(iList))
    print(timeit.timeit("insertionSort(iList)","from __main__ import insertionSort,iList",number=100))
     