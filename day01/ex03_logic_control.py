# 분기문
age = int(input('나이는?'))
if age <19:
    print("go home")
elif age >30 and age <60:
    print("not to go home")

else:
    print("not go home")    


# 반복문
num = int(input('반복횟수 >'))
for i in range(num): # 4를 입력 하면 0~3
    print(i)

for i in range(1,num + 1):
    print(i)


for j in range(2,11,2): 
    print(j)

