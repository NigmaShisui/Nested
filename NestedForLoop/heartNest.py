n = 6

for i in range(n // 2, n + 1, 2):
    for j in range(1, n - i, 2):
        print(" ", end="")
    
    for j in range(1, i + 1):
        print("*", end="")
    
    for j in range(1, n - i + 1):
        print(" ", end="")
    
    for j in range(1, i + 1):
        print("*", end="")
    
    print()

for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end="")
    
    for j in range(1, (i * 2) + 1):
        print("*", end="")
    
    print()

