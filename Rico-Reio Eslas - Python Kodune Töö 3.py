#Iseseisev töö 3
#Rico-Reio Eslas

#3.1 Ülikooli vastuvõetud
fail = open("/Users/ricor/Desktop/rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
    vastuvõetud.append(int(rida))
fail.close()
aastad = (2011,2012,2013,2014,2015,2016,2017,2018,2019)
aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
rebased = vastuvõetud[aastad.index(aasta)]
print(str(aasta)+". aastal oli vastuvõetuid", rebased)


#3.2 Jänesevanemate mure ver.3
ringid = int(input("Sisesta ringide arv: "))
porgandid = 0
for i in range(1, ringid+1):
    if i%2==0:
        porgandid += i
print("Saadavate porgandite koguarv on", porgandid)


#3.3 Sissetulekud
fail = open("/Users/ricor/Desktop/konto.txt", encoding="UTF-8")
sissetulek = []
for rida in fail:
    if float(rida) > 0:
        sissetulek.append(float(rida))
fail.close()
for positiivne in sissetulek:
    print(positiivne)