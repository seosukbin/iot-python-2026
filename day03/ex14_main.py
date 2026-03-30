## 메인 함수 개념

#__name__ 파이썬의 특별 함수(Special variable)
# __import__와 같은 특별 함수(Special method)
# dunder(double underscore): _가 두개씩 붙은 키워드

# 개발자가 사용하는것 __name__, __int__, __str__등 몇가지 사용
if __name__ == '__main__':
    print('프로그램 시작')
    print(__name__)