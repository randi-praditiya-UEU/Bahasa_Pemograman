import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="toko_tamiya"
)

cursor = db.cursor()
sql = """CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(255),
  alamat Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")