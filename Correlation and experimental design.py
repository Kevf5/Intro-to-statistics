# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:36:46 2023

@author: Equipo
"""

import seaborn as sns
import numpy as np
import pandas as pd
#%%
'SCATTER PLOT'
sleep_total = np.random.randint(4,10,size =100)
sleep_rem = np.random.randint(4,10, size=100)
msleep = pd.DataFrame({'total': sleep_total, 'rem': sleep_rem})
print(msleep)

sns.scatterplot( x = 'total', y='rem', data = msleep)
sns.lmplot( x = 'total', y='rem', data = msleep, ci=None) #se agrega una linea de tendencia
#el arg ci none to no haya interv de confia alr de la linea

'COEF CORRELATION'
msleep['total'].corr( msleep['rem'] )
#Pearson product moment correlation (r) : Sum [(xi - xraya)(yi - yraya)]/(desvx . desvy)

#otras versiones de correlacion:
    #tau de Kendall
    #rho de Spearman
#%%
'                   ADVERTENCIAS S/LA CORRELACION'
#non linear rel 0.18 de corr

#sesgo -> transformaacion de registro
bodywt = [60]*20 + [65]*25 + [70]*20 + [73]*10 + [75]*5 + [78]*5 + [80]*3 + [82]*3 + [85]*2 +[87]*2 +[89]*2+[90*1]
print(bodywt)
sns.histplot(bodywt)
#bodywt contiene un sesgo hacia los pesos ligeros
bodywt_trans = np.log(bodywt)
sns.histplot(bodywt_trans)
#este cambio de registro podria dar otra vista de la rel netre 2 variables

'funcion log'
x = range(-100,101)
y = np.log(x)
sns.scatterplot(x,y) #amplia la diferencia

'Other transformations: dep de los dt y de cuan sesgados estan -> lograr rel lineal'
#sqrt(x)
#reciprocal trans: 1/x
#s/x o y

'lograr una rel lineal pueden ser nec para realizar cierto metodos estadisticos '
#%%
'                                  Diseño de experimentos'
'Standars de oro'
#ensayo controlado aleatorio: aseg gr sean comparables
#Placebo: usar algo parecido al tratam/solucion real pero no tiene efec, los partic no sabran en q gr estan
#asegurar que el efecto sea real 
#Double-blind trial (exper doble ciego): persona q adm el trat/corre el estudio tampoco sabe si estan adm
#el TRATAMIENTO REAL O PLACEBO, protege contra sesgo de respuesta y de analisis de resultados
'-> Menos oportunidades para sesgos = mas conclusiones confiables sobre la causalidad (trat afecta la resp)'

'Estudio observacional'
#part no asign aleat a los gr, se asigan ellos mismos en f de carac preexist
#util para responder preg q no conducen a un exp controlado
    #si desea estudiar el efecto de fumar s/el cancer no puede obligarlos a fumar
    #caracteristica no controlada, existe un grupo en el universo, distinguible pero no controlable en su reproductibilidad y en la profundidad en q se puede conocer cada participante
    #ni obligar a ciertos comportamiento de consumo para conocer los efectos de este comport 
#ASIGNACION NO ALEATORIA: no forma de gar q los grupos seran comparables en todo aspecto
#NO ESTABLECEN CAUSALIDAD, SOLO ASOCIACION: cuales son las caracteristicas inciales q llevan a conformar nu grupo?
    #los efect pueden ser confund con los factores q llevaron a alg al gr de control y alg al gr de trat
    #hay formas de controlar los factores de confusion para ayudar a fortal la confiabil de las conclusiones acerca de la asoc

'Estudios longitudinale y transversales'
#1ro: se los sigue un per de t para examinar el efecto de trat en la resp 
#2do: dt recopilados en una unica instantanea en el t 
#%%
print('nueva linea')




















