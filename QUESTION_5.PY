grid = [
  ['1', '1', '0', '0'],
  ['0', '1', '0', '0'],
  ['0', '0', '1', '1'],
  ['0', '0', '0', '1']
]

dirs = [
  (-1, 0), (1, 0), (0, -1), (0, 1),  # up, down, left, right
]
visited = set()
saved_islands = []

def count_islands(i,j,visited,group):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return False
    else: 
        if grid[i][j] == '0' or (i,j) in visited :
            return 
        visited.add((i,j))
        group.append((i,j))
        for dx ,dy in dirs:
            count_islands(i+dx,i+dy,visited,group)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        
        if grid[i][j] == '1' and (i, j) not in visited:
            group = []
            count_islands(i, j,visited,group)
            
            saved_islands.append(group)    

for loop in saved_islands:
    print(f"{loop},")




