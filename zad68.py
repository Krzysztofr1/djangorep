def jednolite(wyrazy):
    for i in range(len(wyrazy)-1):
        if wyrazy[i]!=wyrazy[i+1]:
            return False
    return True

lista_wyrazow=[]
with open("dane_napisy.txt", "r") as plik:
    for linia in plik:
        lista_wyrazow.append(linia.split())
#print(lista_wyrazow)
licznik=0
for wyrazy in lista_wyrazow:
    if len(wyrazy[0])==len(wyrazy[1]):
        if jednolite(wyrazy[0]) and jednolite(wyrazy[1]) and wyrazy[0][0]==wyrazy[1][0]:
            licznik+=1
print(licznik)

for wyrazy in lista_wyrazow:
    if sorted(wyrazy[0])==sorted(wyrazy[1]):
        licznik+=1
print(licznik)