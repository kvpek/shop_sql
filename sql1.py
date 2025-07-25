import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    amount integer
)
""")

conn.commit()

# cursor.execute("""
# INSERT INTO products(name, price, amount)
# VALUES ('Laptopp', 3000, 5)
# """)

# conn.commit()
def show_products():
    x = cursor.execute("""
    SELECT * FROM products
                """)

    rows = cursor.fetchall()
    print("ID | NAME | PRICE [PLN] | AMOUNT ")
    print("-" * 40)
    for row in rows:
        print(f"{row[0]:<2}|{row[1]:<12}|{row[2]:<5}|{row[3]:<5}")

def add_product():
    name1 = input("Name of new product: ")
    price1 = float(input("Price of the new product: "))
    amount1 = int(input("Amount: "))
    
    cursor.execute("""
               INSERT INTO PRODUCTS (name, price, amount)
               Values (?, ?, ?)
               """, (name1, price1, amount1))
    conn.commit()
    
def update_amount():
    id2 = int(input("Id: "))
    amount2 = int(input("Amount: "))
    cursor.execute(
        "UPDATE products SET amount = ? WHERE id = ?"
        , (amount2, id2)
    )
    conn.commit()
    
def delete_product():
    id3 = int(input("ID: "))
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id3,)
    )
    conn.commit()
      
def update_price():
    id3 = int(input("Id: "))
    price3 = float(input("New price: "))
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?"
        , (price3, id3)
    )
    conn.commit()
    
def show_stats():
    cursor.execute("SELECT SUM (price *amount) FROM products")
    result = cursor.fetchone()
    print(f"Warehouse value : {result[0]} [PLN]")
    

while True:
    print("Choose what action to you want to do: \n 1. Show all products. \n 2. Add new product. \n 3. Update amount. \n 4. Delete product. \n 5. Update price. \n 9. Warehouse value stats. \n 10. End of action.")
    x = int(input("Number: "))

    if x == 1:
        show_products()
    if x == 2:
        add_product()
    if x == 3:
        update_amount()
    if x == 4:
        delete_product()
    if x == 5:
        update_price()
    if x == 9:
        show_stats()
    if x == 10:
        break


    
conn.close()
