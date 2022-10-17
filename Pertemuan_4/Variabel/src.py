#variabel
a = "randi praditiya"
def func():
    a = "any"
    print ("selamat " + a)
func()
print (a)

#definisi
def tambah():
    a = 5
    b = 3
    c = a+b
    print (c)

tambah()

#definisi parameter
def data(nama,nim):
    print(f"nama saya {nama} dan {nim}")
data("Randi","20210801265")

#contoh 
def total(sisi):
    return sisi*sisi
def segitiga(alas,tinggi):
    return 0.5*alas*tinggi
    