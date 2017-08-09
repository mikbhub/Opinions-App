# Opinions App:

*Django apps to collect, process and dispatch customer feedback / opinions*

[Live demo on PythonAnywhere](http://mikolajbabiak.pythonanywhere.com/dispatch_to_support/dashboard/)

## Features

### REST api endpoint accepting  opinions from different sources:
- simple form (pluggalble to company website)
- social media (api and web scrapping) (TODO)

### Text analytics
* computing text metrics:
    * sentiment using `NLTK`

### Dispatcher to organise customer care to optimise business metrics (minimize the impact of dissatisfied and angry customers)
- `PriorityQueue` that prioritizes opinions by text analitics metrics (most negative go first).
- User interface for customer support.