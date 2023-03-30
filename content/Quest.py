# Créé par dfialaire, le 27/09/2021 en Python 3.7
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:42:06 2022

@author: dfial
"""

def reponse1(reponse):
    reponse=str(reponse)
    if reponse == "09h16min52.88sec":
        return "C'est la bonne réponse. Bravo !"
    else:
        return "ce n'est pas cela. Réessayez..."
def reponse2(List_GGA,reponse):
    reponse=str(reponse)
    Long_List_GGA=len(List_GGA)

    Long_List_GGA=len(List_GGA)
    La=List_GGA[Long_List_GGA-1][2]
    Lon=List_GGA[Long_List_GGA-1][4]

    La=float(La)

    La_Deg=La/100
    La_Deg=round(La_Deg,2)

    Lon=float(Lon)

    Lon_Deg=Lon/100
    Lon_Deg=round(Lon_Deg,2)

    Entier_La_Deg=La_Deg-La_Deg%1
    Reste_La_Deg=round(La_Deg%1*100,1)
    Reste_La_Deg=int(Reste_La_Deg)
    Entier_La_Deg=int(Entier_La_Deg)

    Entier_Lon_Deg=Lon_Deg-Lon_Deg%1
    Reste_Lon_Deg=round(Lon_Deg%1*100,1)
    Reste_Lon_Deg=int(Reste_Lon_Deg)
    Entier_Lon_Deg=int(Entier_Lon_Deg)

    Entier_La_Deg=str(Entier_La_Deg)
    Latitude=Entier_La_Deg+"\N{DEGREE SIGN}"
    Reste_La_Deg=str(Reste_La_Deg)
    Latitude_minute=Reste_La_Deg+"'"

    Entier_Lon_Deg=str(Entier_Lon_Deg)
    Longitude=Entier_Lon_Deg+"\N{DEGREE SIGN}"
    Reste_Lon_Deg=str(Reste_Lon_Deg)
    Longitude_minute=Reste_Lon_Deg+"'"

    Var=str(Latitude)+str(Latitude_minute)+str(List_GGA[-1][3])+str(Longitude)+str(Longitude_minute)+str(List_GGA[-1][5])
    # print(Var)
    if reponse == Var:
        return "C'est la bonne réponse. Bravo !"
    else:
        return "ce n'est pas cela. Réessayez..."

