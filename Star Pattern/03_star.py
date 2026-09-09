# we have to print the number in given pattern
# 1
# 12
# 123
# 1234

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print("\n")

pattern(5)
