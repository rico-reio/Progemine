#Progemise iseseisev töö nr. 2
#Rico-Reio Eslas

#2.1 Bussid
inimesed = int(input("Inimeste arv: "))
kohad = int(input("Kohtade arv: "))
if inimesed > 40:
    print("Busside arv: 2")
else:
    print("Busside arv: 1")
viimane = inimesed % kohad
print("Viimases bussis inimesi: ",str(viimane),"")

#2.2 Äratus
äratus = int(input("Sisestage mitu korda äratada: "))   
for i in range(äratus):
    print("Tõuse ja sära!")
    
#2.4 Täringud
from random import randint
täringud = int(input("Täringute arv: "))
tulemus = randint(1,6)
for i in range(täringud):
    print(tulemus)
    tulemus = randint(1,6)