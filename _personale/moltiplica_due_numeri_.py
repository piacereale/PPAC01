import sys

#path_script = sys.argv[0] 

if(sys.argv) !=3:
    print(' il numero di parametri passati non è corretto. Devi passare due numeri.')
else:
    primo_numero = float(sys.argv[1])
    secondo_numero = float(sys.argv[2])

    risultato = primo_numero * secondo_numero

    print(risultato)

    print(f'Il risultato di {primo_numero} per {secondo_numero} è uguale a {risultato}')


