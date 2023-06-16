# Foodpicker - program do podpowiadania co możesz zjeść na podstawie rzeczy w Twojej lodówce

products_list = []

def productAdd():
    while True:
        product = input("Podaj produkty z lodówki (wpisz 'f', aby zakończyć wprowadzanie produktów)>> ").lower()
        if product != "f":
            products_list.append(product)
        elif product == "":
            continue
        else:
            break

def readFood():
    with open('meals.txt', 'r') as food:
        meals = [meal.strip() for meal in food.readlines()]

    with open('ingredients.txt', 'r') as ing:
        ingredients = [line.strip().split(',') for line in ing.readlines()]
    
    return meals, ingredients

def foodCompare(meals, ingredients, products_list):
    prop = []
    products_set = set(products_list)
    for i in range(len(meals)):
        if set(ingredients[i]).issubset(products_set):
            prop.append(meals[i])
    return prop

def main():
    productAdd()
    meals, ingredients = readFood()
    prop = foodCompare(meals, ingredients, products_list)
    print(prop)

main()


