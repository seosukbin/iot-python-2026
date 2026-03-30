## ex13_datastruct.py 리스트외 자료 구조

arr = [1,2,3,4]
arr.append(5)
print(arr)

#Tuple(튜플) - 소괄호

tup = (1,2,3,4)
print(f'튜플값 = {tup}')

# 튜플은 변경이 불가능한 리스트, const형 리스트
# 튜플 -> DB에서 한줄()
# 속도가 빠르고, 데이터를 함부로 못 고치게 고정 역할

## Dictionary - 중괄호
spiderman = {

    'name': '스파이더맨',
    'age' : 21,
    'realname': 'Peter Parker'
}

print(spiderman['realname'])

# 사전형식, 빠른 검색이 가능한 hash 기반
## 키로 접근(key: value 항상 쌍)

# Set(집합) - 중괄호 사용

st = {1,3,5,7,9,3,1}

print(st)

# 중복 제거, 순서 없음
# 집합 연산(교집합, 차집합)