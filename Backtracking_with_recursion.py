# 1 to n using backtracking without plus operator
def backtrack(n):
    if n<1:
        return
    else:
        backtrack(n-1)
        print(n)

n = int(input("Enter the value of n: "))
backtrack(n)

# n to 1 using backtracking without minus operator gives reverse order output
def rev(i,n):
    if i>n:
        return
    else:
        rev(i+1,n)
        print(i)

n = int(input("Enter the value of n: "))
rev(1,n)