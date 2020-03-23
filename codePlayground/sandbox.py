def NWD(a,b):
    while b > 0:
        c = a % b
        a = b
        b = c
    print(a)

arr = [0] * 10
print(arr)