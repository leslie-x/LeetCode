#project name: block search
#function: find if in the list
#info:use block search, list needn't be sorted,and faster than sequentialsearch

from randomList import randomList

iList = randomList(20)
indexList = [[250,0],[500,0],[750,0],[1000,0]]  #[block, count]


def divideBlock():
    global iList, indexList
    sortList = []
    for key in indexList:
        subList = [i for i in iList if i<key[0]]  #inwhich num <250 or 500 or so on
        key[1] = len(subList)                     #counting
        sortList += subList                       #sortlist stores the linear of blocks
        iList = list(set(iList)-set(subList))     #only set() can plus or minus each other
    iList = sortList                              #make ilist a divided list
    print(f"iList after divide ={iList}")
    return indexList


def blockSearch(iList,key,indexList):     #return index
    
    left = 0
    right = 0
    
    for indexInfo in indexList:
        left += right
        right += indexInfo[1]
        if key < indexInfo[0]:
            break
    for i in range(left,right):
        if key == iList[i]:
            return i
    return -1
        
        

if __name__ ==  '__main__':
    print(f"iList = {iList}")
    divideBlock()
    key = int(input("Find the number:"))
    index = blockSearch(iList,key,indexList)
    if index>=0:
        print(f"iList = {iList}")
        print(f"Yes,find '{key}' in List! index is {index}")
    else:
        print(f"iList = {iList}")
        print(f"No,find no '{key}' in List!")
