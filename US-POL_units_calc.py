# US-Poland units calculator by dgrztl

import time

# This function prints menu
def printMainMenu():
    menu_options = [
        "1) Celsius to Fahrenheit",
        "2) Liters to Gallons",
        "3) Meters to Feet",
        "4) Kilometers to Miles",
        "5) Kilograms to Pounds",
        "6) Grams to Ounces"
    ]
    print("Choose what units you want to calculate: (type 1-6)")
    print("\n".join(menu_options))


# Those functions calculate units
def celsfahrCalculator():
    print("Choose what you want to calculate: (type 1-2)")
    print("1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    usr_input = input("Type here>> ")
    if usr_input == "1":
        cels = input("Give celsius value to calculate>> ")
        answ = float(cels) * (9 / 5) + 32
        print(f"Result is {round(answ, 3)} degrees Fahrenheit")
        time.sleep(3)
    elif usr_input == "2":
        fahr = input("Give fahrenheit value to calculate>> ")
        answ = (float(fahr) - 32) * (5 / 9) 
        print(f"Result is {round(answ, 3)} degrees Celsius")
        time.sleep(3)
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
        time.sleep(3)
    elif usr_input == "2":
        gal = input("Give gallons value to calculate>> ")
        answ = float(gal) * 3.785411784
        print(f"Result is {round(answ, 3)} liters")
        time.sleep(3)
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
        time.sleep(3)
    elif usr_input == "2":
        fet = input("Give feet value to calculate>> ")
        answ = float(fet) * 0.3048
        print(f"Result is {round(answ, 3)} meters")
        time.sleep(3)
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
        time.sleep(3)
    elif usr_input == "2":
        mil = input("Give miles value to calculate>> ")
        answ = float(mil) * (1 * 1.609344)
        print(f"Result is {round(answ, 3)} kilometers")
        time.sleep(3)
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
        time.sleep(3)
    elif usr_input == "2":
        pou = input("Give pounds value to calculate>> ")
        answ = float(pou) * 0.45359237
        print(f"Result is {round(answ, 3)} kilograms")
        time.sleep(3)
    else:
        print("Wrong value!")

def grmoncCalculator():
    print("Choose what you want to calculate: (type 1-2)")
    print("1) Grams to Ounces")
    print("2) Ounces to Grams")
    usr_input = input("Type here>> ")
    if usr_input == "1":
        grm = input("Give grams value to calculate>> ")
        answ = float(grm) * 0.03527396195
        print(f"Result is {round(answ, 3)} ounces")
        time.sleep(3)
    elif usr_input == "2":
        onc = input("Give ounces value to calculate>> ")
        answ = float(onc) * 28.34952
        print(f"Result is {round(answ, 3)} grams")
        time.sleep(3)
    else:
        print("Wrong value!")

# This function is resposible for running program 
def programRunning():
    while True:
        printMainMenu()
        usr_input = input("Type here (or 'q' to quit)>> ")
        if usr_input == "q":
            break
        elif usr_input == "":
            print('Invalid input! Cannot be empty')
            continue
        elif usr_input not in ["1", "2", "3", "4", "5", "6"]:
            print("Wrong input! Type a number from 1 to 6")
            continue

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
        elif usr_input == "6":
            grmoncCalculator()

# Main function
def main():
    print("#" * 45)
    print("\nWELCOME TO US-POL UNITS CALCULATOR BY DGRZYL\n")
    print("#" * 45)
    programRunning()

main()
