import math as math
m = int(input("Enter the initial mass of the material: "))
while m <= 0:
    print("Error! The mass of the material must be a positive number!")
    m = int(input("Enter the initial mass of the material: "))
h = int(input("Enter half-life in days: "))
while h <= 0:
    print("Error! Half-life must be a positive number!")
    h = int(input("Enter half-life in days: "))
t = -1
while t < 20:
    t = t + 1
    mt = m * 0.5 ** (t / h)
    print("After day " + str(t) + " there are " + str(mt) + "grams remaining.")
