## pr01_gugudan.py 구구단 프로그램

dan = int(input("출력할 단 입력(2~9사이): "))

for i in range(2,dan+1):
    print(f'{i}단 입력')

    for j in range(1,9+1):
        print(f'{i} x{j} = {i*j}')
