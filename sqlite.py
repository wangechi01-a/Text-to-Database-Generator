import sqlite3

# Create the database connection
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Create Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL,
    registration_date DATE NOT NULL
)
""")

# Create Products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL,
    added_date DATE NOT NULL
)
""")

# Create Orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    total_amount REAL NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

# Create Order Items table
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price_per_unit REAL NOT NULL,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
""")

# Insert sample data into Users table (Increased number of users)
cursor.executemany("""
INSERT INTO users (name, email, phone, address, registration_date)
VALUES (?, ?, ?, ?, ?)
""", [
    ("Eunice Muriithi", "eunicemuriithi034@gmail.com", "0712345678", "Nairobi, Kenya", "2024-01-10"),
    ("Peter Kamau", "mwangikamau@gmail.com", "0723456789", "Kiambu, Kenya", "2024-01-15"),
    ("Christine Atieno", "akinyiatieno0@gmail.com", "0734567890", "Kisumu, Kenya", "2024-02-10"),
    ("Omollo Ochieng", "omolloochieng09@gmail.com", "0745678901", "Homabay, Kenya", "2024-02-20"),
    ("Jane Njeri", "wanjikunjeri@gmail.com", "0756789012", "Nakuru, Kenya", "2024-03-01"),
    ("James Mwangi", "jamesmwangi@gmail.com", "0771234567", "Mombasa, Kenya", "2024-04-05"),
    ("Linda Wambui", "lindawambui@gmail.com", "0782345678", "Nairobi, Kenya", "2024-04-10"),
    ("Samuel Otieno", "samuelotieno@gmail.com", "0793456789", "Nakuru, Kenya", "2024-04-15"),
    ("Grace Njiru", "gracenjiru@gmail.com", "0704567890", "Kisumu, Kenya", "2024-04-20"),
    ("Mark Otieno", "markotieno@gmail.com", "0715678901", "Kisii, Kenya", "2024-04-25")
])

# Insert sample data into Products table (Increased number of products)
cursor.executemany("""
INSERT INTO products (name, description, category, price, stock, added_date)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    ("Samsung S23 Ultra", "Affordable Android smartphone", "Electronics", 15000.00, 100, "2024-01-15"),
    ("Hp EliteBook 840", "14-inch lightweight laptop", "Electronics", 70000.00, 30, "2024-02-01"),
    ("Ramtons Blender", "High-speed blender", "Home Appliances", 5000.00, 80, "2024-02-20"),
    ("L-Shaped Sofa Set", "Comfortable 3-seater sofa", "Furniture", 45000.00, 10, "2024-03-01"),
    ("Sony WH-1000XM5", "Noise-canceling headphones", "Electronics", 25000.00, 50, "2024-03-10"),
    ("Lenovo ThinkPad", "Business laptop", "Electronics", 85000.00, 20, "2024-03-15"),
    ("Dyson Vacuum Cleaner", "High-performance vacuum cleaner", "Home Appliances", 35000.00, 40, "2024-03-25"),
    ("Dining Table Set", "Elegant wooden dining table", "Furniture", 60000.00, 15, "2024-04-01"),
    ("LG OLED TV", "55-inch 4K OLED TV", "Electronics", 120000.00, 25, "2024-04-05"),
    ("Sofa Bed", "Convertible sofa bed", "Furniture", 30000.00, 5, "2024-04-10")
])

# Insert sample data into Orders table (Increased order count)
cursor.executemany("""
INSERT INTO orders (user_id, order_date, total_amount, status)
VALUES (?, ?, ?, ?)
""", [
    (1, "2024-03-05", 17000.00, "Delivered"),
    (2, "2024-03-10", 3000.00, "Shipped"),
    (3, "2024-03-15", 45000.00, "Processing"),
    (4, "2024-03-20", 70000.00, "Delivered"),
    (5, "2024-03-25", 12000.00, "Cancelled"),
    (6, "2024-04-01", 35000.00, "Shipped"),
    (7, "2024-04-03", 50000.00, "Delivered"),
    (8, "2024-04-06", 20000.00, "Delivered"),
    (9, "2024-04-07", 55000.00, "Processing"),
    (10, "2024-04-10", 40000.00, "Shipped")
])

# Insert sample data into Order Items table (Increased number of order items)
cursor.executemany("""
INSERT INTO order_items (order_id, product_id, quantity, price_per_unit)
VALUES (?, ?, ?, ?)
""", [
    (1, 1, 1, 15000.00),
    (1, 3, 1, 5000.00),
    (2, 4, 1, 3000.00),
    (3, 2, 1, 70000.00),
    (4, 5, 1, 25000.00),
    (5, 6, 1, 85000.00),
    (6, 7, 1, 35000.00),
    (7, 8, 1, 60000.00),
    (8, 9, 1, 120000.00),
    (9, 10, 1, 30000.00)
])

# Commit and close the database
conn.commit()
conn.close()

print("E-commerce database created successfully!")
