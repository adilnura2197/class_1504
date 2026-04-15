#11
class Mashina:
    gildirak = 4


m1 = Mashina()
m1.rang = "Yashil"
m1.model = "Malibu"
m1.narx = 200
print(f"m1 rangi: {m1.rang}")
print(f"m1 modeli: {m1.model}")
print(f"m1 narxi: {m1.narx}")
print()

m2 = Mashina()
m2.rang = "Oq"
m2.tezlik = 290
m2.yoqilgi = 23
print(f"m2 rangi: {m2.rang}")
print(f"m2 tezligi: {m2.tezlik}")
print(f"m2 yoqilg'isi: {m2.yoqilgi}")
print()

m3 = Mashina()
m3.model = "BMW"
m3.narx = 500
m3.yil = 2024
print(f"m3 modeli: {m3.model}")
print(f"m3 narxi: {m3.narx}")
print(f"m3 yili: {m3.yil}")


#12
class Telefon:
    pass


t1 = Telefon()
t1.narx = 5400
t1.kamera = 12
t1.xotira = 128
print(f"t1 narxi: {t1.narx}")
print(f"t1 kamerasi: {t1.kamera}")
print(f"t1 xotirasi: {t1.xotira}")
print()

t2 = Telefon()
t2.narx = 5400
t2.rang = "Qora"
t2.xotira = 128
print(f"t2 narxi: {t2.narx}")
print(f"t2 kamerasi: {t2.rang}")
print(f"t2 xotirasi: {t2.xotira}")
print()

t3 = Telefon()
t3.brand = "Samsung"
t3.model = "Galaxy A 52"
t3.sim_soni = 12
print(f"t3 brandi: {t3.brand}")
print(f"t3 modeli: {t3.model}")
print(f"t3 sim soni: {t3.sim_soni}")
