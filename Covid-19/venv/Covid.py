import pandas
import seaborn
import matplotlib.pyplot as plt
import numpy
import csv

data = pandas.read_csv('Covid-19.csv')

#Calculs pour avoir le nombre de Cas et de morts en France et dans le monde
casesWorld = pandas.DataFrame(data["cases"]).sum()
casesFrance = data.loc[data["countriesAndTerritories"]=="France"].cases.sum()
deathsWorld = pandas.DataFrame(data["deaths"]).sum()
deathsFrance = data.loc[data["countriesAndTerritories"]=="France"].deaths.sum()

#Affichage du camembert pour les cas de Covid en France et dans le monde
plt.figure(figsize = (8, 8))
x = [casesFrance,casesWorld-casesFrance]
plt.pie(x,
    labels=['France', 'Monde'],
    colors = ['#2d6f9a', '#0c4469'],
    labeldistance=1.1,
    autopct = lambda x: str(round(x, 2)) + '%',
    pctdistance = 0.5,
    explode=[0.2,0],
       )
plt.legend(
    title="Cas de Covid-19 en France et dans le monde en pourcentages",
    loc="upper right",
    bbox_to_anchor=(1.1,1.1),
    prop={'size': 10}
)
plt.show()

#Affichage du camembert pour les morts de Covid en France et dans le monde
plt.figure(figsize=(8, 8))
x = [deathsFrance, deathsWorld - deathsFrance]
plt.pie(x,
        labels=['France', 'Monde'],
        colors=['#2d6f9a', '#0c4469'],
        labeldistance=1.1,
        autopct=lambda x: str(round(x, 2)) + '%',
        pctdistance=0.5,
        explode=[0.2, 0],
        )
plt.legend(
    title="Morts du Covid-19 en France et dans le monde en pourcentages",
    loc="upper right",
    bbox_to_anchor=(1.1, 1.1),
    prop={'size': 10}
)
plt.show()

#Affichage des barres pour mieux faire la comparaison entre le monde et la France
y1 = [casesFrance,casesWorld]
y2 = [deathsFrance,deathsWorld]
Width = 0.4
r1 = range(len(y1))
r2 = [x + Width for x in r1]

plt.bar(r1, y1, width=Width, color=['#bd6b36' for i in y1])
plt.bar(r2, y2, width=Width, color=['#873703' for i in y1])
plt.xticks([r + Width / 2 for r in range(len(y1))], ['Cas France      Morts France', 'Cas Monde     Morts Monde'])
plt.title('Comparaison entre la France et le reste du monde')
plt.show()

#Calculs et affichage de l'évolution du Covid en France en prenant la date en index
France = data.loc[data["countriesAndTerritories"]=="France"]
#On met la date sous un format compréhensible par Phyton en créant une nouvelle colonne "date" qui est croissante
France['date'] = pandas.to_datetime(France[['year', 'month', 'day']], errors = 'coerce')
France[['date','deaths']].set_index('date').plot()
plt.title('Evolution de la mortalité du Covid-19 en France de Janvier au 11 Mai')
plt.show()

France[['date','cases']].set_index('date').plot()
plt.title('Evolution des cas du Covid-19 en France de Janvier au 11 Mai')
plt.show()

# Série de calculs pour avoir le nombre de cas et de morts par continent
AsiaDeaths = data.loc[data["continentExp"] == "Asia"].deaths.sum()
AsiaCases = data.loc[data["continentExp"] == "Asia"].cases.sum()

EuropeDeaths = data.loc[data["continentExp"] == "Europe"].deaths.sum()
EuropeCases = data.loc[data["continentExp"] == "Europe"].cases.sum()

AmericaDeaths = data.loc[data["continentExp"] == "America"].deaths.sum()
AmericaCases = data.loc[data["continentExp"] == "America"].cases.sum()

AfricaDeaths = data.loc[data["continentExp"] == "Africa"].deaths.sum()
AfricaCases = data.loc[data["continentExp"] == "Africa"].cases.sum()

OceaniaDeaths = data.loc[data["continentExp"] == "Oceania"].deaths.sum()
OceaniaCases = data.loc[data["continentExp"] == "Oceania"].cases.sum()

#Affichage de nos calculs précédents sous la forme de deux diagrammes
names = ['Asia', 'Europe', 'America', 'Africa','Oceania']
values = [AsiaCases, EuropeCases, AmericaCases, AfricaCases, OceaniaCases]
plt.bar(names, values,color = '#71c23c')
plt.title('Nombre de cas de Covid-19 par continents en écriture scientifique')
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(values,
        labels=['Asia', 'Europe', 'America', 'Africa','Oceania'],
        colors=['#e4e46c',  '#2e47ae' , '#7a043f', '#588553','#7b5f7b'],
        labeldistance=1.1,
        pctdistance=0.5,
        autopct = lambda x: str(round(x, 2)) + '%',
        )
plt.legend(
    title="Cas de Covid-19 par continents",
    loc="upper right",
    bbox_to_anchor=(1.1, 1.1),
    prop={'size': 10},
)
plt.title('Nombre de cas de Covid-19 par continents \n en pourcentages')
plt.show()

names = ['Asia', 'Europe', 'America', 'Africa','Oceania']
values = [AsiaDeaths, EuropeDeaths, AmericaDeaths, AfricaDeaths, OceaniaDeaths]
plt.bar(names, values,color = '#51892c')
plt.title('Nombre de morts du Covid-19 par continents')
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(values,
        labels=['Asia', 'Europe', 'America', 'Africa','Oceania'],
        colors=['#e4e46c',  '#2e47ae' , '#7a043f', '#588553','#7b5f7b'],
        labeldistance=1.1,
        pctdistance=0.5,
        autopct = lambda x: str(round(x, 2)) + '%',
        )
plt.legend(
    title="Morts lié au Covid-19 par continents",
    loc="upper right",
    bbox_to_anchor=(1.1, 1.1),
    prop={'size': 10}
)
plt.title('Nombre de morts de Covid-19 par \n continents en pourcentages')
plt.show()

#Calculs de la moyenne de cas et de morts dans plusieurs pays en fonction de sa population
PopFrance = data.loc[data["countriesAndTerritories"]=="France"].popData2018.mean()
CasesMeanFrance = casesFrance/PopFrance*1000
DeathsMeanFrance = deathsFrance/PopFrance*10000

PopItaly = data.loc[data["countriesAndTerritories"]=="Italy"].popData2018.mean()
CasesMeanItaly= data.loc[data["countriesAndTerritories"]=="Italy"].cases.sum()
DeathsMeanItaly= data.loc[data["countriesAndTerritories"]=="Italy"].deaths.sum()
CasesMeanItaly = CasesMeanItaly/PopItaly*1000
DeathsMeanItaly = DeathsMeanItaly/PopItaly*10000

PopBelgium = data.loc[data["countriesAndTerritories"]=="Belgium"].popData2018.mean()
CasesMeanBelgium= data.loc[data["countriesAndTerritories"]=="Belgium"].cases.sum()
DeathsMeanBelgium= data.loc[data["countriesAndTerritories"]=="Belgium"].deaths.sum()
CasesMeanBelgium = CasesMeanBelgium/PopBelgium*1000
DeathsMeanBelgium = DeathsMeanBelgium/PopBelgium*10000

PopAmerica = data.loc[data["countriesAndTerritories"]=="United_States_of_America"].popData2018.mean()
CasesMeanAmerica= data.loc[data["countriesAndTerritories"]=="United_States_of_America"].cases.sum()
DeathsMeanAmerica= data.loc[data["countriesAndTerritories"]=="United_States_of_America"].deaths.sum()
CasesMeanAmerica = CasesMeanAmerica/PopAmerica*1000
DeathsMeanAmerica = DeathsMeanAmerica/PopAmerica*10000

PopChina = data.loc[data["countriesAndTerritories"]=="China"].popData2018.mean()
CasesMeanChina= data.loc[data["countriesAndTerritories"]=="China"].cases.sum()
DeathsMeanChina= data.loc[data["countriesAndTerritories"]=="China"].deaths.sum()
CasesMeanChina = CasesMeanChina/PopChina*1000
DeathsMeanChina = DeathsMeanChina/PopChina*10000

PopEngland = data.loc[data["countriesAndTerritories"]=="United_Kingdom"].popData2018.mean()
CasesMeanEngland= data.loc[data["countriesAndTerritories"]=="United_Kingdom"].cases.sum()
DeathsMeanEngland= data.loc[data["countriesAndTerritories"]=="United_Kingdom"].deaths.sum()
CasesMeanEngland = CasesMeanEngland/PopEngland*1000
DeathsMeanEngland = DeathsMeanEngland/PopEngland*10000

PopGermany = data.loc[data["countriesAndTerritories"]=="Germany"].popData2018.mean()
CasesMeanGermany= data.loc[data["countriesAndTerritories"]=="Germany"].cases.sum()
DeathsMeanGermany= data.loc[data["countriesAndTerritories"]=="Germany"].deaths.sum()
CasesMeanGermany = CasesMeanGermany/PopGermany*1000
DeathsMeanGermany = DeathsMeanGermany/PopGermany*10000

PopSpain = data.loc[data["countriesAndTerritories"]=="Spain"].popData2018.mean()
CasesMeanSpain= data.loc[data["countriesAndTerritories"]=="Spain"].cases.sum()
DeathsMeanSpain= data.loc[data["countriesAndTerritories"]=="Spain"].deaths.sum()
CasesMeanSpain = CasesMeanSpain/PopSpain*1000
DeathsMeanSpain = DeathsMeanSpain/PopSpain*10000

#Affichage
names = ['France', 'Italy', 'Belgium', 'America','China', 'England', 'Germany', 'Spain']
values = [CasesMeanFrance, CasesMeanItaly, CasesMeanBelgium, CasesMeanAmerica, CasesMeanChina, CasesMeanEngland, CasesMeanGermany, CasesMeanSpain]
plt.bar(names, values, color = '#e11355')
plt.title('Moyenne de cas de Covid-19 par pays pour 1000 habitants')
plt.show()

names = ['France', 'Italy', 'Belgium', 'America','China', 'England', 'Germany', 'Spain']
values = [DeathsMeanFrance, DeathsMeanItaly, DeathsMeanBelgium, DeathsMeanAmerica, DeathsMeanChina, DeathsMeanEngland, DeathsMeanGermany, DeathsMeanSpain]
plt.bar(names, values, color = '#6c256d')
plt.title('Moyenne de morts du Covid-19 par pays pour 10 000 habitants')
plt.show()

print("Cas de Covid-19 an France au 11 Mai:",casesFrance)
print("Cas de Covid-19 dans le monde au 11 Mai:",casesWorld)
print("Morts liés au Covid-19 an France au 11 Mai:",deathsFrance)
print("Morts liés au Covid-19 dans le monde au 11 Mai:",deathsWorld)