'''
I voti assegnati a una classe di 30 studenti 
in una prova di italiano sono memorizzati
in un dizionario che ha per chiave la matricola mentre
il valore associato è il voto.
Elenca i risultati in ordine crescente di voto e successivamente visualizza
quali voti diversi tra loro sono stati assegnati,
riducendo a uno i voti assegnati.
'''
import random as r
    
def dizionario_inizializza():
       
    while len(studenti) < tot:
        studenti[r.randint(1,30)] = r.randint(1, 10)
    
        

def studenti_ordinati():
    print("Elenco studenti ordinati per voto in modo crescente")
    for chiave in sorted(studenti, key = studenti.get):
        print("studente", chiave, "=", studenti[chiave])

def voti_distinti():
    print("Elenco voti distinti")
    for voto in set(studenti.values()):
        print("voto =", voto)

def main():
    global tot
    global studenti
    global classe
    
    tot = 30
    studenti = {}
    classe = {"Mario Rossi":1,
              "Enrico Bianchi":2,
              "Matteo Zaccarelli":3,
              "Antonio Bruno":4,
              "Andrea De Luca":5,
              "Lucia Mondella":6,
              "Renzo Tramaglino":7,
              "Marco Fontana":8,
              "Giorgia Gallo":9,
              "Aurora Conti":10,
              "Andra Barbera":11,
              "Marta Angela":12,
              "Bartolomeo Ferrero":13,
              "Andrea Bondavalli":14,
              "Giovanni Storti":15,
              "Aldo Baglio":16,
              "Dante Alighieri":17,
              "Giacomo Poretti":18,
              "Alberto Ferrari":19,
              "Alessia D'Angelo":20,
              "Arianna Russo":21,
              "Marco Romano":22,
              "Martina Esposito":23,
              "Mariangela Ricci":24,
              "Giorgio Greco":25,
              "Lorenzo Rinaldi":26,
              "Luca Gentile":27,
              "Irene Leone":28,
              "Aleessio Longo":29,
              "Mirco Martinelli":30}
    dizionario_inizializza()
    
    while True:
        print("\nOperazioni possibili")
        print("[1] Mostra elenco studenti con voto \n[2] Mostra elenco voti distinti")
        scelta = input("cosa vuoi fare ")
        if not scelta.isdigit():
            print("\nErrore nella digitazione, riprova ...\n")
        else:
            scelta_int = int(scelta)
            if scelta_int == 1:
                print("Ad ogni voto è associato un numero,tale numero corrisponde ad uno studente,")
                print("per capire di chi è un voto, consultare il seguente dizionario. ")
                print(classe)
                studenti_ordinati()
                
            elif scelta_int == 2:
                voti_distinti()
                break
            else:
                print("\nHai digitato male, riprova ...\n")
main()
