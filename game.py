import random
from functools import lru_cache

def generate_grid(n, obstacle_prob=0.4):
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i, j) in [(0,0), (n-1,n-1)]:
                row.append(0)
            elif random.random() < obstacle_prob:
                row.append(-1)  # obstacle
            else:
                row.append(random.randint(1, 9))
        grid.append(row)
    return grid

def shortest_path_sum(grid1, grid2):
    n = len(grid1)
    @lru_cache(None)
    def dp(x1,y1,x2,y2):
        if not (0<=x1<n and 0<=y1<n and 0<=x2<n and 0<=y2<n):
            return float('inf')
        if grid1[x1][y1]==-1 or grid2[x2][y2]==-1:
            return float('inf')
        if x1==n-1 and y1==n-1 and x2==0 and y2==0:
            return grid1[x1][y1]+grid2[x2][y2]
        cost = grid1[x1][y1]+grid2[x2][y2]
        return cost + min(
            dp(x1+1,y1,x2-1,y2),   # down/up
            dp(x1,y1+1,x2,y2-1)    # right/left
        )
    return dp(0,0,n-1,n-1)

def print_grid(grid, pos, title):
    print(title)
    n = len(grid)
    for i in range(n):
        row = []
        for j in range(n):
            if (i,j)==pos:
                row.append("X")
            elif grid[i][j]==-1:
                row.append("#")
            else:
                row.append(str(grid[i][j]))
        print(" ".join(row))
    print()

def generate_solvable_grids(n, obstacle_prob=0.4):
    attempts = 0
    while True:
        attempts += 1
        g1 = generate_grid(n, obstacle_prob)
        g2 = generate_grid(n, obstacle_prob)
        opt = shortest_path_sum(g1, g2)
        if opt != float('inf'):
            print(f"Found solvable grids after {attempts} attempts")
            return g1, g2, opt

def game(n=5, obstacle_prob=0.5):
    grid1, grid2, optimal = generate_solvable_grids(n, obstacle_prob)

    pos1=(0,0)
    pos2=(n-1,n-1)
    total=0
    moves=[]

    print("Grid1 initial:")
    for r in grid1: print(r)
    print("\nGrid2 initial:")
    for r in grid2: print(r)
    print("\nOptimal path sum:", optimal)

    while True:
        print("\nCurrent sum:", total)
        print_grid(grid1,pos1,"Grid1")
        print_grid(grid2,pos2,"Grid2")
        move=input("Enter move (up/down/left/right/quit): ").strip().lower()
        if move=="quit":
            print("Game ended.")
            break

        # calculate new positions
        if move=="down":
            new1=(pos1[0]+1,pos1[1]); new2=(pos2[0]-1,pos2[1])
        elif move=="up":
            new1=(pos1[0]-1,pos1[1]); new2=(pos2[0]+1,pos2[1])
        elif move=="right":
            new1=(pos1[0],pos1[1]+1); new2=(pos2[0],pos2[1]-1)
        elif move=="left":
            new1=(pos1[0],pos1[1]-1); new2=(pos2[0],pos2[1]+1)
        else:
            print("Invalid move!")
            continue

        # bounds check
        if not (0<=new1[0]<n and 0<=new1[1]<n and 0<=new2[0]<n and 0<=new2[1]<n):
            print("Invalid move (out of bounds)!")
            continue
        # obstacle check
        if grid1[new1[0]][new1[1]]==-1 or grid2[new2[0]][new2[1]]==-1:
            print("Obstacle there! You cannot move.")
            continue

        # update positions
        pos1, pos2=new1,new2
        total+=grid1[pos1[0]][pos1[1]]+grid2[pos2[0]][pos2[1]]
        moves.append(move)

        if total>optimal:
            print("LOSE (exceeded optimal)")
            print("Your moves:", " -> ".join(moves))
            break
        if pos1==(n-1,n-1) and pos2==(0,0):
            if total==optimal:
                print("WIN (optimal path)")
            else:
                print("LOSE (suboptimal path)")
            print("Your moves:", " -> ".join(moves))
            break

if __name__=="__main__":
    # You can change n and obstacle_prob here
    game(n=5, obstacle_prob=0.5)
