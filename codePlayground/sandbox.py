def NWD(a,b):
    while b > 0:
        c = a % b
        a = b
        b = c
    print(a)

