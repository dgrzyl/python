# Foodpicker - An app that suggests what you can eat based on the items in your fridge
import time

products_list = []

def productAdd():
    while True:
        product = input("Please provide the items from the fridge (type 'f' to finish entering the products)>> ").lower()
        if product != "f":
            products_list.append(product)
        elif product == "":
            continue
        else:
            break

def readFood():

    with open('meals_en.txt', 'r') as food:
        meals = food.readlines()
        meals = [meal.strip() for meal in meals]

    
    with open('ingredients_en.txt', 'r') as ing:
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
    print('Welcome to the Foodpicker program! This program will suggest what you can make for a meal!')
    print('')
    print('#' * 85)
    time.sleep(2)
    print('INFO: Enter the products one by one! Do not use Polish characters or commas! Letter case doesn\'t matter. For example, enter: eggs or olive oil and press enter')
    time.sleep(2)
    productAdd()
    meals, ingredients = readFood()
    foodCompare(meals, ingredients, products_list)
    print("The meals you can make are:")
    time.sleep(1)
    for i in prop:
        print("-", i)
        time.sleep(0.5)

main()

