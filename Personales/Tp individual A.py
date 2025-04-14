#resolución del problema A de:
#https://codeforces.com/contests/601138
'''
import time
def templadobottomup(matriz):
    m,n = len(matriz), len(matriz[0])
    mem = [[set() for _ in range(n)] for _ in range(m)]
    mem[0][0] = {matriz[0][0]}
    for f in range(0,m):
        for c in range(0,n):
            if c== 0 and f ==0:
                continue
            elif c==0:
                mem[f][0] = set([e + matriz[f][0] for e in mem[f-1][0]])
            elif f == 0:
                mem[0][c] = set([e + matriz[0][c] for e in mem[0][c-1]])
            else:
                mem[f][c] = set([e + matriz[f][c] for e in mem[f][c-1]])|set([e + matriz[f][c] for e in mem[f-1][c]])
    return 0 in mem[m-1][n-1]

def templado(matriz,x,y,t, memoria):
    n,m = len(matriz), len(matriz[0])
    if x>= m or y >= n:
        return False
    t+= matriz[y][x]
    if (x,y,t) in memoria:
        return memoria[(x,y,t)]
    if x == m-1 and y == n-1:
        res = (t == 0)
    else:
        res = templado(matriz,x,y+1, t,memoria) or templado(matriz,x+1,y, t,memoria)
    memoria[(x,y,t)] = res
    return res

def templado2(matriz,x,y,t, memoria):
    n,m = len(matriz), len(matriz[0])
    if x>= m or y >= n:
        return False
    t+= matriz[y][x]
    if memoria[x][y][t] != -1:
        return memoria[x][y][t]
    if x == m-1 and y == n-1:
        res = (t == 0)
    else:
        res = templado2(matriz,x,y+1, t,memoria) or templado2(matriz,x+1,y, t,memoria)
    memoria[x][y][t] = res
    return res
'''
def bottomup(matriz):
    m,n = len(matriz), len(matriz[0])
    
    mem[0][0] = (matriz[0][0],matriz[0][0])
    for f in range(0,m):
        for c in range(0,n):
            if c== 0 and f ==0:
                continue
            elif c==0:
                mem[f][0] = (matriz[f][0] + mem[f-1][0][0],mem[f-1][0][1] + matriz[f][0])
            elif f == 0:
                mem[0][c] = (mem[0][c-1][0] +  matriz[f][c],mem[f][c-1][1] + matriz[f][c])
            else:
                mem[f][c] = (min(mem[f-1][c][0],mem[f][c-1][0])+matriz[f][c],max(mem[f-1][c][1],mem[f][c-1][1])+matriz[f][c])
    return mem[m-1][n-1][0] <= 0 <= mem[m-1][n-1][1]
#esto en realidad medio random porque dicen que la cantidad maxima es 10e6 casos, pero no te dicen la forma de matriz, podria no ser 10e5 x 10. para proximas veces es mas entendible si dicen la forma de la matriz y no la complican
mem = [[(1000000,-1000000) for _ in range(1000)] for _ in range(1000)]
t = int(input())
for _ in range(t):
        n,m = map(int, input().split())
        if (n+m) % 2 == 0:
            print('NO')
            for _ in range(n):
                nothing = input()
        else:
            matriz = []
            #memoria = {}
            #memoria2 = [[[-1 for _ in range(m+n)]for _ in range(n)] for _ in range(m)]
            for i in range(n):
                matriz.append(list(map(int, input().split())))

            #if templado2(matriz,0,0,0,memoria2):
            if bottomup(matriz):
                print('YES')
            else:
                print('NO')
