# How to reverse an array using recursion?
def rev(arr):
    if len(arr)==0:
        return []
    else:
        return [arr[-1]]+rev(arr[:-1])
arr = [1, 2, 3, 4, 5]
rev_arr = rev(arr) 
print(rev_arr)
