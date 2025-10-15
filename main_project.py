import csv

CSV_FILE = 'products.csv'

# Funktion för att ladda produkterna och ändra datatyp
def products_loader():
    products = []
    with open (CSV_FILE, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for product in csv_reader:
            product['price'] = int(product['price'])
            product['quantity'] = int(product['quantity'])
            products.append(product)
    return products


