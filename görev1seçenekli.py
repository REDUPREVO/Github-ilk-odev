a = float(input("sayı giriniz"))
b=float(input("bir sayı daha alalım"))
c=input("Yapmak istediğiniz işlemi seçiniz\n1-toplama\n2-çıkarma\n3-çarpma\n4-bölme\n5-mod alma\n6-üs alma")

if c == "1":
  print(a+b)#+
elif c =="2":
  print(a-b)#-
elif c == "3":
  print(a*b)#*
elif c=="4":
  print(a/b)#/
elif c== "5":
  print(a%b)#%
elif c=="6":
  print(a**b)#**
else:
  print("Hatalı seçim yaptınız")