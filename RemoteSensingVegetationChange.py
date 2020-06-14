# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:33:07 2019

@author: Nurullah
"""

from tkinter import *
top = Tk()
top.geometry('800x400')
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
matplotlib.use("TkAgg")

def calculate_vegetation():
    r1 = img.imread(label1.cget("text"))
    nir1 = img.imread(label2.cget("text"))
    r2 = img.imread(label3.cget("text"))
    nir2 = img.imread(label4.cget("text"))
    
    R1 = np.asarray( r1, dtype="int32" )
    NIR1 = np.asarray( nir1, dtype="int32" )
    ndvi1=(NIR1-R1)/(NIR1+R1)
    q1=(ndvi1 > 0.50)
    b1=np.count_nonzero(q1)
    oran1=(b1/q1.size)*100
    plt.figure().suptitle("Eski görüntü")
    plt.imshow(q1, cmap='gray', vmin=0, vmax=1)
    
    R2 = np.asarray(r2, dtype="int32" )
    NIR2 = np.asarray(nir2, dtype="int32" )
    ndvi2=(NIR2-R2)/(NIR2+R2)
    q2=(ndvi2 > 0.50)
    b2=np.count_nonzero(q2)
    oran2=(b2/q2.size)*100
    plt.figure().suptitle("Yeni görüntü")
    plt.imshow(q2, cmap='gray', vmin=0, vmax=1)

    
    oran= "Eski yeşillik oranı = % " + str(oran1) + "     Yeni yeşillik oranı = % " + str(oran2)
    fark="Zamana göre değişim farkı = % " + str(oran2-oran1)
    label5.config(text=oran)
    label6.config(text=fark)
    
    

def browse_red1():

    Tk().withdraw() 
    filename = askopenfilename()
    label1.config(text=filename)

def browse_nir1():
    
    Tk().withdraw() 
    filename = askopenfilename()
    label2.config(text=filename)

def browse_red2():

    Tk().withdraw() 
    filename = askopenfilename()
    label3.config(text=filename)

def browse_nir2():
    
    Tk().withdraw() 
    filename = askopenfilename()
    label4.config(text=filename)

düğme1 = Button(text='Eski RED Band', command=browse_red1)
düğme2 = Button(text='Eski NIR Band', command=browse_nir1)
label1 = Label( text="")
label2 = Label( text="")
label3 = Label( text="")
label4 = Label( text="")
düğme3 = Button(text='Yeni RED Band', command=browse_red2)
düğme4 = Button(text='Yeni NIR Band', command=browse_nir2)
düğme6 = Button(text='Yeşillik Değişimi Hesapla', command=calculate_vegetation)
label5 = Label( text="")
label6 = Label( text="")



düğme1.grid(column=1,row=1,padx=15, pady=15)
düğme2.grid(column=1,row=2,padx=15, pady=15)
label1.grid(column=2,row=1,padx=15, pady=15)
label2.grid(column=2,row=2,padx=15, pady=15)


düğme3.grid(column=1,row=3,padx=15, pady=15)
düğme4.grid(column=1,row=4,padx=15, pady=15)

düğme6.grid(column=1,row=5,padx=15, pady=15)

label3.grid(column=2,row=3,padx=15, pady=15)
label4.grid(column=2,row=4,padx=15, pady=15)

label5.grid(column=2,row=5,padx=15, pady=15)
label6.grid(column=2,row=6,padx=15, pady=15)


top.mainloop()