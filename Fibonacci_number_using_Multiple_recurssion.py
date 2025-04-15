# write a function that give you nth fibonacci number using multiple recursion
def fibo(ip):
    if ip<=1:
        return ip
    last = fibo(ip-1) # this will run first till the end of the recursion
    slast = fibo(ip-2) # After the last recursion is completed, this will run
    return last + slast
ip = int(input("Enter the number of terms: "))
print(fibo(ip))