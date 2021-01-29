#project name: binary search
#function: find if in the list
#info:use binary search,

from randomList import randomList
from quickSort import quickSort

iList = quickSort(randomList(20))

def binarySearch(iList,key):     #return index
    
    left = 0
    right = len(iList)-1
    
    while right-left > 1:
        mid = (left+right) // 2
        
        if key < iList[mid]:
            right = mid
        elif key > iList[mid]:
            left = mid
        else:
            return mid
    
    if key == iList[left]:
        return left
    elif key == iList[right]:
        return right
    else:
        return -1
        

if __name__ ==  '__main__':
    print(f"iList = {iList}")
    key = int(input("Find the number:"))
    index = binarySearch(iList,key)
    if index>=0:
        print(f"iList = {iList}")
        print(f"Yes,find '{key}' in List! index is {index}")
    else:
        print(f"iList = {iList}")
        print(f"No,find no '{key}' in List!")