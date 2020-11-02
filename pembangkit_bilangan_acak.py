
def mixed_conqruent_method():
  print("Mixed Conqruent Method")
  jumlahBilanganAcak = int(input("Masukan jumlah Bilangan Randam : "))
  z0 = int(input("Masukan z0 : "))
  m = int(input("Masukan nilai m :"))
  c = int(input("Masukan nilai c :"))
  a = int(input("Masukan nilai a :"))
  print('====================================')
  print('i        zi       m      a      zi+1')
  print('====================================')
  for x in range(jumlahBilanganAcak):
    hasil1 = (a * z0 + c) % m
    print(x ,"\t", z0, "\t", m, "\t", a, "\t", hasil1)
    z0 = hasil1

  print('===================================')


def multiplicative_method():
  print("multiplicative_method")
  jumlahBilanganAcak = int(input("Masukan jumlah Bilangan Randam : "))
  z0 = int(input("Masukan z0 : "))
  m = int(input("Masukan nilai m :"))
  a = int(input("Masukan nilai a :"))
  print('====================================================')
  print('i        zi       m      a      zi+1       Ri+1')
  print('====================================================')
  for x in range(jumlahBilanganAcak):
    hasil1 = (a * z0) % m
    r = hasil1 / m
    print(x ,"\t", z0, "\t", m, "\t", a, "\t", hasil1, "\t",r)
    z0 = hasil1

  print('====================================================')



print("Pembangkit Bilangan Acak")
print("------------------------")
print("Silahkan Pilih metode yg ingin digunakan")
print('1. Mixed Conqruent Method')
print('2. Multiplicate Method (RNG)')
print('-----------------------------------------')

pilihan = int(input("Masukan Pilihan :"))

if pilihan == 1:
  mixed_conqruent_method()
elif pilihan == 2:
  multiplicative_method()
else:
  print ("Masukan Pilihan dengan benar")

