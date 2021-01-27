#project name: merge sort
#function: make list nums arrange from min to max
#info:divide list to left&right,then right,left insert to middle by arrange

from randomList import randomList
import timeit

iList = randomList(20)

def mergeSort(iList):
    
    if len(iList) <= 1:
        #check if list has one num
        return iList
    
    middle = len(iList) // 2
    left,right = iList[0:middle],iList[middle:]
    return mergeList(mergeSort(left),mergeSort(right))
    
    
def mergeList(left,right):
    
    mlist = [] #middle list restore combine(left,right)
    
    while left and right:
        if left[0] >= right[0]:
            mlist.append(right.pop(0))
        else:
            mlist.append(left.pop(0))
            
    while left:
        mlist.append(left.pop(0))
        
    while right:
        mlist.append(right.pop(0))
        
    return mlist
    
    
if __name__ ==  '__main__':
    print(iList)
    print(mergeSort(iList))
    print(timeit.timeit("mergeSort(iList)","from __main__ import mergeSort,iList",number=100))