#import bibliotek
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

# wyświetlenie zawartości katalogu opinions_json
input_direcory = './opinions_json'
print(*os.listdir(input_direcory))

# wczytywanie identyfikatora produktu, którego opinie będą analizowane
product_id = input('Podaj id produktu: ')

# wczytywanie do ramki danyh opinii o pojedyńczym produkcie
opinions = pd.read_json(input_direcory+'/'+product_id+'.json')
opinions = opinions.set_index('opinion_id')

# podstawowe statystyki
#average_score= round(opinions.stars.mean(),2)
average_score = opinions.stars.mean().round(2)
pros = opinions.pros.count()
cons = opinions.cons.count()
print(
    f'Średnia ocena: {average_score}\nLiczba opinii z zaletami: {pros}\nLiczba opinii z wadami: {cons}\n')
recommendation = opinions.recommendation.value_counts()

# histogarm częstości wystepowania poszczególnych ocen (gwiazdek)
stars = opinions.stars.value_counts().sort_index().reindex(
    list(np.arange(0, 5.5, 0.5)), fill_value=0)
fig, ax = plt.subplots()
stars.plot.bar(color=('#f5c3c2'))
stars.plot.bar()
plt.title('Gwiazdki')
plt.xlabel('Ocena')
plt.ylabel('Liczba Ocen')
plt.xticks(rotation=0)
plt.savefig('figures_png/'+product_id+'bar.png')
plt.close()

# udział poszczególnych rekomendacji w ogólnej liczbie opinii
recommendation = opinions.recommendation.value_counts()
fig, ax = plt.subplots()
recommendation.plot.pie(label='', autopct='%1.1f%%',
                        colors=['#89cff0', '#f5c3c2'])
plt.title('Rekomendacja')
plt.savefig('app/static/figures_png/'+product_id+'pie.png')
plt.close()

opinions['purchased'] = opinions['purchase_date'].apply(
    lambda x: False if x == None else True)
stars_purchased = pd.crosstab(opinions['stars'], opinions['purchased'])
print(stars_purchased)
