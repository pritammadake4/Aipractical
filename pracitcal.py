N=8
b=[[0]*N for _ in range(N)]

def safe(r,c):
    for i in range(c):
        if b[r][i] or (r-i)==abs(c-i): return 0
    return 1

def solve(c):
    if c==N:return 1
    for r in range(N):
        if safe(r,c):
            b[r][c]=1
            if solve(c+1):return 1
            b[r][c]=0
    return 0

solve(0)
for x in b:print(x)