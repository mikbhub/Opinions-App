# TODO:
*local jquery
# final project
Django apps to collect, process and dispatch customer feedback / opinions.

## REST api to collect opinions from different sources:
- simple form (pluggalble to company website)
- social media (api and web scrapping)
- formularz wysyjący na api używając ajax
- rest api na serwerze
- django signals
### database schema:
- model customer
    * id
    * email
    * name
    * surname
- model feedback
    * opinion text
    * customer (by id or email)
    * source
## worker that uses ms/ibm/google apis to analyse feedback text and compute metrics (sentiment, ...)
- ms azure sentiment
## dispatcher to organise customer care to optimise business metrics (minimize the impact of ragining customers)
- python priority queue

# MVP
#### Formularz wysyłający opinię na api.
#### Api przyjmuje, zapisuje do bazy danych, analizuje, oblicza metryki i nadaje pozycję w kolejce zadań dla customer supportu.
### TODO:  
- formularz wysyjący dane na server
- requests użyte do odpytania MS azure o sentyment
- jakiś worker / job / signal który odputuje api metryk (ms azure) o sentyment
- frontend pokazujący kolejkę, z możliwością wzięcia kolejnego zadania, 
    * oraz statystkyki:
        * podział opini na neutralne / pozytywne / negatywne
