import pandas as pd
import configparser
import os

config_path = os.path.join(os.getcwd(), "assets", "utils", "config.ini")

config = configparser.ConfigParser()
config.read(config_path)

cases_malaysia_url = config["COVID_CASES_URL"]["MALAYSIA"]
df_cases_malaysia = pd.read_csv(cases_malaysia_url).fillna(0)

cases_state_url = config["COVID_CASES_URL"]["STATE"]
df_cases_state = pd.read_csv(cases_state_url).fillna(0)

deaths_malaysia_url = config["COVID_DEATHS_URL"]["MALAYSIA"]
df_detahs_malaysia = pd.read_csv(deaths_malaysia_url).fillna(0)

deaths_state_url = config["COVID_DEATHS_URL"]["STATE"]
df_deaths_state = pd.read_csv(deaths_state_url).fillna(0)

tests_malaysia_url = config["COVID_TESTS_URL"]["MALAYSIA"]
df_tests_malaysia = pd.read_csv(tests_malaysia_url).fillna(0)

tests_state_url = config["COVID_TESTS_URL"]["STATE"]
df_tests_state = pd.read_csv(tests_state_url).fillna(0)

hospital_general_url = config["COVID_HOSPITAL_URL"]["GENERAL"]
df_hospital = pd.read_csv(hospital_general_url).fillna(0)

class DataHandler:
    def __init__(self) -> None:
        pass
        
    def get_cases_malaysia(client_query_date) -> dict:
        for row in range(len(df_cases_malaysia.index)):
            if client_query_date == df_cases_malaysia.iloc[row, 0]:
                results = {
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
                }
                break

            else:
                results = None

        return results

    def get_state_cases(client_query_date, client_query_state) -> dict:
        for row in range(len(df_cases_state.index)):
            if client_query_date == df_cases_state.iloc[row, 0] and client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                results = {
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
                }
                break
            else:
                results = None
        return results

    def get_deaths_malaysia(client_query_date):
        for row in range(len(df_detahs_malaysia.index)):
            if client_query_date == df_detahs_malaysia.iloc[row, 0]:
                results = {
                    f"{df_detahs_malaysia.columns[1]}": int(df_detahs_malaysia.iloc[row, 1]),
                    f"{df_detahs_malaysia.columns[2]}": int(df_detahs_malaysia.iloc[row, 2]),
                    f"{df_detahs_malaysia.columns[3]}": int(df_detahs_malaysia.iloc[row, 3]),
                    f"{df_detahs_malaysia.columns[4]}": int(df_detahs_malaysia.iloc[row, 4]),
                    f"{df_detahs_malaysia.columns[5]}": int(df_detahs_malaysia.iloc[row, 5]),
                    f"{df_detahs_malaysia.columns[6]}": int(df_detahs_malaysia.iloc[row, 6]),
                    f"{df_detahs_malaysia.columns[7]}": int(df_detahs_malaysia.iloc[row, 7])
                }
                break
            else:
                results = None
        return results

    def get_deaths_state(client_query_date, client_query_state):
        for row in range(len(df_deaths_state.index)):
            if client_query_date == df_deaths_state.iloc[row, 0] and client_query_state == df_deaths_state.iloc[row, 1]:
                results = {
                    f"{df_deaths_state.columns[2]}": int(df_deaths_state.iloc[row, 2]),
                    f"{df_deaths_state.columns[3]}": int(df_deaths_state.iloc[row, 3]),
                    f"{df_deaths_state.columns[4]}": int(df_deaths_state.iloc[row, 4]),
                    f"{df_deaths_state.columns[5]}": int(df_deaths_state.iloc[row, 5]),
                    f"{df_deaths_state.columns[6]}": int(df_deaths_state.iloc[row, 6]),
                    f"{df_deaths_state.columns[7]}": int(df_deaths_state.iloc[row, 7]),
                    f"{df_deaths_state.columns[8]}": int(df_deaths_state.iloc[row, 8])
                }
                break
            else:
                results = None
        return results

    def get_tests_malaysia(client_query_date):
        for row in range(len(df_tests_malaysia.index)):
            if client_query_date == df_tests_malaysia.iloc[row, 0]:
                results = {
                    f"{df_tests_malaysia.columns[1]}": int(df_tests_malaysia.iloc[row, 1]),
                    f"{df_tests_malaysia.columns[2]}": int(df_tests_malaysia.iloc[row, 2])
                }
                break
            else:
                results = None
        return results

    def get_tests_state(client_query_date, client_query_state):
        for row in range(len(df_tests_state.index)):
            if client_query_date == df_tests_state.iloc[row, 0] and client_query_state == df_tests_state.iloc[row, 1]:
                results = {
                    f"{df_tests_state.columns[2]}": int(df_tests_state.iloc[row, 2]),
                    f"{df_tests_state.columns[3]}": int(df_tests_state.iloc[row, 3])
                }
                break
            else:
                results = None
        return results

    def get_hospital(client_query_date, client_query_state) -> dict:
        for row in range(len(df_hospital.index)):
            if client_query_date == df_hospital.iloc[row, 0] and client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                results = {
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
                }
                break
            else:
                results = None
        return results