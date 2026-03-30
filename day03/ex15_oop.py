## ex15_oop.py 객체 지향

class dog:
    pass # 내용을 넣어야 되는데 어떻게 적어야될지 모를때 pass를 작성 하면 된다. 
    
if __name__ == '__main__':
    poppy = dog() # 클래스 인스턴스 객체 생성, c++와 달리 new를 안쓴다
    poppy.name = "뽀삐"
    poppy.age = 3

    print(f'강아지 이름: {poppy.name}{poppy.age}살')
