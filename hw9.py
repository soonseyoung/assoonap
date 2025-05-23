# Point 클래스 정의
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Rectangle 클래스 정의
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(min(x1, x2), min(y1, y2))  # left-top
        self.rb = Point(max(x1, x2), max(y1, y2))  # right-bottom

    def getWidth(self):
        return self.rb.x - self.lt.x

    def getHeight(self):
        return self.rb.y - self.lt.y

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())

    def show(self):
        print(f"좌측 상단 꼭지점이 ({self.lt.x}, {self.lt.y})이고 "
              f"우측 하단 꼭지점이 ({self.rb.x}, {self.rb.y})인 사각형입니다.")

# 테스트 코드
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f"\n넓이는 {a}, 둘레는 {p}")