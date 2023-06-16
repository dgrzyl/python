# Foodpicker - program do podpowiadania co możesz zjeść na podstawie rzeczy w Twojej lodówce

products_list = []

def productAdd():
    while True:
        product = input("Podaj produkty z lodówki: (wpisz f aby zakończyć wprowadzanie produktów)").lower()
        if product != "f":
            products_list.append(product)
        else:
            break




# productAdd()
# print(products_list)