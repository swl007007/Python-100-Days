row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for _ in range(i+1):
        print('*',end='')
    print()

for i in range(row):
    for _ in range(row-1-i):
        print(' ',end='')
    for _ in range(2*i+1):
        print('*',end='')
    print()