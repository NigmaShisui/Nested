def left():
    user = int(input("Range: "))
    for i in range(user):
        for j in range(i + 1):
            print("*", end="")
        print()

def upTri():
    user = int(input("Range: "))
    for i in range(user, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

def triLeft():
    user = int(input("Range: "))
    for i in range(user):
        for j in range(i + 1):
            print("*", end="")
        print()

    for i in range(user, 0, -1):
        for j in range(i):
            print("*", end="")
        print()

def square():
    user = int(input("Range: "))
    for i in range(user):
        for j in range(user):
            if i == 0 or i == user - 1 or j == 0 or j == user - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def cenTri():
    user = int(input("Range: "))
    for i in range(1, user + 1):
        for j in range(user - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()

def downCenTri():
    user = int(input("Range: "))
    for i in range(user, 0, -1):
        for j in range(user - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()

def dia():
    user = int(input("Range: "))
    for i in range(1, user + 1):
        for j in range(user - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()
    
    for i in range(user - 1, 0, -1):
        for j in range(user - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print()

def heart():
    user = int(input("Range: "))
    for i in range(user // 2, user + 1, 2):
        for j in range(1, user - i // 2 + 1):
            print(" ", end="")
        
        for j in range(1, i + 1):
            print("*", end="")
        
        for j in range(1, user - i // 2 + 1):
            print(" ", end="")
        
        for j in range(1, i + 1):
            print("*", end="")
        
        print()

    for i in range(user, 0, -1):
        for j in range(user - i + 1):
            print(" ", end="")
        
        for j in range(1, (i * 2) + 1):
            print("*", end="")
        
        print()

def main():
    while True:
        print("Welcome to Nested For Loop")
        print("Try the Other Patterns for this Loop")
        print("1. Left Angled Triangle")
        print("2. Upside-Left Angled Triangle")
        print("3. Completed Left Angled Triangle")
        print("4. Hollow Square")
        print("5. Center Triangle")
        print("6. Upside Center Triangle")
        print("7. Diamond")
        print("8. Heart")
        print("9. Exit")

        choice = input("Choose option (1, 2, 3, 4, 5, 6, 7, 8, 9): ")

        if choice == '1':
            left()
        elif choice == '2':
            upTri()
        elif choice == '3':
            triLeft()
        elif choice == '4':
            square()
        elif choice == '5':
            cenTri()
        elif choice == '6':
            downCenTri()
        elif choice == '7':
            dia()
        elif choice == '8':
            heart()
        elif choice == '9':
            break
        else:
            print("Invalid input.")

main()
