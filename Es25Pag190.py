'''
I voti assegnati a una classe di 30 studenti 
in una prova di italiano sono memorizzati
in un dizionario che ha per chiave la matricola mentre
il valore associato è il voto.
Elenca i risultati in ordine crescente di voto e successivamente visualizza
quali voti diversi tra loro sono stati assegnati,
riducendo a uno i voti assegnati.
'''
n_studenti = 30
studenti_voti = {}
for n in range(1, n_studenti +1):
    studente = input("inserire il nome dello studente")
    voto = float(input("Inserire il voto"))
    studenti_voti = {studente:voto}
print(studenti_voti)