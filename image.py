# Créé par lcolbert, le 25/01/2024 en Python 3.7
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import random

from PIL import Image
import random

def meilleur() :
    changer_ciel()
    bleu = 0
    bleu2 = 0
    image1 = Image.open("maNouvelleImage.png")	# L’image se situe dans le même répertoire
    L, H = image1.size

    for y in range(H):
        for x in range(L):
            if (x*y)%10000 == 0:           # Compteur de pixels
                print(x*y)
            pixel = image1.getpixel((x,y))
            r = pixel[0]
            v = pixel[1]
            b = pixel[2]
            if (b > 150 and r < 200 and v<=200) or (b > 180 and r < 200 and v>=200):
                bleu += 1
    changer_ciel_colonne()
    image1 = Image.open("maNouvelleImage.png")	# L’image se situe dans le même répertoire

    for y in range(H):
        for x in range(L):
            if (x*y)%10000 == 0:           # Compteur de pixels
                print(x*y)
            pixel = image1.getpixel((x,y))
            r = pixel[0]
            v = pixel[1]
            b = pixel[2]
            if (b > 150 and r < 200 and v<=200) or (b > 180 and r < 200 and v>=200):
                bleu2 += 1
    difference = bleu2 - bleu
    print (difference, bleu, bleu2)

    if difference >= 200 :
        changer_ciel()
    else :
        changer_ciel_colonne()
def inverse () :
    image1 = Image.open(explorateur_de_fichier)	# L’image se situe dans le même répertoire
    L, H = image1.size
    image2 = Image.new("RGB",(L,H))
    for y in range(H):
        for x in range(L):
            if (x*y)%10000 == 0:           # Compteur de pixels
                print(x*y)
            pixel = image1.getpixel((x,y))
            r = pixel[0]
            v = pixel[1]
            b = pixel[2]
            r, v, b= v , b, r
            image2.putpixel((x,y),(r,v,b))
    image2.save("maNouvelleImage.png")
    afficher_final()



def supprRouge () :
    image1 = Image.open(explorateur_de_fichier)	# L’image se situe dans le même répertoire
    L, H = image1.size
    image2 = Image.new("RGB",(L,H))
    for y in range(H):
        for x in range(L):
            if (x*y)%10000 == 0:           # Compteur de pixels
                print(x*y)
            pixel = image1.getpixel((x,y))
            r = pixel[0]
            v = pixel[1]
            b = pixel[2]
            if ( r > 100 and b < 75 and v<75) :
                r=0
                v=0
                b=0

            image2.putpixel((x,y),(r,v,b))

    image2.save("maNouvelleImage.png")
    afficher_final()


def aleatoire() :
    image1 = Image.open(explorateur_de_fichier)	# L’image se situe dans le même répertoire
    L, H = image1.size
    image2 = Image.new("RGB",(L,H))

    for y in range(H):

        for x in range(L):
            X2 = random.randint(0,L-1)
            Y2 = random.randint(0,H-1)
            if (x*y)%10000 == 0:           # Compteur de pixels
                print(X2,Y2)
            pixel = image1.getpixel((x,y))
            r = pixel[0]
            v = pixel[1]
            b = pixel[2]
            image2.putpixel((X2,Y2),(r,v,b))
    image2.save("maNouvelleImage.png")
    afficher_final()






def changer_ciel() :
    image1 = Image.open(explorateur_de_fichier)	# L’image se situe dans le même répertoire
    L, H = image1.size
    cosmos = Image.open("cosmos2(1).jpg")
    #cosmos = cosmos.resize((L,H))
    L2, H2 = cosmos.size
    stop = False
    image2 = Image.new("RGB",(L,H))

    for y in range(H):
        pas_de_ciel = 0
        for x in range(L):
            xprime = x
            if (x*y)%10000 == 0:           # Compteur de pixels
                print(x*y)
            pixel = image1.getpixel((x,y))



            r = pixel[0]
            v = pixel[1]
            b = pixel[2]



            verif1 = (b > 150 and r < 200 and v<=200) or (b > 180 and r < 200 and v>=200)


            if  ((verif1 ) and not(stop))  :

                        pixelCosmos = cosmos.getpixel((x,y))

                        r=pixelCosmos[0]+50
                        v=pixelCosmos[1]+50
                        b=pixelCosmos[2]+50

            else :
                pas_de_ciel += 1
            if pas_de_ciel >= L-10 :
                stop = True
                break
            image2.putpixel((x,y),(r-50,v-50,b-50))

    image2.save("maNouvelleImage.png")
    afficher_final()








def changer_ciel_colonne() :
    image1 = Image.open(explorateur_de_fichier)	# L’image se situe dans le même répertoire
    L, H = image1.size
    cosmos = Image.open("cosmos2(1).jpg")
    #cosmos = cosmos.resize((L,H))
    L2, H2 = cosmos.size
    stop = False
    image2 = Image.new("RGB",(L,H))

    for x in range(L):
        pas_de_ciel = 0
        stop = False
        for y in range(H):
            if (x*y)%10000 == 0:           # Compteur de pixels
                print(x*y)
            pixel = image1.getpixel((x,y))



            r = pixel[0]
            v = pixel[1]
            b = pixel[2]



            verif1 = (b > 150 and r < 200 and v<=200) or (b > 180 and r < 200 and v>=200)


            if  ((verif1 ) and not(stop))  :

                        pixelCosmos = cosmos.getpixel((x,y))

                        r=pixelCosmos[0]+50
                        v=pixelCosmos[1]+50
                        b=pixelCosmos[2]+50

            else :
                pas_de_ciel += 1
            if pas_de_ciel >= 60 :
                stop = True

            image2.putpixel((x,y),(r-50,v-50,b-50))

    image2.save("maNouvelleImage.png")
    afficher_final()




def modifier_image(fonction):
    if explorateur_de_fichier:  # Vérifie que la fonction explorateur_de_fichier a été exécuté
        image = Image.open(explorateur_de_fichier)  # Ouvre l'image avec PIL
        fonction(image)
        afficher_final()

def afficher_image(img):
    print(img)
    image = Image.open(img)  # Ouvre l'image avec PIL
    image.thumbnail((800, 800))  # Mettre l'image avec une taille de 800*800
    photo = ImageTk.PhotoImage(image)  # Mettre l'image PIL en image tkinter qui pourra être affiché avec l'interface
    label_image.config(image=photo)
    label_image.image = photo  # Mettre l'image affiché est photo ( donc l'image tkinter)

def afficher_final():
    print("coucou")
    image = Image.open("maNouvelleImage.png")  # Ouvre l'image avec PIL
    image.thumbnail((800, 800))  # Mettre l'image avec une taille de 800*800
    photo = ImageTk.PhotoImage(image)  # Mettre l'image PIL en image tkinter qui pourra être affiché avec l'interface
    label_image.config(image=photo)
    label_image.image = photo  # Mettre l'image affiché est photo ( donc l'image tkinter)
def fichier():
    global explorateur_de_fichier
    explorateur_de_fichier = filedialog.askopenfilename(initialdir="/", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("All files", "*.*")])  # Ouvre l'explorateur de fichier où l'on peut selectionné un fichier image
    if explorateur_de_fichier:  # Vérifie si un fichier a été sélectionné
        afficher_image(explorateur_de_fichier)  # Fait la fonction afficher_image
    else :
        explorateur_de_fichier = "ATTENTION AUCUN FICHIER N'EST OUVERT" # Initialisation de explorateur_de_fichier

    label_file_explorer.configure(text="Fichier ouvert: " + explorateur_de_fichier)  # Permet de savoir le fichier ouvert


def image_d_origine() :
    global explorateur_de_fichier
    if explorateur_de_fichier: # vérifie que explorateur_de_fichier a été exécuté
        afficher_image(explorateur_de_fichier)  # affiche l'image qui



fen = Tk()
fen.title("MODIFICATIONS D'IMAGE")
fen.geometry("1080x720")

label_file_explorer = Label(fen, text="Aucun fichier ouvert", width=100, height=4, fg="blue")
label_file_explorer.pack()

menu = Menu()
a = Menu(menu, tearoff=0)
b = Menu(menu, tearoff=0)

x = Menu(menu, tearoff=0)

a.add_command(label="Choisir une image", command=fichier)
a.add_command(label="Restaurer l'image d'origine", command=image_d_origine)
menu.add_cascade(label="Fichiers", menu=a)


b.add_command(label="Changer le ciel", command=changer_ciel)
b.add_command(label="Changer le ciel avec traitement en colonne", command=changer_ciel_colonne)
b.add_command(label="Choisir la meilleure option de changement de ciel pour l'image", command=meilleur)


#x.add_command(label="Jour", command=changer_ciel)
#x.add_command(label="Nuit", command=changer_ciel)

b.add_command(label="Inverser les couleurs", command=inverse)
b.add_command(label="Supprimer le Rouge", command=supprRouge)
b.add_command(label="Aléatoire", command=aleatoire)
menu.add_cascade(label="Modifications de l'image", menu=b)

fen.config(menu=menu)

label_image = Label(fen)
label_image.pack()

explorateur_de_fichier = "ATTENTION AUCUN FICHIER N'EST OUVERT" # Initialisation de explorateur_de_fichier

fen.mainloop() # Permet d'afficher l'interface