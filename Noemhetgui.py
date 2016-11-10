from tkinter import *
from Test import *
root = Tk()
invoer = ""

def toonVenster():
    def close():
        subwindow.withdraw()

    subwindow = Toplevel(master=root)
    button2 = Button(master=subwindow, text='Sluit mij', command=close)
    button2.pack(padx=10, pady=10)


#hier moet je functie patrick
def toonVenster4():
    def close():
        subwindow.withdraw()

    subwindow = Toplevel(master=root)
    labelVertrektijden = Label(master=subwindow, text=vertrektijdenUtrecht(), justify=LEFT, width='150')
    button6 = Button(master=subwindow, text='Andere station', command=toonVenster5)
    button6.pack(side=RIGHT)
    labelVertrektijden.pack(padx=100, pady=100)


def toonVenster5():
    def close():
        subwindow.withdraw()
    def opvragentijden():
        text1.delete(1.0, END)
        verzoek = entry.get()
        data = stationsnamen(verzoek)
        text1.insert(1.0, data)

    subwindow = Toplevel(master=root)
    labelVertrektijden = Label(master=subwindow, text='Voer uw station in')

    entry = Entry(master=subwindow, textvariable=invoer)

    button5 = Button(master=subwindow, text='OK', command=opvragentijden)

    text1 = Text(master=subwindow, background = 'white')

    labelVertrektijden.grid()
    entry.grid(row=0, column= 1)
    button5.grid(row=0, column=2)
    text1.grid(row=1, columnspan = 3)


label = Label(master=root,text='Welkom bij de NS')
label.pack()

button1 = Button(master=root, text="Kopen los kaartje", command=toonVenster)
button1.pack(side=LEFT)
button2 = Button(master=root, text="Kopen OV-Chipkaart", command=toonVenster)
button2.pack(side=LEFT)
button3 = Button(master=root, text="Ik wil naar het buitenland", command=toonVenster)
button3.pack(side=LEFT)
button4 = Button(master=root, text="Actuele vertrektijden", command=toonVenster4)
button4.pack(side=LEFT)
root.mainloop()
