"""nome,cognome,eta
enrico, verdi, 52
alice, bianchi,36
giovanna, rossi, 22"""

#aprire il file
import os
import json

nomefile='nomefile.csv'
nomefile=os.path.abspath(nomefile)
with open('nomefile.csv',r) as fr: 

#leggere il file
  paperino = fr.read()


#dividere per righe
righe= paperino.split(\n)

#costruitre il dizionario
datdiz={}

#dividere ogni riga per coloonna
riga=0
for r in righe:
   colonne= r.split(';')
   print(r)
   print(colonne)

    if riga==0:
        chiavi=colonne
    else:
        dizdati[riga]={}
        dizdati[riga][chiavi[0]]=colonne[0]
        dizdati[riga][chiavi[1]]=colonne[1]
        dizdati[riga][chiavi[2]]=colonne[2]
    riga=riga+1
#print(dizdati)


#convertire il dizionario in json

jdata=json.dumps(dizdati)
#print('JSON - >', jdata)
#print('DIZIONARIO'->, dizdata)

#scrivere i dati in formato json
with open('jdati.json', w) as fw:
  fw.write(jdata)

    