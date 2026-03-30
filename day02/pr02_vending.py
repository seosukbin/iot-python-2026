## PR01_vending.py 자판기 프로그램

menu = ['펩시','칠성 사이다','코카콜라','제로 콜라','웰치스','백산수']
price = [1900,2100,2000,2300,1000,1500]
money = 0
sel = 0
num = 5000
def printmenu():
    print('[자판기 메뉴]')
    for i in range(0,len(menu)):
        print(f'{i+1}.{menu[i]}\t가격 : {price[i]}')
    print()

def getproduct(menu):
    if money < price[num]:
        print(f'잔액 부족, 잔액: {price[i]}원')
    else:
        print(f'{menu[num]} 구입 완료')
        balance = money  - price[num]
        print(f'잔액: {balance}원')
        return balance
    
while(True):
    printmenu()
    sel = int(input('메뉴 번호 선택(종료: 0): '))
    if sel == 0:
        break
    elif(sel >=1 and sel<= len(menu)) :
        print(f'{menu[sel - 1]}선택!')
        money = getproduct(sel - 1)

    else:
        print('메뉴 선택 다시 해요')


print('자판기 사용 끝')