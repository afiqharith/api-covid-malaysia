# Malaysia Covid-19 API

### 1. Install dependencies

```sh
$ pip3 install -r requirements.txt
```

### 2. Run project

Run:

```sh
$ python3 wsgi.py
```

### 3. Query

| Format |      Path       |             Fields             |            Query            |
| :----: | :-------------: | :----------------------------: | :-------------------------: |
|  json  | index, epidemic | cases, deaths, tests, hospital | start_date, end_date, state |

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

Usage:

```sh
https://api-covid19-malaysia.herokuapp.com/epidemic/cases?state=Selangor&start_date=2021-01-02&end_date=2021-01-05
```

### 4. Heroku-App

[![HEROKU](https://img.shields.io/badge/Malaysia_Covid19_API-HEROKU-purple)](https://api-covid19-malaysia.herokuapp.com/)
