#project name: sequential search
#function: find if in the list
#info:

from randomList import randomList
from quickSort import quickSort
import timeit

iList = quickSort(randomList(20))

def sequentialSearch(iList,key):
    
    for i in range(len(iList)):
        if iList[i] == key:
            return True   #return True
        
    return False    #if not find, return False


    
if __name__ ==  '__main__':
    
    key = input("Find the number:")
    if sequentialSearch(iList,key):
        print(f"iList = {iList}")
        print(f"Yes,find '{key}' in List!")
    else:
        print(f"iList = {iList}")
        print(f"No,find no '{key}' in List!")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    