

#aprire il file
import os
import json

nomefile='./_personale/2024-04-23/NomeCognomeEta.csv'
#nomefile=os.path.abspath(nomefile)
with open(nomefile, "r",encoding='utf-8') as fr: #UniversalTypograficFormat (UTF). Se fosse ascii (american s...) non sa leggere le vocali accentate

#leggere il file
  paperino = fr.read()


#dividere per righe
righe= paperino.split("\n")

#costruitre il dizionario
dizdati={}

#dividere ogni riga per coloonna
riga=0
for r in righe:
   colonne= r.split(',')
   print(r)
   print(colonne)

   if riga==0:
      chiavi=colonne
   else:
      dizdati[riga]={
         chiavi[0] : colonne[0],
         chiavi[1] : colonne[1],
         chiavi[2] : colonne[2]
      }
   riga=riga+1
#print(dizdati)


#convertire il dizionario in json

jdata=json.dumps(dizdati)
#print('JSON - >', jdata)
#print('DIZIONARIO'->, dizdata)

#scrivere i dati in formato json
with open('jdati.json', "w", encoding='utf-8') as fw:
  fw.write(jdata)
  
#adesso facciamo il contrario
#leggiamo il file json
with open('jdati.json', 'r', encoding='utf-8') as fr:
   buffer=fr.read()

#lo ritrasformo in un dizionario
dicDatiNew = json.loads(buffer)
print(dicDatiNew)

#rifaccio il file csv
chiavi=dicDatiNew.keys()
print(chiavi)

righe=0
file=[]

for k in chiavi:
   dicPiccolo=dicDatiNew[k]
   chiaviCSV = dicPiccolo.keys()
   rigaCSV=''
   if righe==0:
      rigaIntestazione=''
      for k2 in chiaviCSV:
         rigaIntestazione += k2 + ';'
      print(rigaIntestazione)
      intestazione = rigaIntestazione[:-1]  #togliamo l'ultimo punto e virgola
      intestazione = intestazione + '\n'
      file.append(intestazione)
      righe +=1
  
   else:
      for k3 in chiaviCSV:
         rigaCSV += dicPiccolo[k3] + ';'
      rigaCSV=rigaCSV[:-1] + '\n'
      print(rigaCSV)
      file.append(rigaCSV)

print(file)


#Devo scrivere il nuovo file csv
buffer=''
for z in file:
   buffer += z

buffer=buffer[:-1] #l'ultimo a capo crea una riga vuota. 

with open('nuovoCSV.CSV', 'w', encoding ='utf-8') as fw:
   fw.write(buffer)




    