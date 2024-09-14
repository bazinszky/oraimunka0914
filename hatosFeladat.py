
szam1= beolvas.tortszambeolvas()
szam2=beolvas.tortSzamBeolvas()

#müveletek
osszeg = szam1+szam2
kulonbseg = szam1-szam2
szorzat = szam1*szam2
hanyados =szam1/szam2
maradek = szam1%szam2
hatvany1 = szam1**szam2
hatvany2 = szam2**szam1
#kiírás

print(str(szam1)+"+"+str(szam2)+"="+str(osszeg))
print(str(szam1) +"-"+str (szam2) +"="+str(kulonbseg))
print (str(szam1)+"*"+str(szam2)+"="+str(szorzat))
print(str(szam1)+"/"+str(szam2)+"="(hanyados))
print (str(szam1)+"^"+str(szam2)+"="+str(maradek))
print str(szam1)+"^"+str(szam2)+"="+str(hatvany1))
print str(szam2)+"^"+str(szam1)+"="+str(hatvany2))