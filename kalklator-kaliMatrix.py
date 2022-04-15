# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:55:44 2022

@author: Rosalina Winda Pratiwi
"""

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
             
label_m1 = Label(window, font=("Times New Roman", 10), text="Input Ukuran Matrik 1")            
label_m1.grid(row=0, column=3, sticky="nesw")

label_row1 = Label(window, font=("Times New Roman", 10), text="row ")            
label_row1.grid(row=1, column=0, sticky="nesw")
input_row1 = Entry(window, font=("Times New Roman", 10))
input_row1.grid(row=1, column=2, sticky="news" )

label_col1 = Label(window, font=("Times New Roman", 10), text="column")            
label_col1.grid(row=2, column=0, sticky="nesw")
input_col1 = Entry(window, font=("Times New Roman", 10))
input_col1.grid(row=2, column=2, sticky="news" )

             
label_m2 = Label(window, font=("Times New Roman", 10), text="Input Ukuran Matrik 2")            
label_m2.grid(row=4, column=3, sticky="nesw")

label_row2 = Label(window, font=("Times New Roman", 10), text="row")            
label_row2.grid(row=5, column=0, sticky="nesw")
input_row2 = Entry(window, font=("Times New Roman", 10))
input_row2.grid(row=5, column=2, sticky="news" )

label_col2 = Label(window, font=("Times New Roman", 10), text="column")            
label_col2.grid(row=6, column=0, sticky="nesw")
input_col2 = Entry(window, font=("Times New Roman", 10))
input_col2.grid(row=6, column=2, sticky="news" )
def bentuk_matrix():
   window1 = Tk()
   window1.title("Perkalian 2 Buah Matrik")
   window1.geometry("400x400+120+120")
   window1.configure(bg='#49A')
   window1.resizable(False, False)

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
       Label(window1, text="Hasil Perkalian Matrik A dan B :", font=('arial', 10, 'bold'), 
         bg='#0059b3').place(x=20, y=210)
       Label(window1, text=temp_mat, font=('arial', 10, 'bold'), 
         bg='white').place(x=20, y=240)
         
   def col_matriks(matriks):
       return len(matriks[0])
    
   def row_matriks(matriks):
       return len(matriks) 

   Label(window1, text="Matrik A :", font=('arial', 10, 'bold'), 
         bg="#0059b3").place(x=20, y=20)

   x2 = 0
   y2 = 0
   rows, cols = (int(input_row1.get()),int(input_col1.get()))
   for i in range(rows):
       # append an empty list to your two arrays
       # so you can append to those later
       text_var.append([])
       entries.append([])
       for j in range(cols):
           # append your IntVar and Entry
           text_var[i].append(IntVar())
           entries[i].append(Entry(window1, textvariable=text_var[i][j],width=3))
           entries[i][j].place(x=20 + x2, y=50 + y2)
           x2 += 30
       y2 += 30
       x2 = 0    
   #make matriks B
   Label(window1, text="Matrik B :", font=('arial', 10, 'bold'), 
         bg="#0059b3").place(x=200, y=20)

   text_varB = []
   entriesB = []
   x3 = 0
   y3 = 0
   rows_B, cols_B = (int(input_row2.get()),int(input_col2.get()))
   for k in range(rows_B):
       # append an empty list to your two arrays
       # so you can append to those later
       text_varB.append([])
       entriesB.append([])
       for l in range(cols_B):
           # append your IntVar and Entry
           text_varB[k].append(IntVar())
           entriesB[k].append(Entry(window1, textvariable=text_varB[k][l],width=3))
           entriesB[k][l].place(x=200 + x3, y=50 + y3)
           x3 += 30

       y3 += 30
       x3 = 0    
   button= Button(window1,text="Hitung", bg='#0059b3', width=15, command=get_mat)
   button.place(x=200,y=300)     
   
                   
buttonBentukMatrix= Button(window, text="Submit", font=("Times New Roman", 10), command=bentuk_matrix)
buttonBentukMatrix.grid(row=9, column=3, sticky="nesw")
              
window.mainloop()