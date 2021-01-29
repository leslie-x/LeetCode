#CreatRandomList

import random

def randomList(n):
    """creat an n length list, range 0,1000"""
    
    iList = []  #make an empty list
    
    for i in range(n):
        #once loop add a num in ilist, loop n times
        iList.append(random.randrange(1000))
        
    return iList

if __name__ == "__main__":
    iList = randomList(10)
    print(iList)