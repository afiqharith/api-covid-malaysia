import pandas as pd
import configparser
import os
import datetime

config_path = os.path.join(os.getcwd(), "assets", "utils", "config.ini")

config = configparser.ConfigParser()
config.read(config_path)

cases_malaysia_url = config["COVID_CASES_URL"]["MALAYSIA"]
df_cases_malaysia = pd.read_csv(cases_malaysia_url).fillna(0)

cases_state_url = config["COVID_CASES_URL"]["STATE"]
df_cases_state = pd.read_csv(cases_state_url).fillna(0)

deaths_malaysia_url = config["COVID_DEATHS_URL"]["MALAYSIA"]
df_deaths_malaysia = pd.read_csv(deaths_malaysia_url).fillna(0)

deaths_state_url = config["COVID_DEATHS_URL"]["STATE"]
df_deaths_state = pd.read_csv(deaths_state_url).fillna(0)

tests_malaysia_url = config["COVID_TESTS_URL"]["MALAYSIA"]
df_tests_malaysia = pd.read_csv(tests_malaysia_url).fillna(0)

tests_state_url = config["COVID_TESTS_URL"]["STATE"]
df_tests_state = pd.read_csv(tests_state_url).fillna(0)

hospital_general_url = config["COVID_HOSPITAL_URL"]["GENERAL"]
df_hospital = pd.read_csv(hospital_general_url).fillna(0)

vaccine_state_url = config["VACCINE_URL"]["STATE"]
df_vaccine_state = pd.read_csv(vaccine_state_url).fillna(0)

vaccine_malaysia_url = config["VACCINE_URL"]["MALAYSIA"]
df_vaccine_malaysia = pd.read_csv(vaccine_malaysia_url).fillna(0)


class DataHandlerEpidemic:
    def __init__(self) -> None:
        pass
        
    def get_cases_malaysia(client_query_start_date, client_query_end_date) -> dict:

        response_results = list()
        for row in range(len(df_cases_malaysia.index)):
            if client_query_start_date == df_cases_malaysia.iloc[row, 0] and client_query_end_date == None:
                response_results.append({
                    f"{df_cases_malaysia.columns[0]}": str(df_cases_malaysia.iloc[row, 0]),
                    f"{df_cases_malaysia.columns[1]}": int(df_cases_malaysia.iloc[row, 1]),
                    f"{df_cases_malaysia.columns[2]}": int(df_cases_malaysia.iloc[row, 2]),
                    f"{df_cases_malaysia.columns[3]}": int(df_cases_malaysia.iloc[row, 3]),
                    f"{df_cases_malaysia.columns[4]}" : int(df_cases_malaysia.iloc[row, 4]),
                    f"{df_cases_malaysia.columns[5]}" : int(df_cases_malaysia.iloc[row, 5]),
                    f"{df_cases_malaysia.columns[6]}" : int(df_cases_malaysia.iloc[row, 6]),
                    f"{df_cases_malaysia.columns[7]}" : int(df_cases_malaysia.iloc[row, 7]),
                    f"{df_cases_malaysia.columns[8]}" : int(df_cases_malaysia.iloc[row, 8]),
                    f"{df_cases_malaysia.columns[9]}" : int(df_cases_malaysia.iloc[row, 9]),
                    f"{df_cases_malaysia.columns[10]}" : int(df_cases_malaysia.iloc[row, 10]),
                    f"{df_cases_malaysia.columns[11]}" : int(df_cases_malaysia.iloc[row, 11]),
                    f"{df_cases_malaysia.columns[12]}": int(df_cases_malaysia.iloc[row, 12]),
                    f"{df_cases_malaysia.columns[13]}": int(df_cases_malaysia.iloc[row, 13]),
                    f"{df_cases_malaysia.columns[14]}": int(df_cases_malaysia.iloc[row, 14]),
                    f"{df_cases_malaysia.columns[15]}": int(df_cases_malaysia.iloc[row, 15]),
                    f"{df_cases_malaysia.columns[16]}": int(df_cases_malaysia.iloc[row, 16]),
                    f"{df_cases_malaysia.columns[17]}": int(df_cases_malaysia.iloc[row, 17]),
                    f"{df_cases_malaysia.columns[18]}": int(df_cases_malaysia.iloc[row, 18])
                })
                break
            elif client_query_start_date == None and client_query_end_date == None:
                    response_results.append({
                        f"{df_cases_malaysia.columns[0]}": str(df_cases_malaysia.iloc[row, 0]),
                        f"{df_cases_malaysia.columns[1]}": int(df_cases_malaysia.iloc[row, 1]),
                        f"{df_cases_malaysia.columns[2]}": int(df_cases_malaysia.iloc[row, 2]),
                        f"{df_cases_malaysia.columns[3]}": int(df_cases_malaysia.iloc[row, 3]),
                        f"{df_cases_malaysia.columns[4]}" : int(df_cases_malaysia.iloc[row, 4]),
                        f"{df_cases_malaysia.columns[5]}" : int(df_cases_malaysia.iloc[row, 5]),
                        f"{df_cases_malaysia.columns[6]}" : int(df_cases_malaysia.iloc[row, 6]),
                        f"{df_cases_malaysia.columns[7]}" : int(df_cases_malaysia.iloc[row, 7]),
                        f"{df_cases_malaysia.columns[8]}" : int(df_cases_malaysia.iloc[row, 8]),
                        f"{df_cases_malaysia.columns[9]}" : int(df_cases_malaysia.iloc[row, 9]),
                        f"{df_cases_malaysia.columns[10]}" : int(df_cases_malaysia.iloc[row, 10]),
                        f"{df_cases_malaysia.columns[11]}" : int(df_cases_malaysia.iloc[row, 11]),
                        f"{df_cases_malaysia.columns[12]}": int(df_cases_malaysia.iloc[row, 12]),
                        f"{df_cases_malaysia.columns[13]}": int(df_cases_malaysia.iloc[row, 13]),
                        f"{df_cases_malaysia.columns[14]}": int(df_cases_malaysia.iloc[row, 14]),
                        f"{df_cases_malaysia.columns[15]}": int(df_cases_malaysia.iloc[row, 15]),
                        f"{df_cases_malaysia.columns[16]}": int(df_cases_malaysia.iloc[row, 16]),
                        f"{df_cases_malaysia.columns[17]}": int(df_cases_malaysia.iloc[row, 17]),
                        f"{df_cases_malaysia.columns[18]}": int(df_cases_malaysia.iloc[row, 18])
                })

            elif client_query_start_date != None and client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_cases_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    response_results.append({
                        f"{df_cases_malaysia.columns[0]}": str(df_cases_malaysia.iloc[row, 0]),
                        f"{df_cases_malaysia.columns[1]}": int(df_cases_malaysia.iloc[row, 1]),
                        f"{df_cases_malaysia.columns[2]}": int(df_cases_malaysia.iloc[row, 2]),
                        f"{df_cases_malaysia.columns[3]}": int(df_cases_malaysia.iloc[row, 3]),
                        f"{df_cases_malaysia.columns[4]}" : int(df_cases_malaysia.iloc[row, 4]),
                        f"{df_cases_malaysia.columns[5]}" : int(df_cases_malaysia.iloc[row, 5]),
                        f"{df_cases_malaysia.columns[6]}" : int(df_cases_malaysia.iloc[row, 6]),
                        f"{df_cases_malaysia.columns[7]}" : int(df_cases_malaysia.iloc[row, 7]),
                        f"{df_cases_malaysia.columns[8]}" : int(df_cases_malaysia.iloc[row, 8]),
                        f"{df_cases_malaysia.columns[9]}" : int(df_cases_malaysia.iloc[row, 9]),
                        f"{df_cases_malaysia.columns[10]}" : int(df_cases_malaysia.iloc[row, 10]),
                        f"{df_cases_malaysia.columns[11]}" : int(df_cases_malaysia.iloc[row, 11]),
                        f"{df_cases_malaysia.columns[12]}": int(df_cases_malaysia.iloc[row, 12]),
                        f"{df_cases_malaysia.columns[13]}": int(df_cases_malaysia.iloc[row, 13]),
                        f"{df_cases_malaysia.columns[14]}": int(df_cases_malaysia.iloc[row, 14]),
                        f"{df_cases_malaysia.columns[15]}": int(df_cases_malaysia.iloc[row, 15]),
                        f"{df_cases_malaysia.columns[16]}": int(df_cases_malaysia.iloc[row, 16]),
                        f"{df_cases_malaysia.columns[17]}": int(df_cases_malaysia.iloc[row, 17]),
                        f"{df_cases_malaysia.columns[18]}": int(df_cases_malaysia.iloc[row, 18])
                    })
        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_cases_state(client_query_start_date, client_query_end_date, client_query_state) -> dict:
        response_results = list()
        for row in range(len(df_cases_state.index)):
            if client_query_start_date == df_cases_state.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                response_results.append({
                    f"{df_cases_state.columns[0]}": str(df_cases_state.iloc[row, 0]),
                    f"{df_cases_state.columns[1]}": str(df_cases_state.iloc[row, 1]),
                    f"{df_cases_state.columns[2]}": int(df_cases_state.iloc[row, 2]),
                    f"{df_cases_state.columns[3]}": int(df_cases_state.iloc[row, 3]),
                    f"{df_cases_state.columns[4]}": int(df_cases_state.iloc[row, 4]),
                    f"{df_cases_state.columns[5]}" : int(df_cases_state.iloc[row, 5]),
                    f"{df_cases_state.columns[6]}" : int(df_cases_state.iloc[row, 6]),
                    f"{df_cases_state.columns[7]}" : int(df_cases_state.iloc[row, 7]),
                    f"{df_cases_state.columns[8]}" : int(df_cases_state.iloc[row, 8]),
                    f"{df_cases_state.columns[9]}" : int(df_cases_state.iloc[row, 9]),
                    f"{df_cases_state.columns[10]}" : int(df_cases_state.iloc[row, 10]),
                    f"{df_cases_state.columns[11]}" : int(df_cases_state.iloc[row, 11]),
                    f"{df_cases_state.columns[12]}" : int(df_cases_state.iloc[row, 12])
                })
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                response_results.append({
                    f"{df_cases_state.columns[0]}": str(df_cases_state.iloc[row, 0]),
                    f"{df_cases_state.columns[1]}": str(df_cases_state.iloc[row, 1]),
                    f"{df_cases_state.columns[2]}": int(df_cases_state.iloc[row, 2]),
                    f"{df_cases_state.columns[3]}": int(df_cases_state.iloc[row, 3]),
                    f"{df_cases_state.columns[4]}": int(df_cases_state.iloc[row, 4]),
                    f"{df_cases_state.columns[5]}" : int(df_cases_state.iloc[row, 5]),
                    f"{df_cases_state.columns[6]}" : int(df_cases_state.iloc[row, 6]),
                    f"{df_cases_state.columns[7]}" : int(df_cases_state.iloc[row, 7]),
                    f"{df_cases_state.columns[8]}" : int(df_cases_state.iloc[row, 8]),
                    f"{df_cases_state.columns[9]}" : int(df_cases_state.iloc[row, 9]),
                    f"{df_cases_state.columns[10]}" : int(df_cases_state.iloc[row, 10]),
                    f"{df_cases_state.columns[11]}" : int(df_cases_state.iloc[row, 11]),
                    f"{df_cases_state.columns[12]}" : int(df_cases_state.iloc[row, 12])
                })

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(df_cases_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    response_results.append({
                        f"{df_cases_state.columns[0]}": str(df_cases_state.iloc[row, 0]),
                        f"{df_cases_state.columns[1]}": str(df_cases_state.iloc[row, 1]),
                        f"{df_cases_state.columns[2]}": int(df_cases_state.iloc[row, 2]),
                        f"{df_cases_state.columns[3]}": int(df_cases_state.iloc[row, 3]),
                        f"{df_cases_state.columns[4]}": int(df_cases_state.iloc[row, 4]),
                        f"{df_cases_state.columns[5]}" : int(df_cases_state.iloc[row, 5]),
                        f"{df_cases_state.columns[6]}" : int(df_cases_state.iloc[row, 6]),
                        f"{df_cases_state.columns[7]}" : int(df_cases_state.iloc[row, 7]),
                        f"{df_cases_state.columns[8]}" : int(df_cases_state.iloc[row, 8]),
                        f"{df_cases_state.columns[9]}" : int(df_cases_state.iloc[row, 9]),
                        f"{df_cases_state.columns[10]}" : int(df_cases_state.iloc[row, 10]),
                        f"{df_cases_state.columns[11]}" : int(df_cases_state.iloc[row, 11]),
                        f"{df_cases_state.columns[12]}" : int(df_cases_state.iloc[row, 12])
                    })

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_deaths_malaysia(client_query_start_date, client_query_end_date):
        response_results = list()
        for row in range(len(df_deaths_malaysia.index)):
            if client_query_start_date == df_deaths_malaysia.iloc[row, 0] and client_query_end_date == None:
                response_results.append({
                    f"{df_deaths_malaysia.columns[0]}": str(df_deaths_malaysia.iloc[row, 0]),
                    f"{df_deaths_malaysia.columns[1]}": int(df_deaths_malaysia.iloc[row, 1]),
                    f"{df_deaths_malaysia.columns[2]}": int(df_deaths_malaysia.iloc[row, 2]),
                    f"{df_deaths_malaysia.columns[3]}": int(df_deaths_malaysia.iloc[row, 3]),
                    f"{df_deaths_malaysia.columns[4]}": int(df_deaths_malaysia.iloc[row, 4]),
                    f"{df_deaths_malaysia.columns[5]}": int(df_deaths_malaysia.iloc[row, 5]),
                    f"{df_deaths_malaysia.columns[6]}": int(df_deaths_malaysia.iloc[row, 6]),
                    f"{df_deaths_malaysia.columns[7]}": int(df_deaths_malaysia.iloc[row, 7])
                })
                break

            elif client_query_start_date == None and client_query_end_date == None:
                response_results.append({
                    f"{df_deaths_malaysia.columns[0]}": str(df_deaths_malaysia.iloc[row, 0]),
                    f"{df_deaths_malaysia.columns[1]}": int(df_deaths_malaysia.iloc[row, 1]),
                    f"{df_deaths_malaysia.columns[2]}": int(df_deaths_malaysia.iloc[row, 2]),
                    f"{df_deaths_malaysia.columns[3]}": int(df_deaths_malaysia.iloc[row, 3]),
                    f"{df_deaths_malaysia.columns[4]}": int(df_deaths_malaysia.iloc[row, 4]),
                    f"{df_deaths_malaysia.columns[5]}": int(df_deaths_malaysia.iloc[row, 5]),
                    f"{df_deaths_malaysia.columns[6]}": int(df_deaths_malaysia.iloc[row, 6]),
                    f"{df_deaths_malaysia.columns[7]}": int(df_deaths_malaysia.iloc[row, 7])
                })

            elif client_query_start_date != None and client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_deaths_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    response_results.append({
                    f"{df_deaths_malaysia.columns[0]}": str(df_deaths_malaysia.iloc[row, 0]),
                    f"{df_deaths_malaysia.columns[1]}": int(df_deaths_malaysia.iloc[row, 1]),
                    f"{df_deaths_malaysia.columns[2]}": int(df_deaths_malaysia.iloc[row, 2]),
                    f"{df_deaths_malaysia.columns[3]}": int(df_deaths_malaysia.iloc[row, 3]),
                    f"{df_deaths_malaysia.columns[4]}": int(df_deaths_malaysia.iloc[row, 4]),
                    f"{df_deaths_malaysia.columns[5]}": int(df_deaths_malaysia.iloc[row, 5]),
                    f"{df_deaths_malaysia.columns[6]}": int(df_deaths_malaysia.iloc[row, 6]),
                    f"{df_deaths_malaysia.columns[7]}": int(df_deaths_malaysia.iloc[row, 7])
                })

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_deaths_state(client_query_start_date, client_query_end_date, client_query_state):
        response_results = list()
        for row in range(len(df_deaths_state.index)):
            if client_query_start_date == df_deaths_state.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                response_results.append({
                    f"{df_deaths_state.columns[0]}": str(df_deaths_state.iloc[row, 0]),
                    f"{df_deaths_state.columns[1]}": str(df_deaths_state.iloc[row, 1]),
                    f"{df_deaths_state.columns[2]}": int(df_deaths_state.iloc[row, 2]),
                    f"{df_deaths_state.columns[3]}": int(df_deaths_state.iloc[row, 3]),
                    f"{df_deaths_state.columns[4]}": int(df_deaths_state.iloc[row, 4]),
                    f"{df_deaths_state.columns[5]}": int(df_deaths_state.iloc[row, 5]),
                    f"{df_deaths_state.columns[6]}": int(df_deaths_state.iloc[row, 6]),
                    f"{df_deaths_state.columns[7]}": int(df_deaths_state.iloc[row, 7]),
                    f"{df_deaths_state.columns[8]}": int(df_deaths_state.iloc[row, 8])
                })
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                response_results.append({
                    f"{df_deaths_state.columns[0]}": str(df_deaths_state.iloc[row, 0]),
                    f"{df_deaths_state.columns[1]}": str(df_deaths_state.iloc[row, 1]),
                    f"{df_deaths_state.columns[2]}": int(df_deaths_state.iloc[row, 2]),
                    f"{df_deaths_state.columns[3]}": int(df_deaths_state.iloc[row, 3]),
                    f"{df_deaths_state.columns[4]}": int(df_deaths_state.iloc[row, 4]),
                    f"{df_deaths_state.columns[5]}": int(df_deaths_state.iloc[row, 5]),
                    f"{df_deaths_state.columns[6]}": int(df_deaths_state.iloc[row, 6]),
                    f"{df_deaths_state.columns[7]}": int(df_deaths_state.iloc[row, 7]),
                    f"{df_deaths_state.columns[8]}": int(df_deaths_state.iloc[row, 8])
                })

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_deaths_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    response_results.append({
                        f"{df_deaths_state.columns[0]}": str(df_deaths_state.iloc[row, 0]),
                        f"{df_deaths_state.columns[1]}": str(df_deaths_state.iloc[row, 1]),
                        f"{df_deaths_state.columns[2]}": int(df_deaths_state.iloc[row, 2]),
                        f"{df_deaths_state.columns[3]}": int(df_deaths_state.iloc[row, 3]),
                        f"{df_deaths_state.columns[4]}": int(df_deaths_state.iloc[row, 4]),
                        f"{df_deaths_state.columns[5]}": int(df_deaths_state.iloc[row, 5]),
                        f"{df_deaths_state.columns[6]}": int(df_deaths_state.iloc[row, 6]),
                        f"{df_deaths_state.columns[7]}": int(df_deaths_state.iloc[row, 7]),
                        f"{df_deaths_state.columns[8]}": int(df_deaths_state.iloc[row, 8])
                    })

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_tests_malaysia(client_query_start_date, client_query_end_date):
        response_results = list()
        for row in range(len(df_tests_malaysia.index)):
            if client_query_start_date == df_tests_malaysia.iloc[row, 0] and client_query_end_date == None:
                response_results.append({
                    f"{df_tests_malaysia.columns[0]}": str(df_tests_malaysia.iloc[row, 0]),
                    f"{df_tests_malaysia.columns[1]}": int(df_tests_malaysia.iloc[row, 1]),
                    f"{df_tests_malaysia.columns[2]}": int(df_tests_malaysia.iloc[row, 2])
                })
                break

            elif client_query_start_date == None and client_query_end_date == None:
                response_results.append({
                    f"{df_tests_malaysia.columns[0]}": str(df_tests_malaysia.iloc[row, 0]),
                    f"{df_tests_malaysia.columns[1]}": int(df_tests_malaysia.iloc[row, 1]),
                    f"{df_tests_malaysia.columns[2]}": int(df_tests_malaysia.iloc[row, 2])
                })  

            elif client_query_start_date != None and client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_tests_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    response_results.append({
                        f"{df_tests_malaysia.columns[0]}": str(df_tests_malaysia.iloc[row, 0]),
                        f"{df_tests_malaysia.columns[1]}": int(df_tests_malaysia.iloc[row, 1]),
                        f"{df_tests_malaysia.columns[2]}": int(df_tests_malaysia.iloc[row, 2])
                    })

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_tests_state(client_query_start_date, client_query_end_date, client_query_state):
        response_results = list()
        for row in range(len(df_tests_state.index)):
            if client_query_start_date == df_tests_state.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                response_results.append({
                    f"{df_tests_state.columns[0]}": str(df_tests_state.iloc[row, 0]),
                    f"{df_tests_state.columns[1]}": str(df_tests_state.iloc[row, 1]),
                    f"{df_tests_state.columns[2]}": int(df_tests_state.iloc[row, 2]),
                    f"{df_tests_state.columns[3]}": int(df_tests_state.iloc[row, 3])
                })
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                response_results.append({
                    f"{df_tests_state.columns[0]}": str(df_tests_state.iloc[row, 0]),
                    f"{df_tests_state.columns[1]}": str(df_tests_state.iloc[row, 1]),
                    f"{df_tests_state.columns[2]}": int(df_tests_state.iloc[row, 2]),
                    f"{df_tests_state.columns[3]}": int(df_tests_state.iloc[row, 3])
                })

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_tests_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    response_results.append({
                    f"{df_tests_state.columns[0]}": str(df_tests_state.iloc[row, 0]),
                    f"{df_tests_state.columns[1]}": str(df_tests_state.iloc[row, 1]),
                    f"{df_tests_state.columns[2]}": int(df_tests_state.iloc[row, 2]),
                    f"{df_tests_state.columns[3]}": int(df_tests_state.iloc[row, 3])
                })

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_hospital(client_query_start_date, client_query_end_date, client_query_state) -> dict:
        response_results = list()
        for row in range(len(df_hospital.index)):
            if client_query_start_date == df_hospital.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                response_results.append({
                    f"{df_hospital.columns[0]}": str(df_hospital.iloc[row, 0]),
                    f"{df_hospital.columns[1]}": str(df_hospital.iloc[row, 1]),
                    f"{df_hospital.columns[2]}": int(df_hospital.iloc[row, 2]),
                    f"{df_hospital.columns[3]}": int(df_hospital.iloc[row, 3]),
                    f"{df_hospital.columns[4]}": int(df_hospital.iloc[row, 4]),
                    f"{df_hospital.columns[5]}" : int(df_hospital.iloc[row, 5]),
                    f"{df_hospital.columns[6]}" : int(df_hospital.iloc[row, 6]),
                    f"{df_hospital.columns[7]}" : int(df_hospital.iloc[row, 7]),
                    f"{df_hospital.columns[8]}" : int(df_hospital.iloc[row, 8]),
                    f"{df_hospital.columns[9]}" : int(df_hospital.iloc[row, 9]),
                    f"{df_hospital.columns[10]}" : int(df_hospital.iloc[row, 10]),
                    f"{df_hospital.columns[11]}" : int(df_hospital.iloc[row, 11]),
                    f"{df_hospital.columns[12]}" : int(df_hospital.iloc[row, 12]),
                    f"{df_hospital.columns[13]}" : int(df_hospital.iloc[row, 13])
                })
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                response_results.append({
                    f"{df_hospital.columns[0]}": str(df_hospital.iloc[row, 0]),
                    f"{df_hospital.columns[1]}": str(df_hospital.iloc[row, 1]),
                    f"{df_hospital.columns[2]}": int(df_hospital.iloc[row, 2]),
                    f"{df_hospital.columns[3]}": int(df_hospital.iloc[row, 3]),
                    f"{df_hospital.columns[4]}": int(df_hospital.iloc[row, 4]),
                    f"{df_hospital.columns[5]}" : int(df_hospital.iloc[row, 5]),
                    f"{df_hospital.columns[6]}" : int(df_hospital.iloc[row, 6]),
                    f"{df_hospital.columns[7]}" : int(df_hospital.iloc[row, 7]),
                    f"{df_hospital.columns[8]}" : int(df_hospital.iloc[row, 8]),
                    f"{df_hospital.columns[9]}" : int(df_hospital.iloc[row, 9]),
                    f"{df_hospital.columns[10]}" : int(df_hospital.iloc[row, 10]),
                    f"{df_hospital.columns[11]}" : int(df_hospital.iloc[row, 11]),
                    f"{df_hospital.columns[12]}" : int(df_hospital.iloc[row, 12]),
                    f"{df_hospital.columns[13]}" : int(df_hospital.iloc[row, 13])
                })

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_hospital.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    response_results.append({
                        f"{df_hospital.columns[0]}": str(df_hospital.iloc[row, 0]),
                        f"{df_hospital.columns[1]}": str(df_hospital.iloc[row, 1]),
                        f"{df_hospital.columns[2]}": int(df_hospital.iloc[row, 2]),
                        f"{df_hospital.columns[3]}": int(df_hospital.iloc[row, 3]),
                        f"{df_hospital.columns[4]}": int(df_hospital.iloc[row, 4]),
                        f"{df_hospital.columns[5]}" : int(df_hospital.iloc[row, 5]),
                        f"{df_hospital.columns[6]}" : int(df_hospital.iloc[row, 6]),
                        f"{df_hospital.columns[7]}" : int(df_hospital.iloc[row, 7]),
                        f"{df_hospital.columns[8]}" : int(df_hospital.iloc[row, 8]),
                        f"{df_hospital.columns[9]}" : int(df_hospital.iloc[row, 9]),
                        f"{df_hospital.columns[10]}" : int(df_hospital.iloc[row, 10]),
                        f"{df_hospital.columns[11]}" : int(df_hospital.iloc[row, 11]),
                        f"{df_hospital.columns[12]}" : int(df_hospital.iloc[row, 12]),
                        f"{df_hospital.columns[13]}" : int(df_hospital.iloc[row, 13])
                    })

        if len(response_results) > 0:
            return response_results
        else:
            return None


class DataHandlerVaccination:
    def __init__(self) -> None:
            pass
        
    def get_vaccine_malaysia(client_query_start_date, client_query_end_date) -> dict:

        response_results = list()
        for row in range(len(df_vaccine_malaysia .index)):
            if client_query_start_date == df_vaccine_malaysia.iloc[row, 0] and client_query_end_date == None:
                response_results.append({
                    f"{df_vaccine_malaysia.columns[0]}": str(df_vaccine_malaysia.iloc[row, 0]),
                    f"{df_vaccine_malaysia.columns[1]}": int(df_vaccine_malaysia.iloc[row, 1]),
                    f"{df_vaccine_malaysia.columns[2]}": int(df_vaccine_malaysia.iloc[row, 2]),
                    f"{df_vaccine_malaysia.columns[3]}": int(df_vaccine_malaysia.iloc[row, 3]),
                    f"{df_vaccine_malaysia.columns[4]}" : int(df_vaccine_malaysia.iloc[row, 4]),
                    f"{df_vaccine_malaysia.columns[5]}" : int(df_vaccine_malaysia.iloc[row, 5]),
                    f"{df_vaccine_malaysia.columns[6]}" : int(df_vaccine_malaysia.iloc[row, 6]),
                    f"{df_vaccine_malaysia.columns[7]}" : int(df_vaccine_malaysia.iloc[row, 7]),
                    f"{df_vaccine_malaysia.columns[8]}" : int(df_vaccine_malaysia.iloc[row, 8]),
                    f"{df_vaccine_malaysia.columns[9]}" : int(df_vaccine_malaysia.iloc[row, 9]),
                    f"{df_vaccine_malaysia.columns[10]}" : int(df_vaccine_malaysia.iloc[row, 10]),
                    f"{df_vaccine_malaysia.columns[11]}" : int(df_vaccine_malaysia.iloc[row, 11]),
                    f"{df_vaccine_malaysia.columns[12]}": int(df_vaccine_malaysia.iloc[row, 12]),
                    f"{df_vaccine_malaysia.columns[13]}": int(df_vaccine_malaysia.iloc[row, 13]),
                    f"{df_vaccine_malaysia.columns[14]}": int(df_vaccine_malaysia.iloc[row, 14]),
                    f"{df_vaccine_malaysia.columns[15]}": int(df_vaccine_malaysia.iloc[row, 15]),
                    f"{df_vaccine_malaysia.columns[16]}": int(df_vaccine_malaysia.iloc[row, 16]),
                    f"{df_vaccine_malaysia.columns[17]}": int(df_vaccine_malaysia.iloc[row, 17]),
                    f"{df_vaccine_malaysia.columns[18]}": int(df_vaccine_malaysia.iloc[row, 18])
                })
                break
            elif client_query_start_date == None and client_query_end_date == None:
                    response_results.append({
                        f"{df_vaccine_malaysia.columns[0]}": str(df_vaccine_malaysia.iloc[row, 0]),
                        f"{df_vaccine_malaysia.columns[1]}": int(df_vaccine_malaysia.iloc[row, 1]),
                        f"{df_vaccine_malaysia.columns[2]}": int(df_vaccine_malaysia.iloc[row, 2]),
                        f"{df_vaccine_malaysia.columns[3]}": int(df_vaccine_malaysia.iloc[row, 3]),
                        f"{df_vaccine_malaysia.columns[4]}" : int(df_vaccine_malaysia.iloc[row, 4]),
                        f"{df_vaccine_malaysia.columns[5]}" : int(df_vaccine_malaysia.iloc[row, 5]),
                        f"{df_vaccine_malaysia.columns[6]}" : int(df_vaccine_malaysia.iloc[row, 6]),
                        f"{df_vaccine_malaysia.columns[7]}" : int(df_vaccine_malaysia.iloc[row, 7]),
                        f"{df_vaccine_malaysia.columns[8]}" : int(df_vaccine_malaysia.iloc[row, 8]),
                        f"{df_vaccine_malaysia.columns[9]}" : int(df_vaccine_malaysia.iloc[row, 9]),
                        f"{df_vaccine_malaysia.columns[10]}" : int(df_vaccine_malaysia.iloc[row, 10]),
                        f"{df_vaccine_malaysia.columns[11]}" : int(df_vaccine_malaysia.iloc[row, 11]),
                        f"{df_vaccine_malaysia.columns[12]}": int(df_vaccine_malaysia.iloc[row, 12]),
                        f"{df_vaccine_malaysia.columns[13]}": int(df_vaccine_malaysia.iloc[row, 13]),
                        f"{df_vaccine_malaysia.columns[14]}": int(df_vaccine_malaysia.iloc[row, 14]),
                        f"{df_vaccine_malaysia.columns[15]}": int(df_vaccine_malaysia.iloc[row, 15]),
                        f"{df_vaccine_malaysia.columns[16]}": int(df_vaccine_malaysia.iloc[row, 16]),
                        f"{df_vaccine_malaysia.columns[17]}": int(df_vaccine_malaysia.iloc[row, 17]),
                        f"{df_vaccine_malaysia.columns[18]}": int(df_vaccine_malaysia.iloc[row, 18])
                })

            elif client_query_start_date != None and client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_vaccine_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    response_results.append({
                        f"{df_vaccine_malaysia.columns[0]}": str(df_vaccine_malaysia.iloc[row, 0]),
                        f"{df_vaccine_malaysia.columns[1]}": int(df_vaccine_malaysia.iloc[row, 1]),
                        f"{df_vaccine_malaysia.columns[2]}": int(df_vaccine_malaysia.iloc[row, 2]),
                        f"{df_vaccine_malaysia.columns[3]}": int(df_vaccine_malaysia.iloc[row, 3]),
                        f"{df_vaccine_malaysia.columns[4]}" : int(df_vaccine_malaysia.iloc[row, 4]),
                        f"{df_vaccine_malaysia.columns[5]}" : int(df_vaccine_malaysia.iloc[row, 5]),
                        f"{df_vaccine_malaysia.columns[6]}" : int(df_vaccine_malaysia.iloc[row, 6]),
                        f"{df_vaccine_malaysia.columns[7]}" : int(df_vaccine_malaysia.iloc[row, 7]),
                        f"{df_vaccine_malaysia.columns[8]}" : int(df_vaccine_malaysia.iloc[row, 8]),
                        f"{df_vaccine_malaysia.columns[9]}" : int(df_vaccine_malaysia.iloc[row, 9]),
                        f"{df_vaccine_malaysia.columns[10]}" : int(df_vaccine_malaysia.iloc[row, 10]),
                        f"{df_vaccine_malaysia.columns[11]}" : int(df_vaccine_malaysia.iloc[row, 11]),
                        f"{df_vaccine_malaysia.columns[12]}": int(df_vaccine_malaysia.iloc[row, 12]),
                        f"{df_vaccine_malaysia.columns[13]}": int(df_vaccine_malaysia.iloc[row, 13]),
                        f"{df_vaccine_malaysia.columns[14]}": int(df_vaccine_malaysia.iloc[row, 14]),
                        f"{df_vaccine_malaysia.columns[15]}": int(df_vaccine_malaysia.iloc[row, 15]),
                        f"{df_vaccine_malaysia.columns[16]}": int(df_vaccine_malaysia.iloc[row, 16]),
                        f"{df_vaccine_malaysia.columns[17]}": int(df_vaccine_malaysia.iloc[row, 17]),
                        f"{df_vaccine_malaysia.columns[18]}": int(df_cases_malaysia.iloc[row, 18])
                    })
        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_vaccine_state(client_query_start_date, client_query_end_date, client_query_state) -> dict:
        response_results = list()
        for row in range(len(df_vaccine_state.index)):
            if client_query_start_date == df_vaccine_state.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_vaccine_state.iloc[row, 1].lower():
                response_results.append({
                    f"{df_vaccine_state.columns[0]}": str(df_vaccine_state.iloc[row, 0]),
                    f"{df_vaccine_state.columns[1]}": str(df_vaccine_state.iloc[row, 1]),
                    f"{df_vaccine_state.columns[2]}": int(df_vaccine_state.iloc[row, 2]),
                    f"{df_vaccine_state.columns[3]}": int(df_vaccine_state.iloc[row, 3]),
                    f"{df_vaccine_state.columns[4]}": int(df_vaccine_state.iloc[row, 4]),
                    f"{df_vaccine_state.columns[5]}" : int(df_vaccine_state.iloc[row, 5]),
                    f"{df_vaccine_state.columns[6]}" : int(df_vaccine_state.iloc[row, 6]),
                    f"{df_vaccine_state.columns[7]}" : int(df_vaccine_state.iloc[row, 7]),
                    f"{df_vaccine_state.columns[8]}" : int(df_vaccine_state.iloc[row, 8]),
                    f"{df_vaccine_state.columns[9]}" : int(df_vaccine_state.iloc[row, 9]),
                    f"{df_vaccine_state.columns[10]}" : int(df_vaccine_state.iloc[row, 10]),
                    f"{df_vaccine_state.columns[11]}" : int(df_vaccine_state.iloc[row, 11]),
                    f"{df_vaccine_state.columns[12]}" : int(df_vaccine_state.iloc[row, 12])
                })
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_vaccine_state.iloc[row, 1].lower():
                response_results.append({
                    f"{df_vaccine_state.columns[0]}": str(df_vaccine_state.iloc[row, 0]),
                    f"{df_vaccine_state.columns[1]}": str(df_vaccine_state.iloc[row, 1]),
                    f"{df_vaccine_state.columns[2]}": int(df_vaccine_state.iloc[row, 2]),
                    f"{df_vaccine_state.columns[3]}": int(df_vaccine_state.iloc[row, 3]),
                    f"{df_vaccine_state.columns[4]}": int(df_vaccine_state.iloc[row, 4]),
                    f"{df_vaccine_state.columns[5]}" : int(df_vaccine_state.iloc[row, 5]),
                    f"{df_vaccine_state.columns[6]}" : int(df_vaccine_state.iloc[row, 6]),
                    f"{df_vaccine_state.columns[7]}" : int(df_vaccine_state.iloc[row, 7]),
                    f"{df_vaccine_state.columns[8]}" : int(df_vaccine_state.iloc[row, 8]),
                    f"{df_vaccine_state.columns[9]}" : int(df_vaccine_state.iloc[row, 9]),
                    f"{df_vaccine_state.columns[10]}" : int(df_vaccine_state.iloc[row, 10]),
                    f"{df_vaccine_state.columns[11]}" : int(df_vaccine_state.iloc[row, 11]),
                    f"{df_vaccine_state.columns[12]}" : int(df_vaccine_state.iloc[row, 12])
                })

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_vaccine_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(df_vaccine_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    response_results.append({
                        f"{df_vaccine_state.columns[0]}": str(df_vaccine_state.iloc[row, 0]),
                        f"{df_vaccine_state.columns[1]}": str(df_vaccine_state.iloc[row, 1]),
                        f"{df_vaccine_state.columns[2]}": int(df_vaccine_state.iloc[row, 2]),
                        f"{df_vaccine_state.columns[3]}": int(df_vaccine_state.iloc[row, 3]),
                        f"{df_vaccine_state.columns[4]}": int(df_vaccine_state.iloc[row, 4]),
                        f"{df_vaccine_state.columns[5]}" : int(df_vaccine_state.iloc[row, 5]),
                        f"{df_vaccine_state.columns[6]}" : int(df_vaccine_state.iloc[row, 6]),
                        f"{df_vaccine_state.columns[7]}" : int(df_vaccine_state.iloc[row, 7]),
                        f"{df_vaccine_state.columns[8]}" : int(df_vaccine_state.iloc[row, 8]),
                        f"{df_vaccine_state.columns[9]}" : int(df_vaccine_state.iloc[row, 9]),
                        f"{df_vaccine_state.columns[10]}" : int(df_vaccine_state.iloc[row, 10]),
                        f"{df_vaccine_state.columns[11]}" : int(df_vaccine_state.iloc[row, 11]),
                        f"{df_vaccine_state.columns[12]}" : int(df_vaccine_state.iloc[row, 12])
                    })

        if len(response_results) > 0:
            return response_results
        else:
            return None