from tkinter import*
import tkinter.messagebox as tmsg
from conversion import*
global fbg_color
fbg_color = "skyblue"
def click(event):
    global scavlue
    text=event.widget.cget("text")
    if text == "=":
        if scavlue.get().isdigit():
            value = int(scavlue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
        scavlue.set(value)
        screen.update()
    elif text == "C":
        scavlue.set("")
        screen.update()

    else:
        scavlue.set(scavlue.get()+text)
        screen.update()

def darkbg():
    global fbg_color
    root.configure(background="black")
    fbg_color = "skyblue"

def lightbg():
    root.configure(background="white")

def custombg():
    global fbg_color
    root.configure(background="lightgreen")
    fbg_color = color_bg.set("seashell2")

root=Tk()
root.geometry("320x340+150+150")
root.resizable(0,0)
root.title("F@yyu's Calculator")
#root.wm_iconbitmap("Guillendesign-Variations-3-Calculator.ico")
#photo = PhotoImage(file = "Guillendesign-Variations-3-Calculator.ico")
#root.iconphoto(False, photo)
root.configure(background="lightgreen")

def length():
    global conversion_screen
    conversion_screen = Toplevel(root)
    conversion_screen.title("Length Conversion")
    conversion_screen.geometry("520x130+150+150")
    conversion_screen.resizable(0,0)

    cv = Length()
    var = IntVar()
    def convert():
        if var.get() == 0:
            tmsg.showwarning("No selection","Please Select any conversion")
        elif var.get() == 1:
            cm = cv.intocm(Input.get())
            Output.set(cm)

        elif var.get() == 2:
            inch = cv.cmtoin(Input.get())
            Output.set(inch)
                
        elif var.get() == 3:
            ft = cv.fttomtr(Input.get())
            Output.set(ft)
            
        elif var.get() == 4:
            mtr = cv.mtrtoft(Input.get())
            Output.set(mtr)
            
        elif var.get() == 5:
            yd = cv.ydtom(Input.get())
            Output.set(yd)
            
        elif var.get() == 6:
            yard = cv.mtoyard(Input.get())
            Output.set(yard)

        elif var.get() == 7:
            km = cv.miletokm(Input.get())
            Output.set(km)

        elif var.get() == 8:
            mile = cv.kmtomile(Input.get())
            Output.set(mile)
            
        elif var.get() == 9:
            m = cv.nmiletom(Input.get())
            Output.set(m) 

        elif var.get() == 10:
            nmile = cv.mtonmile(Input.get())
            Output.set(nmile)
            


    radio = Radiobutton(conversion_screen,text="in to cm",padx=14,variable=var,value=1).grid(row=0,column=0)
    radio = Radiobutton(conversion_screen,text="cm to in",padx=14,variable=var,value=2).grid(row=1,column=0)
    radio = Radiobutton(conversion_screen,text="ft to m",padx=14,variable=var,value=3).grid(row=0,column=1)
    radio = Radiobutton(conversion_screen,text="m to ft",padx=14,variable=var,value=4).grid(row=1,column=1)
    radio = Radiobutton(conversion_screen,text="yd to m",padx=14,variable=var,value=5).grid(row=0,column=2)
    radio = Radiobutton(conversion_screen,text="m to yd",padx=14,variable=var,value=6).grid(row=1,column=2)
    radio = Radiobutton(conversion_screen,text="mile to km",padx=14,variable=var,value=7).grid(row=0,column=3)
    radio = Radiobutton(conversion_screen,text="km to mile",padx=14,variable=var,value=8).grid(row=1,column=3)
    radio = Radiobutton(conversion_screen,text="nmile to m",padx=14,variable=var,value=9).grid(row=0,column=4)
    radio = Radiobutton(conversion_screen,text="m to nmile",padx=14,variable=var,value=10).grid(row=1,column=4)

    Input = IntVar()
    Output = IntVar()
    e1 = Entry(conversion_screen,textvariable=Input,width=35)
    e1.grid(row=2,column=1,columnspan=3)

    Label(conversion_screen,textvariable=Output).grid(row=3,column=1,columnspan=3)


    b1 = Button(conversion_screen,text="convert",background="skyblue",borderwidth=4,relief=RAISED,command=convert)
    b1.grid(row=4,column=2)

def area():
    global area_conversion
    area_conversion = Toplevel(root)
    area_conversion.title("Area Conversion")
    area_conversion.geometry("250x100+150+150")
    area_conversion.resizable(0,0)
    
    cv = Area()
    var = IntVar()

    def Convert_area():
        if var.get() == 0:
            tmsg.showwarning("No selection","Please Select any conversion")
        elif var.get() == 1:
            msq = cv.acretomsq(Input.get())
            Output.set(msq)

        elif var.get() == 2:
            acre = cv.msqtoacre(Input.get())
            Output.set(acre)
                
    radio = Radiobutton(area_conversion,text="acre to m-sq",padx=14,variable=var,value=1).grid(row=0,column=0)
    radio = Radiobutton(area_conversion,text="m-sq to acre",padx=14,variable=var,value=2).grid(row=0,column=1)

    Input = IntVar()
    Output = IntVar()
    e1 = Entry(area_conversion,textvariable=Input,width=35)
    e1.grid(row=1,column=0,columnspan=2)

    Label(area_conversion,textvariable=Output).grid(row=2,column=0,columnspan=2)


    b1 = Button(area_conversion,text="convert",background="skyblue",borderwidth=4,relief=RAISED,command=Convert_area)
    b1.grid(row=3,column=0,columnspan=2)


def volume():
    global volume_conversion
    volume_conversion = Toplevel(root)
    volume_conversion.title("Volume Conversion")
    volume_conversion.geometry("250x130+150+150")
    volume_conversion.resizable(0,0)
    cv = Volume()
    var = IntVar()

    def Convert_volume():
        if var.get() == 0:
            tmsg.showwarning("No selection","Please Select any conversion")

        elif var.get() == 1:
            galus = cv.galustoltr(Input.get())
            Output.set(galus)

        elif var.get() == 2:
            ltrus = cv.ltrustogal(Input.get())
            Output.set(ltrus)

        elif var.get() == 3:
            galuk = cv.galuktoltr(Input.get())
            Output.set(galuk)
            
        elif var.get() == 4:
            ltruk = cv.ltruktogal(Input.get())
            Output.set(ltruk)
                        
    radio = Radiobutton(volume_conversion,text="gal(US) to ltr",padx=14,variable=var,value=1).grid(row=0,column=0)
    radio = Radiobutton(volume_conversion,text="ltr to (US)gal",padx=14,variable=var,value=2).grid(row=1,column=0)
    radio = Radiobutton(volume_conversion,text="gal(UK) to ltr",padx=14,variable=var,value=3).grid(row=0,column=1)
    radio = Radiobutton(volume_conversion,text="ltr to (UK)gal",padx=14,variable=var,value=4).grid(row=1,column=1)

    Input = IntVar()
    Output = IntVar()
    e1 = Entry(volume_conversion,textvariable=Input,width=35)
    e1.grid(row=2,column=0,columnspan=2)

    Label(volume_conversion,textvariable=Output).grid(row=3,column=0,columnspan=2)


    b1 = Button(volume_conversion,text="convert",background="skyblue",borderwidth=4,relief=RAISED,command=Convert_volume)
    b1.grid(row=4,column=0,columnspan=2)



def mass():
    global mass_conversion
    mass_conversion = Toplevel(root)
    mass_conversion.title("Mass Conversion")
    mass_conversion.geometry("220x130+150+150")
    mass_conversion.resizable(0,0)

    cv = Mass()
    var = IntVar()

    def Convert_mass():
        if var.get() == 0:
            tmsg.showwarning("No selection","Please Select any conversion")

        elif var.get() == 1:
            g = cv.oztog(Input.get())
            Output.set(g)

        elif var.get() == 2:
            oz = cv.gtooz(Input.get())
            Output.set(oz)

        elif var.get() == 3:
            kg = cv.lbtokg(Input.get())
            Output.set(kg)
            
        elif var.get() == 4:
            lb = cv.kgtolb(Input.get())
            Output.set(lb)
                        
    radio = Radiobutton(mass_conversion,text="oz to gram",padx=14,variable=var,value=1).grid(row=0,column=0)
    radio = Radiobutton(mass_conversion,text="gram to oz",padx=14,variable=var,value=2).grid(row=1,column=0)
    radio = Radiobutton(mass_conversion,text="lb to kg",padx=14,variable=var,value=3).grid(row=0,column=1)
    radio = Radiobutton(mass_conversion,text="kg to lb",padx=14,variable=var,value=4).grid(row=1,column=1)

    Input = IntVar()
    Output = IntVar()
    e1 = Entry(mass_conversion,textvariable=Input,width=35)
    e1.grid(row=2,column=0,columnspan=2)

    Label(mass_conversion,textvariable=Output).grid(row=3,column=0,columnspan=2)


    b1 = Button(mass_conversion,text="convert",background="skyblue",borderwidth=4,relief=RAISED,command=Convert_mass)
    b1.grid(row=4,column=0,columnspan=2)


def velocity():
    global velocity_conversion
    velocity_conversion = Toplevel(root)
    velocity_conversion.title("Velocity Conversion")
    velocity_conversion.geometry("250x100+150+150")
    velocity_conversion.resizable(0,0)
    
    cv = Velocity()
    var = IntVar()

    def Convert_velocity():
        if var.get() == 0:
            tmsg.showwarning("No selection","Please Select any conversion")
        elif var.get() == 1:
            ms = cv.kmperhtompers(Input.get())
            Output.set(ms)

        elif var.get() == 2:
            km = cv.mpersectokmperh(Input.get())
            Output.set(km)
                
    radio = Radiobutton(velocity_conversion,text="km/h to m/s",padx=14,variable=var,value=1).grid(row=0,column=0)
    radio = Radiobutton(velocity_conversion,text="m/s to km/h",padx=14,variable=var,value=2).grid(row=0,column=1)

    Input = IntVar()
    Output = IntVar()
    e1 = Entry(velocity_conversion,textvariable=Input,width=35)
    e1.grid(row=1,column=0,columnspan=2)

    Label(velocity_conversion,textvariable=Output).grid(row=2,column=0,columnspan=2)


    b1 = Button(velocity_conversion,text="convert",background="skyblue",borderwidth=4,relief=RAISED,command=Convert_velocity)
    b1.grid(row=3,column=0,columnspan=2)


def power():
    global power_conversion
    power_conversion = Toplevel(root)
    power_conversion.title("Power Conversion")
    power_conversion.geometry("250x100+150+150")
    power_conversion.resizable(0,0)
    cv = Power()
    var = IntVar()

    def Convert_power():
        if var.get() == 0:
            tmsg.showwarning("No selection","Please Select any conversion")
        elif var.get() == 1:
            kw = cv.hptokw(Input.get())
            Output.set(kw)

        elif var.get() == 2:
            hp = cv.kwtohp(Input.get())
            Output.set(hp)
                
    radio = Radiobutton(power_conversion,text="hp to kw",padx=14,variable=var,value=1).grid(row=0,column=0)
    radio = Radiobutton(power_conversion,text="kw to hp",padx=14,variable=var,value=2).grid(row=0,column=1)

    Input = IntVar()
    Output = IntVar()
    e1 = Entry(power_conversion,textvariable=Input,width=35)
    e1.grid(row=1,column=0,columnspan=2)

    Label(power_conversion,textvariable=Output).grid(row=2,column=0,columnspan=2)


    b1 = Button(power_conversion,text="convert",background="skyblue",borderwidth=4,relief=RAISED,command=Convert_power)
    b1.grid(row=3,column=0,columnspan=2)



def pressure():
    global pressure_conversion
    pressure_conversion = Toplevel(root)
    pressure_conversion.title("Pressure Conversion")
    pressure_conversion.geometry("520x130+150+150")
    pressure_conversion.resizable(0,0)
    cv = Pressure()
    var = IntVar()

    def Convert_pressure():
        if var.get() == 0:
            tmsg.showwarning("No selection","Please Select any conversion")
        elif var.get() == 1:
            pa = cv.atmtopa(Input.get())
            Output.set(pa)

        elif var.get() == 2:
            atm = cv.patoatm(Input.get())
            Output.set(atm)

        elif var.get() == 3:
            pas = cv.mmofhgtopa(Input.get())
            Output.set(pas)
            
        elif var.get() == 4:
            hg = cv.patommofhg(Input.get())
            Output.set(hg)
            
        elif var.get() == 5:
            pascal = cv.kgftopa(Input.get())
            Output.set(pascal)
            
        elif var.get() == 6:
            kgf = cv.patokgf(Input.get())
            Output.set(kgf)

        elif var.get() == 7:
            kpa = cv.lbftokpa(Input.get())
            Output.set(kpa)

        elif var.get() == 8:
            lbf = cv.kpatolbf(Input.get())
            Output.set(lbf)
            
                  
    radio = Radiobutton(pressure_conversion,text="atm to Pa",padx=14,variable=var,value=1).grid(row=0,column=0)
    radio = Radiobutton(pressure_conversion,text="Pa to atm",padx=14,variable=var,value=2).grid(row=1,column=0)
    radio = Radiobutton(pressure_conversion,text="mmHg to Pa",padx=14,variable=var,value=3).grid(row=0,column=1)
    radio = Radiobutton(pressure_conversion,text="Pa to mmHg",padx=14,variable=var,value=4).grid(row=1,column=1)
    radio = Radiobutton(pressure_conversion,text="kgf/cm2 to pa",padx=14,variable=var,value=5).grid(row=0,column=2)
    radio = Radiobutton(pressure_conversion,text="pa to kgf/cm2",padx=14,variable=var,value=6).grid(row=1,column=2)
    radio = Radiobutton(pressure_conversion,text="lbf/in2 to kpa",padx=14,variable=var,value=7).grid(row=0,column=3)
    radio = Radiobutton(pressure_conversion,text="kpa to lbf/in2",padx=14,variable=var,value=8).grid(row=1,column=3)

    Input = IntVar()
    Output = IntVar()
    e1 = Entry(pressure_conversion,textvariable=Input,width=35)
    e1.grid(row=2,column=1,columnspan=2)

    Label(pressure_conversion,textvariable=Output).grid(row=3,column=1,columnspan=2)


    b1 = Button(pressure_conversion,text="convert",background="skyblue",borderwidth=4,relief=RAISED,command=Convert_pressure)
    b1.grid(row=4,column=1,columnspan=2)




mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="Dark",command=darkbg)
m1.add_command(label="Light",command=lightbg)
m1.add_command(label="custom",command=custombg)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="Length",command=length)
m2.add_command(label="Area",command=area)
m2.add_command(label="Volume",command=volume)
m2.add_command(label="Mass",command=mass)
m2.add_command(label="Velocity",command=velocity)
m2.add_command(label="Power",command=power)
m2.add_command(label="Pressure",command=pressure)
root.config(menu=mainmenu)


mainmenu.add_cascade(label="Theme",menu=m1)
mainmenu.add_cascade(label="Conversion",menu=m2)
color_bg = StringVar()
scavlue = StringVar()
scavlue.set("")



screen = Entry(root,textvariable=scavlue,font="lucid 20")
screen.pack(fill=X,padx=5)

f=Frame(root,bg=fbg_color)
b = Button(f,text="9",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text="8",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text="7",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text="C",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg=fbg_color)
b = Button(f,text="6",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

b = Button(f,text="5",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


b = Button(f,text="4",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


b = Button(f,text="+",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg=fbg_color)
b = Button(f,text="3",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


b = Button(f,text="2",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


b = Button(f,text="1",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


b = Button(f,text="-",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg=fbg_color)
b = Button(f,text="0",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


b = Button(f,text=".",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


b = Button(f,text="/",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


b = Button(f,text="*",font="lucid 20",width=4)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg=fbg_color)
b = Button(f,text="=",font="lucid 20",width=8)
b.pack(side=LEFT,padx=2,pady=2)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()
