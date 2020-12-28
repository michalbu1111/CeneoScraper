# CeneoScraper
## Etap 1 - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl)

|Składowa                |Selektor                                        |Nazwa zmiennej|
|------------------------|------------------------------------------------|--------------|
|opinia                  |li.js_product-review                            |opinion       |
|identyfikator opinii    |["data-entry-id"]                               |opinion_id    |
|autor                   |div.reviewer-name-line                          |author        |
|rekomendacja            |div.product-review-summary > em                 |recommendation|
|ocena                   |span.review-score-count                         |stars         |
|treść opinii            |p.product-review-body                           |content       |
|lista wad               |div.cons-cell > ul                              |cons          |
|lista zalet             |div.pros-cell > ul                              |pros          |
|przydatna               |button.vote-yes > span                          |useful        |
|nieprzydatna            |button.vote-no > span                           |useless       |
|data wystawienia opinii |span.review-time > time:first-child["datetime"] |opinion_date  |
|data zakupu             |span.review-time > time:nth-child(2)["datetime"]|purchase_date |
## Etap 2 - pobranie składowych pojedynczej opinii
- pobranie kodu jednej strony z opiniani o konkretnym produkcie
- wyciągnięcie a kodu strony fragmentów odpowiadających poszczególnym opiniom
- zapisanie do pojedynczych zmienych wartości poszczególnych składowych opinii
## Etap 3 - pobranie wszystkich opinii o pojedyńczym produkcie
- zapisanie do złożonej struktury danych składowych wszystkich opinii z pojedyńczej strony
- przechodzenie po kolejnych stronach z opiniami
- zapis wszystkich opinii o pojedyńczym produkcie do pliku
## Etap 4
- transformacja i wyczyszczenie danych
- refakoring kodu
- parametryzacja 
## Etap 5 (Pandas, Matplotlib)
- wczytywanie opinii od ramki danych
- poiczenie podstawoych statystyk
- narysowanie wykresów funkcji
## Etap 6 interfejs dla scrapera (Flask)
>    /CeneoScraper  
>>        /run.py  
>>        /config.py  
>>        /app  
>>>            /__init__.py
>>>            /views.py  
>>>            /models.py
>>>            /forms.py
>>>            /scraper.py
>>>            /analizer.py  
>>>            /static/  
>>>>                /main.css
>>>>                /figures_png
>>>            /templates/  
>>>>                /layout.html  
>>>>                /extract.html
>>>>                /about.html
>>>             /opinions_json
>>>        /requirements.txt  
>>>        /.venv