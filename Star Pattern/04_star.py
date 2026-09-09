# we have to print the pattern like given below
#    *
#   **
#  ***

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i+j)<=n:
                print(" ",end="")
            else:
                print("*",end="")
        print()

pattern(5)