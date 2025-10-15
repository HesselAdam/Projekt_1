import csv

CSV_FILE = 'products.csv'

# Funktion för att ladda produkterna och ändra datatyp.
def products_loader():
    products = []
    with open (CSV_FILE, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for product in csv_reader:
            product['price'] = int(product['price'])
            product['quantity'] = int(product['quantity'])
            products.append(product)
    return products


# Funktion för att spara om datan till csv filen.
def save_data(CSV_FILE, products):
    with open (CSV_FILE, 'a', newline='') as file:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv.writeheader()
        for product in products:
            csv.writerow(product)

# Funktion för att lägga till produkter i csv filen.
def add_product(products):
    print("---Add your product---")
    print()
    
    new_id = max(product['id'] for product in products) + 1 if products else 1
    name = input("Produkt namn: ")
    desc = input("Ange beskrivning: ")
    price = float(input("Ange pris: "))
    quantity = int(input("Ange antal i lager: "))
    new_product = {
        "id": new_id,
        "name": name,
        "desc": desc,
        "price": price,
        "quantity": quantity
    }
    products.append(new_product)
    return print(f"New product: {name} --> {price}")

# Funktion för att ändra data för produkt baserat på id.
def change_product(products):
    print("---Change product data---")

    product_id = int(input("Ange id för produkt du vill ändra data för: "))
    for product in products:
        if product['id'] == product_id:

            print(f"Nuvarande namn för produkten är: {product['name']}")
            new_name = input("Ange det nya namnet för produkten: ")
            product['name'] = new_name if new_name else product['name']

            print(f"Nuvarande namn för produkten är: {product['desc']}")
            new_desc = input("Ange det nya namnet för produkten: ")
            product['desc'] = new_desc if new_desc else product['desc']


