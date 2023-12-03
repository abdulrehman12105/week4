def calcArea():
    s= 2 #length of one side of hexagon
    AreaoFHexagon = 1.5*1.732*s
    print("Area of Hexagon:",AreaoFHexagon)
def calcPeri():
    s = 2
    PerioFHexagon = 6*s
    print("Peri of Hexagon is:",PerioFHexagon)
def calcAngleSum():
    a = 120 # one angle of Hexagon
    SumoFAngle = 6*a
    print("Sum of angles of Hexagon:",SumoFAngle)
def display():
    calcArea()
    calcPeri()
    calcAngleSum()
def calcAreaSquare():
    length = 3
    AreaoFSquare = 2*length
    print("Area of Square is :",AreaoFSquare)
def calcPeriSquare():
    length = 3
    PerioFSquare = 4*length
    print("Peri of square is:",PerioFSquare)
def displaySq():
    calcAreaSquare()
    calcPeriSquare()

choice = " "
while choice != "exit":
    print("Enter 1 to calculate area,perimeter and sum of angles of hexagon : ")
    print("Enter 2 to calculate area and perimeter of square : ")
    print("Press any other key to exit : ")
    choice = input()
    if choice == "1":
        display()
        break
    elif choice == "2":
        displaySq()
        break
    else:
        print("Wrong Choice!")
        break