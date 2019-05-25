# Aptoide - Python Challenge

## Autocomplete API

You are asked to implement an Autocomplete API that helps users searching for apps by
their name. When writing the name of an app, the possible results should be shown to
the user. For example, if the user is inputting *Fac*, two possible choices are
*Facebook* and *Facebook Lite*.

The challenge is composed of 2 main components:

* The autocomplete system
* An API (a microservice/web service) that receives a query and returns the possible
results for that query

The autocomplete system can be seen as a composition of 2 subcomponents:

* A data structure to store the possible words (the corpus). This data structure
should enable quick lookups of words.
* A search algorithm that given the above data structure and a query, should
output the possible words

The microservice/web service should be simple enough as to just receive as input a
user query, ask the autocomplete system for the possible results and send them back.

## Requisites

You will need to have python3, python-pip, docker and docker-compose on your machine to run


## How to run

To run the webservices execute
```
FILE="<csv input file>" HOST="<host IP>" docker-compose up

```

To run on host 0.0.0.0 with the test_files/190titles.csv input file run:
```
FILE="test_files/190titles.csv" HOST="0.0.0.0" docker-compose up

```

or thrugh docker if you do not have docker-compose with:
```
docker build -t autocomplete-aptoid .
docker run -p 8080:8080 autocomplete-aptoid -i test_files/190titles.csv -H 0.0.0.0
```



## How to make an API request

With the webservice running on a different console run

```
curl -d "Fac" -X POST http://0.0.0.0:8080/autocomplete
```

## How to run the tests
```
python test_trie.py
python test_search.py
```

