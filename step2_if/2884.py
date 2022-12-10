H, M = map(int,input().split())
x = (H*60)+M-45
H = (x//60)
M = (x%60)

if H < 0:
    H = H+24
else:
    pass

print(H,M)
