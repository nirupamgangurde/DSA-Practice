#Print name n times using recursion 1 to n

name = input("Enter the name : ")
no = int(input("Enter the no: "))
i = 0
def newname():
    global i
    if i==no:
        return
    else:
        print(name)
        i+=1
    newname()
newname()

#Print name n times using recursion n to 1
def fun(num):
    if num==0:
        return
    else:
        print(num)
        fun(num-1)

num = int(input("Enter the num: "))
fun(num)