# Foodpicker - program do podpowiadania co możesz zjeść na podstawie rzeczy w Twojej lodówce
import time

products_list = []

def productAdd():
    while True:
        product = input("Podaj produkty z lodówki(wpisz f aby zakończyć wprowadzanie produktów)>> ").lower()
        if product != "f":
            products_list.append(product)
        elif product == "":
            continue
        else:
            break

def readFood():
    global meals
    global ingredients

    with open('meals.txt', 'r') as food:
        meals = food.readlines()
        meals = [meal.strip() for meal in meals]

    
    with open('ingredients.txt', 'r') as ing:
        ingredients = ing.readlines()
        ingredients = [ingredients.strip() for ingredients in ingredients]
        for i in range(len(ingredients)):
            ingredients[i] = [x.strip() for x in ingredients[i].split(',')]
        return meals, ingredients

def foodCompare(meals, ingredients, products_list):
    global prop
    prop = []
    products_set = set(products_list)
    for i in range(len(meals)):
        if set(ingredients[i]).issubset(products_set):
            prop.append(meals[i])
    return prop

def main():
    print('#' * 85)
    print('')
    print('Witaj w programie foodpicker! Ten program podpowie Ci co możesz zrobić do jedzenia!')
    print('')
    print('#' * 85)
    time.sleep(3)
    print('INFO: Wpisuj produkty pojedyńczo! Nie używaj polskich znaków oraz przecinków! Wielkość liter dowolna. Przykładowo wpisz: jajka lub oliwa z oliwek i naciśnij enter')
    time.sleep(3)
    productAdd()
    readFood()
    foodCompare(meals, ingredients, products_list)
    print("Potrawy, które możesz zrobić to:")
    time.sleep(1)
    for i in prop:
        print("-", i)
        time.sleep(0.5)

main()

