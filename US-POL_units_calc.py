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
        answ = float(cels) * (9 / 5) + 32
        print(f"Result is {round(answ, 3)} degrees Fahrenheit")
    elif usr_input == "2":
        fahr = input("Give fahrenheit value to calculate>> ")
        answ = (float(fahr) - 32) * (5 / 9) 
        print(f"Result is {round(answ, 3)} degrees Celsius")
    else:
        print("Wrong value!")

def litgalCalculator():
    print("Choose what you want to calculate: (type 1-2)")
    print("1) Liters to Gallons")
    print("2) Gallons to Liters")
    usr_input = input("Type here>> ")
    if usr_input == "1":
        lit = input("Give liters value to calculate>> ")
        answ = float(lit) * 0.2641720524
        print(f"Result is {round(answ, 3)} gallons")
    elif usr_input == "2":
        gal = input("Give gallons value to calculate>> ")
        answ = float(gal) * 3.785411784
        print(f"Result is {round(answ, 3)} liters")
    else:
        print("Wrong value!")

def metfeetCalculator():
    print("Choose what you want to calculate: (type 1-2)")
    print("1) Meters to Feet")
    print("2) Feet to Meters")
    usr_input = input("Type here>> ")
    if usr_input == "1":
        met = input("Give meters value to calculate>> ")
        answ = float(met) * 3.280839895
        print(f"Result is {round(answ, 3)} feet")
    elif usr_input == "2":
        fet = input("Give feet value to calculate>> ")
        answ = float(fet) * 0.3048
        print(f"Result is {round(answ, 3)} meters")
    else:
        print("Wrong value!")

def kilmilCalculator():
    print("Choose what you want to calculate: (type 1-2)")
    print("1) Kilometers to Miles")
    print("2) Miles to Kilometers")
    usr_input = input("Type here>> ")
    if usr_input == "1":
        kil = input("Give kilometers value to calculate>> ")
        answ = float(kil) * (1 / 1.609344)
        print(f"Result is {round(answ, 3)} miles")
    elif usr_input == "2":
        mil = input("Give miles value to calculate>> ")
        answ = float(mil) * (1 * 1.609344)
        print(f"Result is {round(answ, 3)} kilometers")
    else:
        print("Wrong value!")

def kilpouCalculator():
    print("Choose what you want to calculate: (type 1-2)")
    print("1) Kilograms to Pounds")
    print("2) Pounds to Kilograms")
    usr_input = input("Type here>> ")
    if usr_input == "1":
        kilg = input("Give kilograms value to calculate>> ")
        answ = float(kilg) * 2.20462262185
        print(f"Result is {round(answ, 3)} pounds")
    elif usr_input == "2":
        pou = input("Give pounds value to calculate>> ")
        answ = float(pou) * 0.45359237
        print(f"Result is {round(answ, 3)} kilograms")
    else:
        print("Wrong value!")

def programRunning():
    usr_input = input("Type here>> ")
    if usr_input == "1":
        celsfahrCalculator()
    elif usr_input == "2":
        litgalCalculator()
    elif usr_input == "3":
        metfeetCalculator()
    elif usr_input == "4":
        kilmilCalculator()
    elif usr_input == "5": 
        kilpouCalculator()
    

printMainMenu()
programRunning()
