# US-Poland units calculator by dgrztl
import math

print("#"* 40)
print("")
print("WELCOME TO UNITS CALCULATOR BY DGRZYL")
print("")
print("#"* 40)
print("")

def printMainMenu():
    print("Choose what units you want to calculate: (type 1-7)")
    print("1) Celsius to Fahrenheit")
    print("2) Liters to Gallons")
    print("3) Meters to Feet")
    print("4) Kilometers to Miles")
    print("5) Kilograms to Pounds")
    print("6) Grams to Ounces")


def celsfahrCalculator():
    print("Choose what you want to calculate: (type 1-2)")
    print("1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    usr_input = input("Type here>> ")
    if usr_input == "1":
        cels = input("Give celsius value to calculate>> ")
        answ = int(cels) * (9 / 5) + 32
        print(f"Result is {answ} degrees Fahrenheit")
    elif usr_input == "2":
        fahr = input("Give fahrenheit value to calculate>> ")
        answ = (int(fahr) - 32) * (5 / 9) 
        print(f"Result is {answ} degrees Celsius")
    else:
        print("Wrong value!")

def programRunning():
    usr_input = input("Type here>> ")
    if usr_input == "1":
        celsfahrCalculator()
    elif usr_input == "2":
        print('')


printMainMenu()
programRunning()
