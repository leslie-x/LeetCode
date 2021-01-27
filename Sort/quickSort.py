#project name: quick sort
#function: make list nums arrange from min to max
#info:

from randomList import randomList
import timeit

iList = randomList(20)

def quickSort(iList):
    
    if len(iList) <= 1:
        #check if list has one num
        return iList
    
    left = []
    right = []
    for i in iList[1:]:
        if i <= iList[0]:
            left.append(i)
        else:
            right.append(i)
    
    return quickSort(left) + [iList[0]] +quickSort(right) #[ls[0]] make value a list element 
    
    
if __name__ ==  '__main__':
    print(iList)
    print(quickSort(iList))
    print(timeit.timeit("quickSort(iList)","from __main__ import quickSort,iList",number=100))
