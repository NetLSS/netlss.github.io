n = int(input())

arr = []
for i in range(n):
    tup = input().split()
    arr.append((tup[0], int(tup[1])))

arr.sort(key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')