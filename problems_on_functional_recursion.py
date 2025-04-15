# How to reverse an array using recursion?
def rev(arr):
    if len(arr)==0:
        return []
    else:
        return [arr[-1]]+rev(arr[:-1])
arr = [1, 2, 3, 4, 5]
rev_arr = rev(arr) 
print(rev_arr)

# check if stirng is palindrome or not using recursion
def pal(s):
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    return pal(s[1:-1])

s = input("Enter a string: ")
print(pal(s))
