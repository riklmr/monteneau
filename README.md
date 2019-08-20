# monteneau
Harvest river measurements from Aqualim stations in Wallonia. This repository was named after the measuring station [Monteneau](https://www.openstreetmap.org/#map=16/50.3586/6.1232) in Wallonia of course. It measures water level and river flow in l'Amblève (die Amel).

The software has a [Github repo here](https://github.com/riklmr/monteneau). The encompassing project is tagged #Meuse on [Github.com](https://github.com/search?q=%23meuse) and on [medium.com](https://medium.com/search/tags?q=%23Meuse).

You might find the additional information in [belleheid README.md](https://github.com/riklmr/belleheid) useful.

This Python 3 script:
- retrieves a ist of Aqualim stations

## Purpose
This script retrieves and stores data that will be used for training neural networks that model the flow of the river Meuse.

## How to retrieve archived measurements from aqualim.environnement.wallonie.be
### Via website tables
This URL offers a list of available stations:
http://aqualim.environnement.wallonie.be/GeneralPages.do?method=displayStationsList

This url gives a page about a single station. It holds graphs for the last 30 days and links to pages with more data. You need to fill out a form with your personalia before you get to download measurements in a XLS table. The site limits the dowload to max. 1 year per request.


## Python libraries needed
The usual: pandas, time, json, urllib, re, pickle.

Also: Beautiful Soup (bs4), Postgres client (psycopg2).