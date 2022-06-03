
#Taller 
#Gariela Torres
#ID:1001970935
#ID:502193
#correo:gabriela.torresr@correo.upb.edu.co
#Cel:3234708201
#Diplomado de PYTHON APLICADO A LA INGENIERIA 
#Docente:Roberto Paez Salgado
#Modulo 2


import pandas as pd
import numpy as np

DataU = pd.read_excel("DataU.xlsx")

# EJERCICIO 1

imc = (DataU["peso"]/(DataU["altura"])**2).round(0)
DataU["imc"] = imc
print(DataU)

# EJERCICIO 2

capital_final = (DataU["dinero a invertir"]*((DataU["interes anual"]/(100 + 1))**DataU["anos de inversion"])).round(5)
DataU["Capital final"] = capital_final

print("El capital Final es:\n",)
print(capital_final)

#EJERCICIO  3

condition_list = [
     (DataU["hora de comprar el pan despues de horneado"] <= 6),
     (DataU["hora de comprar el pan despues de horneado"] <= 12 ),
     (DataU["hora de comprar el pan despues de horneado"] <= 18 ),
     (DataU["hora de comprar el pan despues de horneado"] <= 24 )
]
choice_list = [10,20,30,40]
DataU["porcentaje de descuento"] = np.select(condition_list,choice_list,default="no especificado")

#EJERCICIO 4

condition_list_for_extension = [
    (DataU["sexo"] == "M"),
    (DataU["sexo"] == "F" )
]
choice_list_for_extension = [DataU["telefono"] + "-11",DataU["telefono"] + "-10"]
DataU["numero de extension"] = np.select(condition_list_for_extension,choice_list_for_extension,default="no especificado")

print(DataU)