#project name: Selection sort
#function: make list nums arrange from min to max
#info:select one num,compare it with others and choose the min or max,exchange index

from randomList import randomList
import timeit

iList =  randomList(20)

def selectionSort(iList):
    
    if len(iList) <= 1:
        return iList
    
    for i in range(0,len(iList)-1):
        #if ls[i] == min(right),then not move,if not then exchange index,use minIndex to store min(right) index
        if iList[i] != min(iList[i:]):
            minIndex = iList.index(min(iList[i:]))
            iList[i],iList[minIndex] = iList[minIndex],iList[i]
        #print(f"the {i} turn resolt {iList}")
    
    return iList

if __name__ == "__main__":
    print(iList)
    print(selectionSort(iList))
    print(timeit.timeit("selectionSort(iList)","from __main__ import selectionSort,iList",number=100))
