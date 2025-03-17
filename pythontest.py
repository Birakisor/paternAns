num = int(input("Enter a number in beetWeen 1 to 5: "))
alpha = "ABCDE"

for i in range(num):
    for j in range(num-i):
        print(" ", end="")
    for k in range(i+1):
        print(f"{alpha[k]}",end=" ")
    for j in range(num+i):
        print(" ", end="")
    print()
for i in range(num):
    for k in range(i+2):
        print(" ", end="")
    for j in range((num-1)-i):
        print(f"{alpha[j]}",end=" ")
    for k in range(i-1):
        print("", end="")
    print()