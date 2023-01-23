import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="randi",
  password="",
  database ="toko_tamiya"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE toko_tamiya")