print("Nama : RANDI PRADITIYA")
print("Nim  :20210801265")
def capucino():
    cap = "Memilih Capucino"
    print(cap)
    capucino = int(input("Masukan Harga : "))
    ppn = capucino * 10/100
    total = capucino+ppn
    print("Jumlah Yang Harus Di Bayarkan", total)
def teh():
    T = "Memilih Teh"
    print(teh)
    teh = int(input("Masukan Harga : "))
    ppn = teh * 10/100
    total = teh+ppn
    print("Jumlah Yang Harus Di Bayarkan", total)
def pilihan():
    print("1. Capucino")
    print("2. Teh")
    print("3. exit")

while True:
    pilihan()
    pil=int(input("pilihan : "))
    if pil==1:
        capucino()
    elif pil==2:
        teh()
    else :
        break