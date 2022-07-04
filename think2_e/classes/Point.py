import math
class Point:
    """Represents a point"""
def distance_between_points(p1,p2):
    distance = math.sqrt(((abs(p1.x - p2.x))**2) + ((abs(p1.y - p2.y))**2))
    return distance


def main():
    point1 = Point()
    point1.x = 10;
    point1.y = 10;

    point2 = Point()
    point2.x = 20;
    point2.y = 20;
    print(distance_between_points(point1,point2))

if __name__ == "__main__":
    main()
