from tkinter import *
import random
import time

colors = {"sehat": "blue","sick": "red", "recovered": "green", "dead": "black"}#Dictonary Status dengan warna
class Ball():#HUMAN
    def __init__(self, canvas, ball, color):
        self.canvas = canvas
        self.ball = ball
        self.turnSick = 0
        self.status = color
        starts = list(range(0, 60))
        random.shuffle(starts)
        self.num = starts[0]
        self.id = canvas.create_oval(10, 10,18, 18, fill = self.status)
        self.canvas.move(self.id, random.randint(0, 800), random.randint(0,450))
        self.x = random.randint(-1, 1)# gerak objek dan posisinya bukan tkinter dan dapat juga pada modul lain turtel pygame
        self.y = random.randint(-1, 1)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.recoveryTime = random.randint(2, 10)
        self.deadTime = random.randint(5, 10)

    def update(self):# Klo sakit orang ada tindakan selanjutnya (method)
        if self.status == colors["sick"]:
            if self.turnSick == self.recoveryTime:
                self.status = colors["recovered"]
                self.canvas.itemconfig(self.id, fill=self.status)
            if self.turnSick == self.deadTime:
                self.status = colors["dead"]
                self.canvas.itemconfig(self.id, fill=self.status)
                self.x = 0
                self.y = 0
    def ball0(self, pos):# ini adalah apabila manusia berinteraksi dan setelahnya memantul atau pergi
        paddle_pos = self.canvas.coords(self.ball[self.num].id)
        if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False

    def ball1(self, pos):
        paddle_pos = self.canvas.coords(self.ball[self.num].id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def ball2(self, pos):#fungsi ini di lepar ke method draw
        paddle_pos = self.canvas.coords(self.ball[self.num].id)
        if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] <= paddle_pos[2] and pos[0] >= paddle_pos[0]:
                return True
            return False

    def ball3(self, pos):
        paddle_pos = self.canvas.coords(self.ball[self.num].id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[1] >= paddle_pos[3] and pos[1] <= paddle_pos[1]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.turnSick += 1
            if self.turnSick == 1:
                self.status = colors["sick"]
                self.canvas.itemconfig(self.id, fill=self.status)
            self.update()
            self.y = random.randint(1,4)
        if pos[3] >= self.canvas_height:
            self.turnSick += 1
            if self.turnSick == 1:
                self.status = colors["sick"]
                self.canvas.itemconfig(self.id, fill=self.status)
            self.update()
            self.y = random.randint(-4,-1)
        if self.ball0(pos) == True:
            self.turnSick += 1
            if self.turnSick == 1:
                self.status = colors["sick"]
                self.canvas.itemconfig(self.id, fill=self.status)
            self.update()
            self.x = 2
        if self.ball1(pos) == True:
            self.turnSick += 1
            if self.turnSick == 1:
                self.status = colors["sick"]
                self.canvas.itemconfig(self.id, fill=self.status)
            self.update()
            self.y = -2 #updatenya akan terpilih sendiri dan memilih dari method update
        if self.ball2(pos) == True:
            self.turnSick += 1
            if self.turnSick == 1:
                self.status = colors["sick"]
                self.canvas.itemconfig(self.id, fill=self.status)
            self.update()
            self.x = -2
        if self.ball3(pos) == True:
            self.turnSick += 1
            if self.turnSick == 1:
                self.status = colors["sick"]
                self.canvas.itemconfig(self.id, fill=self.status)
            self.update()
            self.y = 2
        if pos[0] <= 0:
            self.turnSick += 1
            if self.turnSick == 1:
                self.status = colors["sick"]
                self.canvas.itemconfig(self.id, fill=self.status)
            self.update()
            self.x = random.randint(1,4)
        if pos[2] >= self.canvas_width:
            self.turnSick += 1
            if self.turnSick == 1:
                self.status = colors["sick"]
                self.canvas.itemconfig(self.id, fill=self.status)
            self.update()
            self.x = random.randint(-4,-1)


root = Tk()
root.title("Simulation Covid-19")
root.geometry("800x500")
my_menu = Menu(root)
root.config(menu = my_menu)
canvas = Canvas(root, width = 780, height = 460, highlightthickness = 0)
canvas.grid(column = 0,  columnspan = 3, row = 1)

#command
def our_command():
    i = 0
    i += 1
    if i == 1:
        canvas.delete('all')
    root.resizable(0, 0)
    root.wm_attributes("-topmost", 1)

    root.update()

    ball = []
    for x in range(100):# karena tidak praktikal/efisien membuat syntax untuk 100 bola makan dilakukan looping
        ball.append(Ball(canvas, ball, "blue"))


    while 1:
        for x in range(100):
            ball[x].draw()
        root.update_idletasks()
        root.update()
        time.sleep(0.02)

def delete():
    canvas.delete('all')

def design():
    buttons_frame = LabelFrame(root, text="Change Color Background")
    buttons_frame.grid(column=0, row=0)

    curRad1 = Radiobutton(buttons_frame, text="Blue :"+"sehat")
    curRad1.grid(column=0, row=0, sticky=W)
    curRad2 = Radiobutton(buttons_frame, text="Red :"+"sakit")
    curRad2.grid(column=1, row=0, sticky=W)
    curRad3 = Radiobutton(buttons_frame, text="Green :"+"sembuh")
    curRad3.grid(column=2, row=0, sticky=W)
    curRad4 = Radiobutton(buttons_frame, text="Black :"+ "meninggal")
    curRad4.grid(column=3, row=0, sticky=W)

    for child in buttons_frame.winfo_children():
        child.grid_configure(padx=6, pady=5)

    action = Button(root, width = 25, height = 3, text = "Start", command = our_command) #command yang memanggil fugsi agar terjadi perlkuan dari yang sudah code
    action.grid(column=1, row=0)
    action2 = Button(root, width = 25, height = 3, text = "Finish",command = delete) #Finish code memanggil fungsi delet
    action2.grid(column=2, row=0)
design()


root.mainloop()