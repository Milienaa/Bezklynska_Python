#example 1
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

#example 2
class WeekDayError(Exception):
    pass


class Weeker:
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in self.__days:
            raise WeekDayError
        self.__current_day = day

    def __str__(self):
        return self.__current_day

    def add_days(self, n):
        current_index = self.__days.index(self.__current_day)
        new_index = (current_index + n) % len(self.__days)
        self.__current_day = self.__days[new_index]

    def subtract_days(self, n):
        current_index = self.__days.index(self.__current_day)
        new_index = (current_index - n) % len(self.__days)
        self.__current_day = self.__days[new_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

#example 3
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))

#task 1
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        a = self.__vertices[0].distance_from_point(self.__vertices[1])
        b = self.__vertices[1].distance_from_point(self.__vertices[2])
        c = self.__vertices[2].distance_from_point(self.__vertices[0])
        return a + b + c

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())