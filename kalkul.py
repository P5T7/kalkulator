#tampilan
print("+--------------------------------+")
print("|     KALKULATOR SEDERHANA       |")
print("|            by.RA7              |")
print("+--------------------------------+")
print("|                                |")
print("|      1.penjumlahan             |")
print("|      2.pengurangan             |")
print("|      3.perkalian               |")
print("|      4.pembagian               |")
print("|      5.pembagian bulat         |")
print("|      6.sisa bagi               |")
print("|      7.pangkat                 |")
print("|      8.exit                    |")
print("|                                |")
print("+--------------------------------+")
while True:
  #data masuk user
  pilih = int(input("############~PILIH~#############:"))
  x = int(input("~~~angka pertama ="))
  y = int(input("~~~angka kedua ="))
# data esekusi
  if pilih == 1:
    hasil = x + y
    print(x , "+" , y , "=" , hasil)
    
  elif pilih == 2:
    hasil = x - y
    print(x , "-" , y , "=" , hasil)
    
  elif pilih == 3:
    hasil = x * y
    print(x , "*" , y , "=" , hasil)
    
  elif pilih == 4:
    hasil = x / y
    print(x , "/" , y , "=" , hasil)
    
  elif pilih == 5:
    hasil = x // y
    print(x , "//" , y , "=" , hasil)
    
  elif pilih == 6:
    hasil = x % y
    print(x , "%" , y , "=" , hasil)
    
  elif pilih == 7:
    hasil = x ** y
    print(x , "**" , y , "=" , hasil)
 
  else:
   print ("salah goblok!!!")

  lagi = str(input("masih mau megunakan kakulator[y/n]"))
  if lagi.upper() != "Y":
    break