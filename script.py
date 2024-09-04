Ecco un semplice codice Python per eseguire le moltiplicazioni:

```python
def moltiplicazione(num1, num2):
    risultato = num1 * num2
    return risultato

num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

print("Il risultato della moltiplicazione è: ", moltiplicazione(num1, num2))
```

In questo codice, abbiamo definito una funzione chiamata `moltiplicazione` che prende due numeri e ritorna il loro prodotto. Quindi, chiediamo all'utente di inserire due numeri e li moltiplichiamo utilizzando la nostra funzione `moltiplicazione`. Infine, stampiamo il risultato.