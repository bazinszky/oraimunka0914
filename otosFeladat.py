import beolvas
#Tárolj el két számot egy-egy változóba! Írd ki az összegüket,
# különbségüket, szorzatukat és hányadosukat, hatványukat!



szam1= beolvas.tortszambeolvas()
szam2=beolvas.tortSzamBeolvas()

#müveletek
osszeg = szam1+szam2
kulonbseg = szam1-szam2
szorzat = szam1*szam2
hanyados =szam1/szam2
maradek = szam1%szam2
hatvany = szam1**szam2

#kiírás

print(osszeg)
print(kulonbseg)
print(szorzat)
print(hanyados)
print(maradek)
print(hatvany)