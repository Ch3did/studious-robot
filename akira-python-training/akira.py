#-*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dat 

#Cria o Gráfico de casos
def grafico (a_infectados, data):
    df = pd.DataFrame({
    'Número de casos':a_infectados,
    'Semanas': data  
    })
    df.plot(kind='bar',x='Semanas',y='Número de casos')
    plt.show()

#Ajusta o dia seguinte para input no array
def calc_dat (mes, dia):
    o_dia  = dat.date(2020,mes,dia) + dat.timedelta(1)
    return(o_dia)

#Apresenta o programa
def apresentacao():
    print("Resultados de casos de corona dia a dia\n")
    print("O programa aceita um input de mês e dia e em seguida vai aceitando valores de número de casos,\n entendendo que cada novo input é um novo dia")
    print("Para finalizar o programa, aperte  0")
    print("------------------------------------------------------------")

#Arrays para criação da DF
a_infectados = []
a_data = []

#Chamando a apresentação
apresentacao()

#Contador do While
count1 = 1

#Contador de dias dentro do array
cont_days_array = 1

mes = int(input ("Me dê o mes da primeira entrada de análise: "))
dia = int(input("Me dê o dia da primera entrada de análise: "))
#Input do dia inicial
a_data.append(dat.date(2020,mes,dia))

#While para input dos valores dos arrays
while count1 == 1 :
    x = int(input("Me de Valor: ")) 
    if x > 0  :
        a_data.append(calc_dat(mes,dia))
        #Alteração dos dias para ajustes dentro da func calc_data
        data_do_while = a_data[cont_days_array]
        dia = data_do_while.day
        mes = data_do_while.month
        #Input dos numeros de infectados dendo do array 
        a_infectados.append(x)
        cont_days_array = cont_days_array+1
    else :
        #Quebra do while loop para criação da tabela 
        a_infectados.append(x)
        grafico(a_infectados , a_data)
        count1 = 0




