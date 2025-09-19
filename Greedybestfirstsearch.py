# Define the grid (4x5 matrix)
# S = Start, G = Goal, X = Blocked cell, . = Free cell
grid = [
 ['S','.','.','.','.'],
 ['.','X','X','.','.'],
 ['.','.','.','X','.'],
 ['.','X','.','.','G']
]

# Start position and Goal position (row, column)
start, goal = (0,0), (3,4)

# Manhattan distance function (heuristic)
def h(a,b): 
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# open_list = nodes to be explored
# path = nodes visited (final path)
open_list, path = [start], []

# Main loop: keep running until open_list is empty
while open_list:
    # Choose the node with the smallest heuristic (closest to goal)
    cur = min(open_list, key=lambda x: h(x,goal))
    
    # Remove it from open_list and add to path
    open_list.remove(cur)  
    path.append(cur)
    
    # Stop if goal is reached
    if cur == goal: 
        break
    
    # Explore 4 possible directions (Right, Down, Left, Up)
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx, ny = cur[0] + dx, cur[1] + dy  # new cell position
        
        # Conditions:
        # 1. Inside grid boundaries
        # 2. Not a blocked cell (X)
        # 3. Not already visited
        if 0<=nx<4 and 0<=ny<5 and grid[nx][ny] != 'X' and (nx,ny) not in path:
            open_list.append((nx,ny))  # Add valid neighbor to open_list

# Print the final path from Start to Goal
print("Path:", path)
