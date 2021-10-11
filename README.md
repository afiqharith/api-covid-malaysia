# Malaysia Covid-19 API

### 1. Install dependencies

Run:

```sh
$ pip3 install -r requirements.txt
```

### 2. Run project

Run:

```sh
$ python3 wsgi.py
```

### 3. Query

| Format |           Path           |        Fields Epidemic         | Field Vaccine |            Query            |
| :----: | :----------------------: | :----------------------------: | :-----------: | :-------------------------: |
|  json  | index, epidemic, vaccine | cases, deaths, tests, hospital |     None      | start_date, end_date, state |

State available values:

- Johor
- Kedah
- Kelantan
- Melaka
- Negeri Sembilan
- Pahang
- Perak
- Perlis
- Pulau Pinang
- Sabah
- Sarawak
- Selangor
- Terengganu
- W.P. Kuala Lumpur
- W.P. Labuan
- W.P. Putrajaya

### 5. Access data using GET request

Epidemic usage example:

```sh
https://api-covid19-malaysia.herokuapp.com/epidemic/cases?state=Selangor&start_date=2021-01-02&end_date=2021-01-05
```

Vaccine usage example:

```sh
https://api-covid19-malaysia.herokuapp.com/vaccine?state=Selangor&start_date=2021-06-02&end_date=2021-07-05
```

### 6. Access data using JSON POST request

Epidemic usage example:

```sh
CURL-X POST -H "Content-Type: application/json" -d '{"start_date": "2021-02-03", end_date=2021-07-05, "state": "Selangor"}'  https://api-covid19-malaysia.herokuapp.com/epidemic/cases
```

Vaccine usage example:

```sh
CURL -X POST -H "Content-Type: application/json" -d '{"start_date": "2021-02-03", end_date=2021-07-05, "state": "Selangor"}'  https://api-covid19-malaysia.herokuapp.com/vaccine
```

### 7. Heroku-App

[![HEROKU](https://img.shields.io/badge/Malaysia_Covid19_API-HEROKU-purple)](https://api-covid19-malaysia.herokuapp.com/)
