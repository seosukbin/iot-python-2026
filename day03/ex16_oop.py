class Dog:
    #생성자
    def __init__(self):
        self.name = '뽀삐'

    def bark(self):
        print(f'{self.name}이 짖습니다. 멍멍!')

poppy = Dog()
print(poppy.bark())