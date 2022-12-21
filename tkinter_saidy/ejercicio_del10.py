import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

antenas_desde_el_input = []
años_desde_el_input = []


def guardar():
    print()


def grafica():
    datos = pd.read_csv('ant.csv', header=0)
    a = plt.plot(datos.Cesar, "r-o")
    b = plt.plot(datos.Huila, "b--")
    plt.title("Antenas creadas en departamentos durante 50 años")
    plt.xlabel("Años")
    plt.ylabel("Antenas")
    plt.legend(["Cesar", "Huila"])
    plt.grid()
    plt.show()


def ven2():
    v2 = tk.Toplevel()
    v2.geometry("600x600")
    # v2.iconbitmap("ant1.ico")
    v2.title("Datos")
    # imag = tk.PhotoImage(file="col.png")
    # label = tk.Label(v2, image=imag)
    # label.place(x=0, y=0)
    boton3 = tk.Button(v2, text="Todos", bg="pink", command=tdatos).place(
        x=20, y=10, width=250, height=50)
    boton4 = tk.Button(v2, text="Conocer primeros 16", bg="yellow",
                       command=datos1).place(x=20, y=100, width=250, height=50)
    boton5 = tk.Button(v2, text="Conocer antenas en la Guajira", bg="coral",
                       command=datos2).place(x=20, y=200, width=250, height=50)
    label5 = tk.Label(v2, text="Antena", bg="SlateBlue2")
    label5.place(x=20, y=300, width=100, height=30)
    txt2 = tk.Entry(v2, bg="bisque2")
    txt2.place(x=150, y=300, width=100, height=30)
    label7 = tk.Label(v2, text="Año", bg="SlateBlue2")
    label7.place(x=20, y=350, width=100, height=30)
    txt4 = tk.Entry(v2, bg="bisque2")
    txt4.place(x=150, y=350, width=100, height=30)

    def agregar_datos_al_vector():
        try:
            intValue = int(txt2.get())
            añoValue = int(txt4.get())
            antenas_desde_el_input.append(intValue)
            años_desde_el_input.append(añoValue)
            txt2.delete(0, 'end')
            txt2.insert(0, '')
            txt4.delete(0, 'end')
            txt4.insert(0, '')
        except:
            print("Eso no es un numero no se puede agregar")
    btn1 = tk.Button(v2, text="Agregar numero",
                     command=agregar_datos_al_vector)
    btn1.place(x=270, y=300, width=120, height=30)

    label6 = tk.Entry(v2, text="Resultado", bg="SlateBlue2")
    label6.place(x=270, y=350, width=100, height=30)

    def sumar_digitos():
        print("se ejecuto el metodo")
        suma = sum(antenas_desde_el_input)
        label6.delete(0, 'end')
        label6.insert(0, str(suma))

    btn2 = tk.Button(v2, text="Sumar",
                     command=sumar_digitos)
    btn2.place(x=20, y=400, width=120, height=30)

    def graficar_antenas_a():
        plt.plot(años_desde_el_input, antenas_desde_el_input)
        plt.title("Antenas creadas en departamentos durante 50 años")
        plt.xlabel("Años")
        plt.ylabel("Antenas")
        plt.grid()
        plt.show()

    btn3 = tk.Button(v2, text="Graficar",
                     command=graficar_antenas_a)
    btn3.place(x=150, y=400, width=120, height=30)
    # btn2 = tk.Button(v2, text="Sumar",
    #                  command=sumar_digitos)

    # label6 = tk.Label(ven, text="resultado en KM", bg="SlateBlue2")
    # label6.place(x=10, y=400, width=100, height=30)


def tdatos():
    datos = pd.read_csv('ant.csv', header=0)
    print(datos)


def datos1():
    datos = pd.read_csv('ant.csv', header=0)
    print(datos.iloc[0:16])


def datos2():
    datos = pd.read_csv('ant.csv', header=0)
    print(datos['La Guajira'])


def divi():
    n2 = txt2.get()
    r = float(n2)/300
    txt3.delete(0, 'end')
    txt3.insert(0, r)


ven = tk.Tk()
ven.geometry("430x450+0+0")
ven.title("ANTENAS")
ven.configure(bg="lightblue")
# ven.iconbitmap("ant1.ico")
# img = tk.PhotoImage(file="./antenas.png")
# foto = tk.Label(ven, image=img)
# foto.place(x=-50, y=0)
label = tk.Label(ven, text="Antenas de algunos departamentos de Colombia", bg="white", fg="black",
                 font="consolas 13 bold", relief=tk.GROOVE, bd=4, padx=10, pady=15)
label.pack(padx=10, pady=20)
frame1 = tk.LabelFrame(ven, text="Datos", bg="pink")
frame1.pack(fill=tk.X)
frame = tk.LabelFrame(ven, text="Grafica", bg="orange")
label = tk.Label(frame, text="Cesar", bg="red")
label.pack(padx=20, pady=20)
label.pack(side=tk.LEFT)
label1 = tk.Label(frame, text="Huila", bg="blue")
label1.pack(padx=20, pady=20)
label1.pack(side=tk.LEFT)
boton1 = tk.Button(frame, text="Mostrar", bg="pink", command=grafica)
boton1.pack(padx=20, pady=20)
boton2 = tk.Button(frame1, text="Conocer datos", command=ven2)
boton2.pack(pady=10)
frame.pack(fill=tk.X)
t = tk.Label(frame, text="Cesar", bg="red")
label5 = tk.Label(ven, text="frecuencia en Hz", bg="SlateBlue2")
label5.place(x=10, y=310, width=100, height=30)
txt2 = tk.Entry(ven, bg="bisque2")
txt2.place(x=120, y=310, width=100, height=30)
btn1 = tk.Button(ven, text="Distancia", command=divi)
btn1.place(x=230, y=310, width=80, height=30)
label6 = tk.Label(ven, text="resultado en KM", bg="SlateBlue2")
label6.place(x=10, y=400, width=100, height=30)
txt3 = tk.Entry(ven, bg="bisque2")
txt3.place(x=120, y=400, width=100, height=30)
ven.mainloop()
