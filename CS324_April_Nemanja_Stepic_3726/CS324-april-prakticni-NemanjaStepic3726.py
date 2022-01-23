 #zadatak 2
"""
class error(Exception):
     message= ''

class osoba():
     def __init__(self, ime, prezime):
         self.ime = ime
         self.prezime = prezime

class student(osoba):
     def __init__(self, ime, prezime, broj_indeksa, smer, polozeni_ispiti):
         osoba.__init__(self,ime,prezime)
         self.broj_indeksa = broj_indeksa
         self.smer = smer
         self.polozeni_ispiti = polozeni_ispiti

     def dodaj_polozen_ispit(self):
         predmet = input("Unesite sifru predmeta:")
         try:
             ocena = int(input("Unesite ocenu (od 6 do 10):"))
             if (ocena < 6) or (ocena > 10):
                 raise error("Pogresan unos")
             else:
                 self.polozeni_ispiti[predmet] = ocena
         except error as e:
                 print(e)

     def izracunaj_prosek(self):
         ukupno = len(self.polozeni_ispiti)
         ocene = 0
         for x in self.polozeni_ispiti.values():
             ocene += x 

         prosek = ocene/ukupno


         print("Student:  ",self.ime,self.prezime)
         print("Polozeni ispiti:  ",ukupno)
         print("Prosek:  ",prosek)

def studenti_ispiti (*stud):
     broj_stud = 0
     prvi_stud = True
     for s in stud:
         broj_stud += 1
    
     if broj_stud == 2:
        
         for s in stud:
             if prvi_stud:
                 prvi = len(s.polozeni_ispiti) 
                 prvi_stud = False
             else:
                 drugi = len(s.polozeni_ispiti)
         if prvi > drugi:
             print("Prvi student ima vise polozenih ispita")
         elif prvi < drugi:
             print("Drugi student ima vise polozenih ispita")
         else:
             print("Studenti su polozili isti broj ispita")
     else:
         print("Unesite 2 studenta")

# pravljenje studenata
student1 = student("Nemanja", "Stepic", 3724, "IT", {})
student2 = student("Marko", "Markovic", 1234, "SE", {})

#provera metode dodaj_ispit i izracunaj_prosek
student1.dodaj_polozen_ispit()
student1.dodaj_polozen_ispit()
student2.dodaj_polozen_ispit()


print(student1.polozeni_ispiti)

student1.izracunaj_prosek()

#provera koliko je koji student polozio ispita
studenti_ispiti(student1,student2) """



 # zadatak 3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 # Definicija funkcija g(x) i h(x) 
def g(x):
      return np.exp(-x * 0.2) * np.cos(5 * x) 

def h(x):
      return np.exp(-x * 0.5) * np.sin(2 * x)

 #kreiranje plotova
x = np.linspace(0, 10, 1000)               
plt.plot(x, g(x), 'b-', label="$g_x$")   
plt.plot(x, h(x), 'r--', label="$h_x$")    
plt.xlabel('$x$')                        
plt.ylabel('$funkcije$')
plt.xlim(0, 10)                           
plt.ylim(-1, 1)
plt.grid()                                
plt.savefig('funkcije.png')
plt.legend()                                
plt.show()
plt.title("Funkcije $g_x$ i $h_x$")

 #dodavanje u CSV fajl
csv = pd.DataFrame(list(zip(x,g(x), h(x))), columns=['x', 'g', 'h'])
csv.to_csv('funkcije.csv', index=False)




#prvi zadatak

#lista sa prostim brojevima
def prime_nums(a):
    prime_lst = []

    a += 1
    for br in range(a):
        if br > 2:
            for i in range(2, br):
                if (br % i) == 0:
                    break
            else:
                prime_lst.append(br)
    return prime_lst

def var_nums(prime_list):
    ukupno_srednja_vred = 0
    n_srednja_vred = 0
    ukupno_var = 0
    for x in prime_list:
        ukupno_srednja_vred += x
        n_srednja_vred += 1
    srednja_vred = ukupno_srednja_vred / n_srednja_vred
    
    for y in prime_list:
        var =  (y - srednja_vred)**2
        ukupno_var += var
    res = ukupno_var / n_srednja_vred
    return res

lista = prime_nums(100)
print("Lista prostih brojeva od 2 do 100: ",prime_nums(100))
print("Varijansa na dobijenu listu prostih brojeva: ",var_nums(lista))
