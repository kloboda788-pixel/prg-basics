###
# Prints products with price < 60 and stock < 40
#
import csv

file_name = 'clothing.csv'

with open(file_name, 'r', encoding='utf-8') as file:
    # every row: [Product_ID, Product_Name, Category, Size, Color, Price, Stock_Quantity]
    reader = csv.reader(file)
    # skip the header line
    next(reader)
    for row in reader:
        # values read from a CSV file are texts, so they are converted
        price = float(row[5])
        stock = int(row[6])
        if price < 60 and stock < 40:
            print(f'{row[1]}, size {row[3]}, {row[4]}, price: {price}, stock: {stock}')