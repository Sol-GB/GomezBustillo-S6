
VictimasDeLuciana = ["virginia", "sol", "kally"]
print (VictimasDeLuciana)
"kally" in VictimasDeLuciana
VictimasDeLuciana.append("flor")
VictimasDeLuciana.insert(2, "pilar")
print(VictimasDeLuciana)



print("ingrese su edad")
edad = int(input())
if edad >= 15:
    print("tenes la edad para estar en la lista, luciana te persigue")
else:
    print("te podes salvar de luciana, felicitaciones")


numero = int(input("ingrese su nivel"))
if numero <=10:
    print("sos el nuevo sacrificio")
elif numero <=40:
    print("lo consideraremos")
elif numero <= 80:
    print("bienvenido al culto")
else: 
    print("quien sos y como nos encontraste")