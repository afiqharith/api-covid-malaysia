# WEB API COVID19 MALAYSIA

[![MOH](https://img.shields.io/badge/Epidemic_Reference-MOH_Public_Data-orange)](https://github.com/MoH-Malaysia/covid19-public)
[![CITF](https://img.shields.io/badge/Vaccination_Reference-CITF_Malaysia_Public_Data-blue)](https://github.com/CITF-Malaysia/citf-public)

<div align="center" style="border:solid; border-size: 0.4vmin; border-color:black">
  <img src="assets/public/images/web.png">
</div>

### 1. To run locally in Python3 environment

Run:

```sh
$ pip3 install -r requirements.txt
$ python3 wsgi.py
```

### 2. To run locally in Docker

Run:

```sh
$ docker build -t apicovidmy .
$ docker run -p 5000:5000 -d apicovidmy .
```

### 3. Query

| Category    | Fields                         | Query                         |
| :---------- | :----------------------------- | :---------------------------- |
| index       | None                           | None                          |
| epidemic    | cases, deaths, tests, hospital | start_date, end_date, \*state |
| vaccination | registration, progress         | start_date, end_date, state   |

Available states:

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

Check out:

```sh
CURL-X POST -H "Content-Type: application/json" https://api-covidmy.onrender.com//category
```

### 4. Access data using GET request

Fetching epidemic category data example:

```sh
https://api-covidmy.onrender.com//epidemic/cases?state=Selangor&start_date=2021-01-02&end_date=2021-01-05
```

Fetching vaccination category data example:

```sh
https://api-covidmy.onrender.com//vaccination/registration?state=Selangor&start_date=2021-06-02&end_date=2021-07-05
```

### 5. Access data using JSON POST request

Fetching epidemic category data example:

```sh
CURL-X POST -H "Content-Type: application/json" -d '{"start_date": "2021-02-03", "end_date": "2021-07-05", "state": "Selangor"}' https://api-covidmy.onrender.com//epidemic/cases
```

Fetching vaccination category data example:

```sh
CURL -X POST -H "Content-Type: application/json" -d '{"start_date": "2021-02-03", "end_date": "2021-07-05", "state": "Selangor"}'  https://api-covidmy.onrender.com//vaccination/progress
```

### 6. Render Web Service

[![render](https://img.shields.io/badge/API_Covid_MY-render-088F8F)](https://api-covidmy.onrender.com//)
