# Foodpicker - program do podpowiadania co możesz zjeść na podstawie rzeczy w Twojej lodówce

products_list = []

def productAdd():
    while True:
        product = input("Podaj produkty z lodówki(wpisz f aby zakończyć wprowadzanie produktów)>> ").lower()
        if product != "f":
            products_list.append(product)
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
        return meals, ingredients

def foodCompare(meals, ingredients, products_list):
    prop = []
    

productAdd()
readFood()
foodCompare(meals, ingredients, products_list)

