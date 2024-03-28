from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox as mb
import time
from PIL import Image, ImageTk


root = Tk()  

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("600x470+%d+%d" % (x-200, y-200))  
root.title("CAT")  


bg = Image.open("home.png")
bg_resized = bg.resize((500, 400), Image.LANCZOS)

icon = PhotoImage(file="iconCat.png") 
root.iconphoto(False, icon) 


cat_image = Image.open("cat.png")
cat_width, cat_height = 150, 150  


cat_image_resized = cat_image.resize((cat_width, cat_height), Image.BILINEAR)


bg_resized.paste(cat_image_resized, (300, 250), cat_image_resized)  


bg_image = ImageTk.PhotoImage(bg_resized)


lbl_bk = Label(root, image=bg_image)
lbl_bk.pack(fill='none', expand=False)  


healthCat = 20
leisureCat = 20


def update_clock():

    global healthCat  # працюємо з глобальними аргументами
    global leisureCat
    ''' функція, яка відповідає за оновлення ігрової ситуації раз на секунду '''
    now = time.strftime("%H:%M:%S")
    
    if 97 > healthCat >=2 or 97 > leisureCat >=2 : 
        root.after(1000, heppimin)
        root.after(1000, update_clock)
    
    elif healthCat == 0 or leisureCat == 0:
        lost()
   
    elif healthCat >= 97 and leisureCat >= 97:
        win_game()
            

def lost():
    
    global healthCat  # працюємо з глобальними аргументами
    global leisureCat  # працюємо з глобальними аргументами
    
    if  healthCat == 0 or leisureCat ==0:
        healthCat = 0
        leisureCat = 0
        l1.configure(text="health - " + str(healthCat) + "%")  # змінюємо налаштування текстової мітки "здоров'я,", приводимо до стрінги та "надсилаємо" до розділу розташування віджетів 
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        answer = mb.askyesno(title="You lost", message="You lost. Do you want to play again?")
        
        if answer == True:
            healthCat = 53
            leisureCat = 53
            root.after(1000, update_clock)
        
        else:
            root.quit()


def win_game():
    global healthCat  # працюємо з глобальними аргументами
    global leisureCat
            
    if healthCat >= 95 or leisureCat >= 95:
        answer2 = mb.askyesno(title="You win", message="You win!!! Do you want to play again?")
        
        if answer2 == True:
            healthCat = 53
            leisureCat = 53
            root.after(1000, update_clock)
        
        else:
            root.quit()
    

def heppimin():

    global healthCat  # працюємо з глобальними аргументами
    global leisureCat  
    
    if 97 >= healthCat >= 3 and 97 >= leisureCat >= 3 or 97 >= healthCat >= 3 and 97 < leisureCat or 97 < healthCat  and 97 >= leisureCat >= 3:
        healthCat = healthCat - 3  # кожної ітерації параметр "здоров'я," зменшується на 3
        leisureCat = leisureCat - 3  # кожної ітерації параметр "задоволення" зменшується на 3
        l1.configure(text="health - " + str(healthCat) + "%")  # змінюємо налаштування текстової мітки "здоров'я,", приводимо до стрінги та "надсилаємо" до розділу розташування віджетів 
        l2.configure(text="leisure - " + str(leisureCat) + "%")  # змінюємо налаштування текстової мітки "задоволення"
    
    elif healthCat <= 2 or leisureCat <= 2:
        healthCat = 0
        leisureCat = 0
        l1.configure(text="health - " + str(healthCat) + "%")  # змінюємо налаштування текстової мітки "здоров'я,", приводимо до стрінги та "надсилаємо" до розділу розташування віджетів 
        l2.configure(text="leisure - " + str(leisureCat) + "%")


def health():
    global healthCat
    global leisureCat
    
    if  3 < healthCat <= 90 and leisureCat !=3:
        healthCat = healthCat + 10
        leisureCat = leisureCat - 2
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
        l3.configure(text="your cat is health")
        
        if leisureCat <= 10:
            mb.showerror("Sorry", "Your cat is sad")
            leisureCat = leisureCat + 20
        
    elif healthCat > 90:
        healthCat = 100
        leisureCat = leisureCat - 2
        l1.configure(text="health - " + str(healthCat) + "%")
        l2.configure(text="leisure - " + str(leisureCat) + "%")
    
    elif healthCat <= 2 or leisureCat <= 2:
        healthCat = 0
        leisureCat = 0
        l1.configure(text="health - " + str(healthCat) + "%")  # змінюємо налаштування текстової мітки "здоров'я,", приводимо до стрінги та "надсилаємо" до розділу розташування віджетів 
        l2.configure(text="leisure - " + str(leisureCat) + "%")
    

def leisure():
        global healthCat
        global leisureCat
        if 3 <  leisureCat <= 90 and healthCat !=3:
            healthCat = healthCat - 2
            leisureCat = leisureCat + 10
            l1.configure(text="health - " + str(healthCat) + "%")
            l2.configure(text="leisure - " + str(leisureCat) + "%")
            l3.configure(text="your cat is laisure")
            
            if healthCat <= 10:
                mb.showerror("Sorry", "Your cat is ill")
                healthCat = healthCat + 20
        
        elif leisureCat > 90:
            leisureCat = 100
            healthCat = healthCat - 2
            l1.configure(text="health - " + str(healthCat) + "%")
            l2.configure(text="leisure - " + str(leisureCat) + "%")
        
        elif healthCat <= 2 or leisureCat <= 2:
            healthCat = 0
            leisureCat = 0
            l1.configure(text="health - " + str(healthCat) + "%")  # змінюємо налаштування текстової мітки "здоров'я,", приводимо до стрінги та "надсилаємо" до розділу розташування віджетів 
            l2.configure(text="leisure - " + str(leisureCat) + "%")


label2 = Label(width=20, height=1, text="It is your Cat", font="Verdana", borderwidth=2, relief="solid")
b1 = ttk.Button(width=15, text="Feed", command=health)
b2 = ttk.Button(width=15, text="Caress", command=leisure)
b3 = ttk.Button(width=15, text="Train", command=health)
b4 = ttk.Button(width=15, text="Play", command=leisure)
b5 = ttk.Button(width=18, text="Exit", command=root.quit)
l1 = Label(width=20, height=2, text="HEALTH - " + str(healthCat) + "%", font=("Verdana", 10), borderwidth=2, relief="solid")
l2 = Label(width=20, height=2, text="LEISURE - " + str(leisureCat) + "%", font=("Verdana", 10), borderwidth=2, relief="solid")
l3 = Label(width=20, height=2, text="your cat is alive", font=("Verdana", 10), borderwidth=2, relief="solid")

label2.place(relx=0.4, rely=0.05, anchor="center")
b1.place(relx=0.12, rely=0.4, anchor="center")
b2.place(relx=0.12, rely=0.46, anchor="center")
b3.place(relx=0.12, rely=0.52, anchor="center")
b4.place(relx=0.12, rely=0.58, anchor="center")
b5.place(relx=0.7, rely=0.96, anchor="center")
l1.place(relx=0.15, rely=0.2, anchor="center")
l2.place(relx=0.15, rely=0.32, anchor="center")
l3.place(relx=0.7, rely=0.88, anchor="center")

root.after(1000, update_clock)  

root.mainloop()

