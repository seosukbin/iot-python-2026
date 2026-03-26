
# ex02_array.py 리스트
arr= [10,20,30]
print(arr)
arr.append(70)    #스택과 같은데 append는 stack처럼 제일 마지막에 값을 넣는다. pop은 제일 마지막에 넣은거 먼저 뽑아 낸다.
print(arr)
print(arr.index(30))  #index는 리스트중 요소 위치 리턴
arr2 = arr.copy()
print(arr2)
arr.insert(2,90)
print(arr)
print(arr.pop()) # 70이 빠지게 된다
print(arr)
arr.remove(30) # 특정값이 삭제
print(arr)
arr.extend(arr2)
print(arr)

arr.reverse() #요소 순서를 역순으로 변경
print(arr)

arr.sort() # ASCending 정렬
print(arr)

arr.sort(reverse = True) #Python Descending 정렬
print(arr)

arr.append('Python')
print(arr)

arr.append([6,7,9])
print(arr)

arr.remove(30) #remove는 같은게 있으면 같은 요소 한개만 삭제
print(arr)

arr.clear()
print(arr)
