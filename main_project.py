import csv
import os

CSV_FILE = 'products.csv'

# Funktion för att ladda produkterna och ändra datatyp.
def products_loader():
    products = []
    with open (CSV_FILE, 'r', encoding='latin-1') as file:
        csv_reader = csv.DictReader(file)
        for product in csv_reader:
            product['id'] = int(product['id'])
            product['price'] = float(product['price'])
            product['quantity'] = int(product['quantity'])
            product['sales_quantity'] = int(product['sales_quantity']) if product.get('sales_quantity') else 0
            product['sales_total'] = float(product['sales_total']) if product.get('sales_total') else 0.0
            products.append(product)
    return products

# Funktion för att spara om datan till csv filen.
def save_data(CSV_FILE, products):
    with open (CSV_FILE, 'w', newline='', encoding='latin-1') as file:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity', 'sales_quantity', 'sales_total']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

# Funktion för att lägga till produkter i csv filen.
def add_product(products):
    repeat = True
    while repeat == True:
        print("---Add your product---")
        print()

        new_id = max(product['id'] for product in products) + 1 if products else 1
        name = input("Produkt namn: ")
        desc = input("Ange beskrivning: ")
        price = float(input("Ange pris: "))
        quantity = int(input("Ange antal i lager: "))
        sales_quantity = int(input("Ange antal sålda: "))
        sales_total = float(input("Ange totalt försäljningsbelopp: "))
        new_product = {
            "id": new_id,
            "name": name,
            "desc": desc,
            "price": price,
            "quantity": quantity,
            "sales_quantity": sales_quantity,
            "sales_total": sales_total
        }
        products.append(new_product)
        print(f"New product: {name} --> {price}")
        add_another = input("Vill du lägga till en till produkt(Y/N): ").upper()
        if add_another == "N":
            break
    return products

# Funktion för att ändra data för produkt baserat på id.
def change_product(products):
    print("---Change product data---")

    product_id = int(input("Ange id för produkt du vill ändra data för: "))
    found = False

    for product in products:
        if product['id'] == product_id:
            found = True

            print(f"Nuvarande namn för produkten är: {product['name']}")
            new_name = input("Ange det nya namnet för produkten: ")
            if new_name:
                product['name'] = new_name

            print(f"Nuvarande beskrivning för produkten är: {product['desc']}")
            new_desc = input("Ange det nya beskrivningen för produkten: ")
            if new_desc:
                product['desc'] = new_desc

            print(f"Nuvarande pris för produkten är: {product['price']}")
            new_price_input = input("Ange det nya priset för produkten: ")
            if new_price_input:
                product['price'] = float(new_price_input)

            print(f"Nuvarande antal för produkten är: {product['quantity']}")
            new_quant_input = input("Ange det nya antalet av produkten: ")
            if new_quant_input:
                product['quantity'] = int(new_quant_input)

            print(f"Nuvarande antal sålda för produkten är: {product['sales_quantity']}")
            new_sales_quant_input = input("Ange det nya antalet sålda av produkten: ")
            if new_sales_quant_input:
                product['sales_quantity'] = int(new_sales_quant_input)

            print(f"Nuvarande totalt försäljningsbelopp för produkten är: {product['sales_total']}")
            new_sales_total_input = input("Ange det nya totala försäljningsbeloppet för produkten: ")
            if new_sales_total_input:
                product['sales_total'] = float(new_sales_total_input)

            print("Produkten har uppdaterats!")
            break

    if not found:
        print(f"Fel: Produkt med id {product_id} hittades inte!")

    return products
#
def sales_data(products):
    for product in products:
        idx = product['id']+1
        print(f"{idx}.) {product['name']}")
    val = int(input("Vilken produkt vill du se sälj-data om?: "))
    for product in products:
        if product['id']+1 == val:
            print(f"\nAntal sålda av [{product['name']}]: {product['sales_quantity']}")
            print(f"Omsättning av [{product['name']}]: {product['sales_total']} kr\n")
    return products

if __name__ == "__main__":
    prod = products_loader()

    while True:
        os.system('cls')
        print("\n--- MENY ---")
        print("1. Lägg till produkt")
        print("2. Ändra produkt")
        print("3. Sälj data")
        print("4. Avsluta")
        choice = input("Välj alternativ (1-4): ")

        if choice == "1":
            os.system('cls')
            prod = add_product(prod)
            save_data(CSV_FILE, prod)
        elif choice == "2":
            os.system('cls')
            prod = change_product(prod)
            save_data(CSV_FILE, prod)
        elif choice == "3":
            os.system('cls')
            sales_data(prod)
            input("Tryck Enter för att återgå till menyn...")
        elif choice == "4":
            print("Avslutar programmet...")
            break
        else:
            print("Ogiltigt val, försök igen.")