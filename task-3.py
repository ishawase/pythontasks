import math

class distance:

    def __init__(self):
        self.point1 = ()
        self.point2 = ()

    def coordinatesOfPoint1(self):
        # for i in range(2):
        #     cds = tuple(input("enter co-ordinates of point1: "))
        #     self.point1 = self.point1 + cds
        x1, y1 = map(int, input("enter x1 and y1 co-ordinates of point1: ").split())
        self.point1 = (x1,y1)

    def coordintesOfPoint2(self):
        # for i in range(2):
        #     cds = tuple(input("enter x2 and y2 co-ordinates of point2: "))
        #     self.point2 = self.point2 + cds
        x2, y2 = map(int, input("enter x2 and y2 co-ordinates of point2: ").split())
        self.point2 = (x2,y2)

    def distanceBetween(self):
        self.distance = math.sqrt(
            (self.point2[0] - self.point1[0]) **2 +
            (self.point2[1] - self.point1[1]) **2
        )
        print(f"the distance between two point is: {self.distance}")

line = distance()
line.coordinatesOfPoint1()
line.coordintesOfPoint2()
line.distanceBetween()
