if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    for i in range(len(arr)//2):
        arr[i][1] = "-"
    for i in range(len(arr)):
        arr[i][0] = int(arr[i][0])

    countEl = [] * 100
    for _ in range(100):
        countEl.append([])


    for j in range(len(arr)):
        countEl[arr[j][0]].append(arr[j][1])

    print(arr)
    print(countEl)

    for i in range(len(countEl)):
        for j in range(len(countEl[i])):
            print(countEl[i][j], end = " ")

#input:
'''
20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the
'''