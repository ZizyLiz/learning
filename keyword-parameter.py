def myFunc(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

def function(a, b ,c):
    d = a + b
    print(f"{c} = {d}")

myFunc("Aziz", 18, "Jogja") # Jika kita memberikan argument secara berurutan, maka tidak perlu menggunakan keyword-parameter
print("-"*25)
myFunc(age=18, name="Aziz", city="Jogja") # Namun jika lupa urutan parameternya, maka kita bisa menggunakan keyword-parameter
print("-"*25)
myFunc(18, "Aziz", "Jogja") # Jika kita menuliskan argument tanpa menggunakan keyword-parameter dan urutan tidak sesuai, maka akan terjadi kesalahan pada outputnya atau bahkan error
print("-"*25)
#function beda
function(2, 3, "2 + 3") # Jika kita memberikan argument secara berurutan, maka tidak perlu menggunakan keyword-parameter
print("-"*25)
function(c="2 + 3", a=2, b=3) # Namun jika lupa urutan parameternya, maka kita bisa menggunakan keyword-parameter
print("-"*25)
function(2, "Hasil", 3) # Jika kita menuliskan argument tanpa menggunakan keyword-parameter dan urutan tidak sesuai, maka akan terjadi kesalahan pada outputnya atau bahkan error