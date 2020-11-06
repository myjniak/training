jakies_numerki = "080 111 100 097 106 101 032 104 097 115 108 111 058 032 112 105 101 114 111 103 105"
lista_numerkow = jakies_numerki.split()
wyprint = ""
for numerek in lista_numerkow:
    wyprint += chr(int(numerek))
print(wyprint)
