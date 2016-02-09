import sys
import random
#width of environment
e_w = int(input("Enter a width of the environment"))

#height of environment
e_h = int(input("Enter a height of the environment"))

#3 2-D matrices for environment, heurisitcs and visited
environment = [[0 for i in range(e_w)] for i in range(e_h)]
heuristic = [[0 for i in range(e_w)] for i in range(e_h)]
visited = [[0 for i in range(e_w)] for i in range(e_h)]
search_visited = [[0 for i in range(e_w)] for i in range(e_h)]

#initializing environment boundaries
for i in range(e_w):
    environment[0][i]='0'
    environment[e_h-1][i]='0'

#initialising all nodes visited to false
for i in range(e_h):
    for j in range(e_w):
        visited[i][j]='f'
        search_visited[i][j]='f'


#building random blocks in environment
for i in range(1,e_h-1):
    environment[i][0]='0'
    environment[i][e_w-1]='0'
    for j in range(1,e_w-1):
        k=random.randrange(0,2)
        if k==1:
            environment[i][j]='0'
        else:
            environment[i][j]=' '

#giving highest heurisitc to blocks and boundaries of environment
for i in range(e_h):
    for j in range(e_w):
        if environment[i][j]=='0':
            heuristic[i][j]=sys.maxsize

#intialize random source node
while True:
    sx_position=random.randrange(e_h)
    sy_position=random.randrange(e_w)
    if environment[sx_position][sy_position]==' ':
        environment[sx_position][sy_position]='1'
        break
    
#intialize random destination node            
while True:
    dx_position=random.randrange(e_h)
    dy_position=random.randrange(e_w)
    if environment[dx_position][dy_position]==' ':
        environment[dx_position][dy_position]='9'
        break


def developHeuristic(x,y,h_count):
    if environment[x][y]=='0' or h_count>heuristic[x][y]:
        return;
    else:
        #visited[x][y]='t'
        
        heuristic[x][y]=h_count
        #print("%s x position" % x)
        #print("%s y position" % y)
        #print("%s count_value" % heuristic[x][y])
        developHeuristic(x,y+1,h_count+1)
        developHeuristic(x+1,y,h_count+1)
        developHeuristic(x-1,y,h_count+1)
        developHeuristic(x,y-1,h_count+1)
        return;


developHeuristic(dx_position, dy_position,0)

finalcost=sys.maxsize
cost=sys.maxsize

def getMinimalCost(x,y,path_cost):
    search_visited[x][y]='t'
    if x==dx_position and y==dy_position:
        print('path_cost is')
        print(path_cost)
        return;
    else:
        up=[heuristic[x-1][y],x-1,y]
        upright=[heuristic[x-1][y+1],x-1,y+1]
        right=[heuristic[x][y+1],x,y+1]
        downright=[heuristic[x+1][y+1],x+1,y+1]
        down=[heuristic[x+1][y],x+1,y]
        downleft=[heuristic[x+1][y-1],x+1,y-1]
        left=[heuristic[x][y-1],x,y-1]
        upleft=[heuristic[x-1][y-1],x-1,y-1]

        x_indices=[up[1],upright[1],right[1],downright[1],down[1],downleft[1],left[1],upleft[1]]
        y_indices=[up[2],upright[2],right[2],downright[2],down[2],downleft[2],left[2],upleft[2]]
        myList=[up[0],upright[0],right[0],downright[0],down[0],downleft[0],left[0],upleft[0]]

        while True:
            min_h=min(myList)
            index=myList.index(min_h)
            if search_visited[x_indices[index]][y_indices[index]]=='f':
                break
            myList.remove(myList[index])
            x_indices.remove(x_indices[index])
            y_indices.remove(y_indices[index])
            
        if min_h==sys.maxsize:
            print('There is no path possible');
            return;
        else:
            
            getMinimalCost(x_indices[index],y_indices[index],path_cost+1)     

path_cost=getMinimalCost(sx_position,sy_position,0)

print('environment')
for i in range(e_h):
    print(environment[i][:])
print('heurisitc')
for i in range(e_h):
    print(heuristic[i][:])
print('searchvisited')
for i in range(e_h):
    print(search_visited[i][:])

