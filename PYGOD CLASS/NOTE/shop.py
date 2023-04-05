import utills
from pprint import pprint
last_index = 0
products_db = utills.get_products()
display_prods = []
def view_products():
    global last_index
    
    next_index = last_index + 2
    for prod in products_db[last_index:next_index]:
        hold = []
        hold.append(prod["id"])
        hold.append(prod["title"])
        hold.append(prod["price"]) 
        display_prods = hold
    last_index = next_index
    print(display_prods)


while True:
    print("1) view products")
    cmd = input("type here>> ")
    if cmd == "1":
        view_products()
    else:
        break