import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import missingno as msno
import sklearn
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
from sklearn.linear_model import Lasso, ElasticNet
from sklearn.preprocessing import MinMaxScaler, RobustScaler, PolynomialFeatures, StandardScaler,  Binarizer
from sklearn.pipeline import make_pipeline
import pickle
import streamlit as st

pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

df = pd.read_csv("immobilier2.csv")

qualiter_construction_maison = st.selectbox("qualiter de la construction de base", (1,2,3,4,5,6,7,8,9,10,11,12,13))
etats_maison = st.selectbox("états de la maison", (1,2,3,4,5))
annee_construction = st.slider("année de construction", 1900, 2015)

if st.checkbox("cocher la case si la maison a était rénover") :
    annee_renovation = st.slider("année de rénovation", 1900, 2015)
else :
    annee_renovation = annee_construction

vue_sur_mer = st.radio("a t'il une vue sur étendu d'eau", ("oui", "non"))

if vue_sur_mer == "oui" :
    vue_sur_mer = 1
else :
    vue_sur_mer = 0

vue_sur_proprieter = st.selectbox("vue sur la propriété", (0,1,2,3,4))
surface_maison = st.number_input("indiquez la surface de la maison en mètre carré", min_value=0, max_value=1500)
surface_terrain = st.number_input("indiquez la surface du terrain en mètre carré", min_value=200, max_value=15000)
surface_grenier = st.number_input("indiquez la surface du grenier", min_value=30, max_value=900)

if st.checkbox("cocher la case si vous avez une cave") :
    surface_cave = st.number_input("indiquez la surface de la cave", min_value=30, max_value=500)
else :
    surface_cave = 0

nb_salle_de_bain = st.slider("nombre de salle de bains", 0.0, 10.0, step=0.25)
nb_etage = st.slider("nombre d'étages", 1.0, 4.0, step=0.25)
nb_chambre = st.slider("nombre de chambres", 1, 35)
zipcode = st.selectbox("code postal", ('98001', '98002', '98003', '98004',
       '98005', '98006', '98007', '98008', '98010', '98011', '98014', '98019',
       '98022', '98023', '98024', '98027', '98028', '98029', '98030', '98031',
       '98032', '98033', '98034', '98038', '98039', '98040', '98042', '98045',
       '98052', '98053', '98055', '98056', '98058', '98059', '98065', '98070',
       '98072', '98074', '98075', '98077', '98092', '98102', '98103', '98105',
       '98106', '98107', '98108', '98109', '98112', '98115', '98116', '98117',
       '98118', '98119', '98122', '98125', '98126', '98133', '98136', '98144',
       '98146', '98148', '98155', '98166', '98168', '98177', '98178', '98188',
       '98198', '98199'))
       
code = ('98001', '98002', '98003', '98004',
       '98005', '98006', '98007', '98008', '98010', '98011', '98014', '98019',
       '98022', '98023', '98024', '98027', '98028', '98029', '98030', '98031',
       '98032', '98033', '98034', '98038', '98039', '98040', '98042', '98045',
       '98052', '98053', '98055', '98056', '98058', '98059', '98065', '98070',
       '98072', '98074', '98075', '98077', '98092', '98102', '98103', '98105',
       '98106', '98107', '98108', '98109', '98112', '98115', '98116', '98117',
       '98118', '98119', '98122', '98125', '98126', '98133', '98136', '98144',
       '98146', '98148', '98155', '98166', '98168', '98177', '98178', '98188',
       '98198', '98199')

if st.checkbox("cocher la case si vous connaisser pas l'atitude et la longitude"):
    adresse = st.text_input("adresse")
else : 
    latitude = st.slider("latitude", 0.0, 50.0)
    longitude = st.slider("longitude", 0.0, 50.0)

test = [qualiter_construction_maison, etats_maison, annee_construction, annee_renovation, vue_sur_mer, vue_sur_proprieter, surface_maison, surface_terrain, surface_grenier, surface_cave, nb_salle_de_bain, nb_etage, nb_chambre, latitude, longitude]
if st.button("estimation") :
    for cp in code :
        if cp == zipcode:
            test.append(1)
        else:
            test.append(0)
    st.write(test)
    prediction_prix = model.predict([test])
    st.success(prediction_prix)