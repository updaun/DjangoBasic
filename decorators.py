
def decorator(func):
    def decorated(input_text):
        print("함수 시작!")
        func(input_text)
        print("함수 끝!")

    return decorated


@decorator
def hello_world(input_text):
    print(input_text)


hello_world("Hello World!")

def decorator_1(func):
    def decorated_1(width, height):
        if width < 0 or height < 0:
            # 오류 발생 구문!
            raise ValueError('Input must be positive value')
        else:
            func(width, height)
    return decorated_1

@decorator_1
def area_triangle(width, height):
    print("삼각형의 넓이는 {}입니다.".format(width*height/2))

@decorator_1
def area_rectangle(width, height):
    print("사각형의 넓이는 {}입니다.".format(width*height))

area_triangle(3,5)
area_triangle(-3,5)

area_rectangle(3,5)
area_rectangle(-3,5)
