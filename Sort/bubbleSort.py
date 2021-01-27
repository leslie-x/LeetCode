#project name: Bubble sort
#function: make list nums arrange from min to max

from randomList import randomList
import timeit

iList = randomList(20)

def bubbleSort(iList):
    """bubbleSort"""
    
    if len(iList) <= 1:
        #check if list is blank or one element
        return iList
    
    for i in range(1,len(iList)):           #sort i times
        for j in range(0,len(iList)-i):     #everytime compare ls[j]&ls[j+1],and ignore nums which been sorted
            #if left >= right then exchange them
            if iList[j] >= iList[j+1]:
                iList[j],iList[j+1] = iList[j+1],iList[j]
        #print(f"the {i} turn resolt {iList}")
        
    return iList


if __name__ == "__main__":
    print(iList)
    print(bubbleSort(iList))
    print(timeit.timeit("bubbleSort(iList)","from __main__ import bubbleSort,iList",number=100))
