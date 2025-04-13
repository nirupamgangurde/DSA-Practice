# Parameterised Recursion we have used parameters in the function
# def para(i,sum):
#     if i <1:
#         print(sum)
#         return
#     else:
#         para(i-1,sum+i)

# i = int(input("Enter a number: "))
# para(i,0)

# Functional Recursion is a recursion that does not use any parameters in the function
def fun(n):
    if n==0:
        return 0
    else:
        return n+fun(n-1)
    
print(fun(5))