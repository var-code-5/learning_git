
x = 2
y = 3

def square(x):
    return  x **2

def sub(x,y):
    return x-y

print(square(x+sub(square(y),2*x)))