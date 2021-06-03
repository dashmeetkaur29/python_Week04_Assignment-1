# Implementation was learnt from Breadth First Search (BFS) algorithm.
# Implemented with dictionaries
edges = {
    'A':[['B',5],['D',5],['E',7]],
    'B':[['C',4]],
    'C':[['D',8],['E',2]],
    'D':[['C',8],['E',6]],
    'E':[['B',3]]
}


# Function takes source and destination node as arguments
def findPath(src,dst):
    dist = 0
    allPaths=[]
    q=[]
    q.append( (src,[src],dist) )
    visited = []

    while len(q)!=0:
        cur = q.pop(0)
        curnode=cur[0]
        curpath=cur[1]
        curDist = cur[2]
        visited.append(curnode)

        if(curnode==dst):
            allPaths.append((curpath.copy(),curDist))

        else:
            for nei,neiDist in edges[curnode]:
                if(nei not in visited):
                    newCopy=curpath.copy()
                    newCopy.append(nei)
                    q.append( (nei,newCopy,curDist+neiDist) )

    print(f'All paths starting from {src} and ending with {dst} are :\n{allPaths}')

    minimum = allPaths[0][1]
    for min in allPaths:
        if min[1] < minimum:
            minimum = min[1]
    print(f'The shortest path is : {minimum}')


src='A'
dst='D'
findPath(src,dst)  #Calling function to Calculate the distance of the route A-D

print("-----------------------------------------------------------------------------------------")

src='A'
dst='C'
findPath(src,dst)  #Calling function to Calculate the length of the shortest route (in terms of distance to travel) from A to C.

