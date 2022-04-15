# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 20:57:44 2022

@author: Rosalina Winda Pratiwi
"""
from tkinter import Tk, Label, IntVar, Button, Entry
window = Tk()
window.title("Perkalian 2 Buah Matrik")
window.geometry("400x400+120+120")
window.configure(bg='#49A')
window.resizable(False, False)

#make matiks A
text_var = []
entries = []
temp_mat = []
def get_mat():
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(text_var[i][j].get())

    print(matrix)
    matrixB = []
    for i in range(rows_B):
        matrixB.append([])
        for j in range(cols_B):
            matrixB[i].append(text_varB[i][j].get())
    print(matrixB)
    temp_row = []

    temp_sum = 0
 
    for i in range(0, row_matriks(matrix)):
        for j in range(0, col_matriks(matrixB)):
            for k in range(0, row_matriks(matrixB)):
                temp_sum += matrix[i][k] * matrixB[k][j]
            
            temp_row.append(temp_sum)
            temp_sum = 0
        temp_mat.append(temp_row)
        temp_row = []
    print(temp_mat)
    ##print matriks hasil 
    Label(window, text="Hasil Perkalian Matrik A dan B :", font=('arial', 10, 'bold'), 
      bg='#0059b3').place(x=20, y=210)
    Label(window, text=temp_mat, font=('arial', 10, 'bold'), 
      bg='white').place(x=20, y=240)
      
def col_matriks(matriks):
    return len(matriks[0])
 
def row_matriks(matriks):
    return len(matriks) 

Label(window, text="Matrik A :", font=('arial', 10, 'bold'), 
      bg="#0059b3").place(x=20, y=20)

x2 = 0
y2 = 0
rows, cols = (3,4)
for i in range(rows):
    # append an empty list to your two arrays
    # so you can append to those later
    text_var.append([])
    entries.append([])
    for j in range(cols):
        # append your IntVar and Entry
        text_var[i].append(IntVar())
        entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))
        entries[i][j].place(x=20 + x2, y=50 + y2)
        x2 += 30
    y2 += 30
    x2 = 0    
#make matriks B
Label(window, text="Matrik B :", font=('arial', 10, 'bold'), 
      bg="#0059b3").place(x=200, y=20)

text_varB = []
entriesB = []
x3 = 0
y3 = 0
rows_B, cols_B = (4,5)
for k in range(rows_B):
    # append an empty list to your two arrays
    # so you can append to those later
    text_varB.append([])
    entriesB.append([])
    for l in range(cols_B):
        # append your IntVar and Entry
        text_varB[k].append(IntVar())
        entriesB[k].append(Entry(window, textvariable=text_varB[k][l],width=3))
        entriesB[k][l].place(x=200 + x3, y=50 + y3)
        x3 += 30

    y3 += 30
    x3 = 0    
button= Button(window,text="Hitung", bg='#0059b3', width=15, command=get_mat)
button.place(x=200,y=300)

window.mainloop()