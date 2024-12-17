import pyxel
import random

pyxel.init(128, 100, title="grenouille robotique")
vie = 3
nom = ""
compteur = 0
nom_entrer = False
meilleur_joueur = ""
meilleur_score = -1
victoire = False
bosse_up = 0
vie_bosse = 100
time = 0 
taille = 1
bosse_x = 60
bosse_y = 40
vis = vie
liste_vie = []
point = 0
grenouille_x = 10
grenouille_y = 82
aller_retour = 0
arduino_liste = []
virus_liste = []
langue_active = False
langue_longueur = 0
langue_max = 50
langue_direction = 1
cible_x=30
cible_y=60
point_bosse = 0
bosse_batue = 0 
liste_cible_x=[30, 40, 50, 60, 70, 80, 90]  
pyxel.load("PYXEL_RESOURCE_FILE.pyxres")
pyxel.playm(2, loop=True)
for i in range(vie):
        liste_vie.append([60 + 10 * i, 2, 1])
with open("scores.txt", "r") as fichier:
        for ligne in fichier:
            nom1, score = ligne.strip().split(":")
            score = int(score)
            if score > meilleur_score:
                ancien_record = score

aceuille = 0
def ecrant_acceuille():
    global aceuille
    pyxel.text(2,10, "binvenue sur 'gloups je mange ", 7)
    pyxel.text(2,20, "l'arduino', tu est une", 7)
    pyxel.text(2,30, "grenouille et ton objectif est", 7)
    pyxel.text(2,40, "de gagner des calcules, tu dois", 7)
    pyxel.text(2,50, "donc manger le plus d'arduino ", 7)
    pyxel.text(2,60, "tout en esquivant les virus", 7)
    pyxel.text(12,80, "presse ESPACE pour demarrer", 10)
    if pyxel.btnr(pyxel.KEY_SPACE):
        aceuille = 1

def taper_nom():
    global nom, nom_entrer
    if pyxel.btnp(pyxel.KEY_BACKSPACE): 
        nom = nom[:-1]

    for i in range(pyxel.KEY_A, pyxel.KEY_Z + 1):
        if pyxel.btnp(i):
            nom += chr(i)
                
    if pyxel.btnp(pyxel.KEY_RETURN):
        nom_entrer = True
        enregistrer_score()

def ecrant_mort():
    global point, nom, nom_entrer, meilleur_score, meilleur_joueur
    trouver_meilleur_score()
    pyxel.cls(0)
    if ancien_record <= point and (compteur // 10) % 2 == 0:
         pyxel.text(37, 2, "nouveau record", pyxel.frame_count % 16)
    pyxel.text(5, 20, "meilleur score: " + str(meilleur_score) + " par " + str(meilleur_joueur) , 7)
    pyxel.text(45,10, 'game over', 8)
    pyxel.text(37,30, 'ton score '+ str(point), 7)
    pyxel.text(5, 50, "Entrez votre nom: ", 7)
    pyxel.text(5, 60, nom, 7)
    taper_nom()
    if nom_entrer :
        pyxel.text(7,70, "presse ESPACE pour redemarrer", 10)
        if pyxel.btnr(pyxel.KEY_SPACE):
            initialisation()
            vie=vis
    

def appariton_des_vie():
    global liste_vie
    for vi in liste_vie:
        if vi[2]==1:
            pyxel.blt(vi[0], vi[1], 0, 0, 0, 8, 8, 0)
        if vi[2]==0:
            pyxel.blt(vi[0], vi[1], 0, 8, 0, 8, 8, 0)

def initialisation():
    global vie, ancien_record, nom, vis, liste_vie, point, grenouille_x, grenouille_y, aller_retour, arduino_liste, virus_liste, langue_active, langue_longueur, langue_max, langue_direction, vie_bosse, taille, victoire, bosse_up, point_bosse, time, bosse_batue, nom_entrer
    nom_entrer = False
    bosse_up = 0
    nom = ""
    point_bosse = 0
    time = 0 
    vie = 3
    vie_bosse = 100
    taille = 1  
    liste_vie = []
    point = 0
    grenouille_x = 10
    grenouille_y = 82
    aller_retour = 0
    arduino_liste = []
    virus_liste = []
    langue_active = False
    langue_longueur = 0
    langue_max = 50
    langue_direction = 1
    for i in range(vie):
        liste_vie.append([60 + 10 * i, 2, 1])
    with open("scores.txt", "r") as fichier:
        for ligne in fichier:
            nom1, score = ligne.strip().split(":")
            score = int(score)
            if score > meilleur_score:
                ancien_record = score

def enregistrer_score():
    global point
    scores = {}
    
    with open("scores.txt", "r") as fichier:
        for ligne in fichier:
            nom_joueur, score = ligne.strip().split(":")
            scores[nom_joueur] = int(score)
    
    scores[nom] = max(point, scores.get(nom, 0)) 
    
    with open("scores.txt", "w") as fichier:
        for joueur, score in scores.items():
            fichier.write(f"{joueur}:{score}\n")

def trouver_meilleur_score():
    global meilleur_score, meilleur_joueur
    meilleur_score = 0
    meilleur_joueur = ""
    with open("scores.txt", "r") as fichier:
        for ligne in fichier:
            nom, score = ligne.strip().split(":")
            score = int(score)
            if score > meilleur_score:
                meilleur_score = score
                meilleur_joueur = nom

def initialisation_bosse():
    global vie, vis, liste_vie, point, grenouille_x, grenouille_y, aller_retour, arduino_liste, virus_liste, langue_active, langue_longueur, langue_max, langue_direction, vie_bosse, taille, victoire, point_bosse, bosse_up, time, bosse_batue
    bosse_up = 0
    point_bosse = 0
    time = 0 
    vie_bosse = 100
    taille = 1  
    grenouille_x = 10
    grenouille_y = 82
    aller_retour = 0
    arduino_liste = []
    virus_liste = []
    langue_active = False
    langue_longueur = 0
    langue_max = 50
    langue_direction = 1

def arduino_creation(arduino_liste):
    if len(arduino_liste) <= 5:
        arduino_liste.append([random.randint(10, 110), random.randint(15, 50), random.randint(1, 10)])
    return arduino_liste

def arduino_deplacement(arduino_liste):
    new_arduino_liste = []
    for arduino in arduino_liste:
        arduino[random.randint(0, 1)] += random.randint(int(-2), int(2))
        
        if 0 <= arduino[0] <= 128 and 15 <= arduino[1] <= 75:
            new_arduino_liste.append(arduino)
    return new_arduino_liste

def virus_creation(virus_liste):
    if len(virus_liste) <= 5:
        virus_liste.append([random.randint(10, 110), random.randint(15, 50)])
    return virus_liste

def virus_deplacement(virus_liste):
    new_virus_liste = []
    for virus in virus_liste:
        virus[random.randint(0, 1)] += random.randint(int(-2), int(2))
        if 0 <= virus[0] <= 128 and 20 <= virus[1] <= 75:
            new_virus_liste.append(virus)
    return new_virus_liste

def deployer_langue():
    global langue_longueur, langue_direction, arduino_liste, virus_liste, langue_active, vie, point, vie_bosse, cible_x, cible_y, point_bosse
    
    if langue_direction == 1:
        langue_longueur += 6

        if point_bosse >= 1000:
            if pyxel.pget(grenouille_x + 7, 90-langue_longueur) == 7 or pyxel.pget(grenouille_x + 8, 90-langue_longueur) == 7:
                cible_x = liste_cible_x[random.randint(0, len(liste_cible_x) - 1)]  
                langue_direction = -1 
                vie_bosse -= 10   
            if pyxel.pget(grenouille_x + 7, 90-langue_longueur) == 9 and (90-langue_longueur)>30:
                langue_direction = -1  
                vie -= 1  
                mettre_a_jour_vies()

        elif point_bosse<1000:  
            for arduino in arduino_liste[:]:  
                if (grenouille_x + 7 < arduino[0] + 10 and grenouille_x + 7 + 2 > arduino[0]  and grenouille_y - langue_longueur < arduino[1] + 8  and grenouille_y - langue_longueur + 4 > arduino[1]):
                    arduino_liste.remove(arduino)
                    langue_direction = -1  
                    point += 100
                    point_bosse += 100
                    if arduino[2] == 1 :
                        vie += 1
                        mettre_a_jour_vies()  

            for virus in virus_liste[:]:  
                if (grenouille_x + 7 < virus[0] + 10 and grenouille_x + 7 + 2 > virus[0] and grenouille_y - langue_longueur < virus[1] + 9  and grenouille_y - langue_longueur + 4 > virus[1]):
                    virus_liste.remove(virus)
                    langue_direction = -1  
                    vie -= 1  
                    mettre_a_jour_vies()

        if grenouille_y - langue_longueur <= 0:
            langue_direction = -1

    elif langue_direction == -1:
        langue_longueur -= 4
        if langue_longueur <= 0:
            langue_longueur = 0
            langue_active = False
            langue_direction = 1
    
def mettre_a_jour_vies():
    global liste_vie, vie
    for i in range(len(liste_vie)):
        if i < vie:
            liste_vie[i][2] = 1
        else :
            liste_vie[i][2] = 0

def bosse():
    global taille, bosse_up
    if taille < 5:
        taille = taille *1.01
    else:
        bosse_up = 1
    
def update():
    global grenouille_x, grenouille_y, aller_retour, arduino_liste, virus_liste, langue_active, vie, point, liste_vie, bosse_x, bosse_y, taille, cible_x, liste_cible_x, time
    if time > 100:
        cible_x = liste_cible_x[random.randint(0, 6)]
        time = 0
    if pyxel.btnr(pyxel.KEY_SPACE) and not langue_active and aceuille == 1:
        langue_active = True
    if point >= 100:
        bosse()
    if langue_active:
        deployer_langue()
    else:
        if aller_retour == 0:
            grenouille_x += int(1+(point/600))
        else:
            grenouille_x -= int(1+(point/600))

        if grenouille_x > 105:
            aller_retour = 1
        elif grenouille_x < 10:
            aller_retour = 0

    arduino_liste = arduino_creation(arduino_liste)
    arduino_liste = arduino_deplacement(arduino_liste)
        
    virus_liste = virus_creation(virus_liste)
    virus_liste = virus_deplacement(virus_liste)

def draw():
    global grenouille_x, grenouille_y, vie, point, aceuille, bosse_x, bosse_y, taille, time, vie_bosse,point_bosse, bosse_up, bosse_batue, compteur, liste_vie, langue_longueur, langue_direction, langue_active, cible_
    compteur += 1
    mettre_a_jour_vies()
    if aceuille == 1 :
        if point_bosse >= 1000:
            time += 1
            pyxel.cls(0)
            pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
            if langue_active:
                pyxel.rect(grenouille_x + 7, 90-langue_longueur, 2, langue_longueur, 9)  
            pyxel.blt(grenouille_x, grenouille_y, 0, 0, 16, 16, 16, 0)
            appariton_des_vie()
            pyxel.blt(bosse_x, bosse_y, 0, 16, 0, 10, 9, 0, scale=taille)
            if bosse_up == 1:
                pyxel.blt(cible_x, cible_y, 0, 48, 0, 8, 8, 0)
                pyxel.rect(38, 10, 54, 9, 13)
                pyxel.text(5,2, 'calcul:'+ str(point), 13)
                pyxel.rect(40, 12,50-5*(100-vie_bosse)/10, 5, 8)
            if vie == 0:
                ecrant_mort()
            if vie_bosse == 0:
                initialisation_bosse()
        else:
            if vie>0:
                pyxel.cls(0)
                pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
                pyxel.text(5,2, 'calcul:'+ str(point), 7)
                if langue_active:
                    pyxel.rect(grenouille_x + 7, 90-langue_longueur, 2, langue_longueur, 9)

                pyxel.blt(grenouille_x, grenouille_y, 0, 0, 16, 16, 16, 0)

                for arduino in arduino_liste:
                    if arduino[2] == 1:
                        pyxel.blt(arduino[0], arduino[1], 0, 0, 32, 10, 8, 15)
                    else:
                        pyxel.blt(arduino[0], arduino[1], 0, 32, 0, 10, 8, 15)
            
                for virus in virus_liste:
                    pyxel.blt(virus[0], virus[1], 0, 16, 0, 10, 9, 0)

                appariton_des_vie()   
            else:
                ecrant_mort()
    else :
        ecrant_acceuille()
pyxel.run(update, draw)