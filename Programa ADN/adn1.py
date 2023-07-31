import subprocess 
import os

def adn1(): 
    welcome="Bienvenido al programa de ADN1 lineal" 
    print(welcome) 
    print("Introduzca la cadena de ADN: ejemplo: AACTGTGAACTAACGTCTTAACGACTGGTACGTAC") 
    adn = input() 
   
    os.system("AMSjobs")
    p = subprocess.Popen(["AMSjobs"], stdout=subprocess.PIPE)
    for i in range(len(adn)): 
        print(adn[i])
        p.communicate(input=adn[i].encode())
         

print(adn1())