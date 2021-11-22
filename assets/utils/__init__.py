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
                sub_response = dict()
                for column in range(len(df_cases_malaysia.columns)):
                    sub_response[f"{df_cases_malaysia.columns[column]}"] = str(df_cases_malaysia.iloc[row, column])
                response_results.append(sub_response)
                break

            elif client_query_start_date == None and client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_cases_malaysia.columns)):
                    sub_response[f"{df_cases_malaysia.columns[column]}"] = str(df_cases_malaysia.iloc[row, column])
                response_results.append(sub_response)

            elif client_query_start_date != None and client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_cases_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_cases_malaysia.columns)):
                        sub_response[f"{df_cases_malaysia.columns[column]}"] = str(df_cases_malaysia.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_cases_state(client_query_start_date, client_query_end_date, client_query_state) -> dict:
        
        response_results = list()
        for row in range(len(df_cases_state.index)):

            if client_query_start_date == df_cases_state.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_cases_state.columns)):
                    sub_response[f"{df_cases_state.columns[column]}"] = str(df_cases_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_cases_state.columns)):
                    sub_response[f"{df_cases_state.columns[column]}"] = str(df_cases_state.iloc[row, column])
                response_results.append(sub_response)

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(df_cases_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_cases_state.columns)):
                        sub_response[f"{df_cases_state.columns[column]}"] = str(df_cases_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_deaths_malaysia(client_query_start_date, client_query_end_date):

        response_results = list()
        for row in range(len(df_deaths_malaysia.index)):

            if client_query_start_date == df_deaths_malaysia.iloc[row, 0] and client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_deaths_malaysia.columns)):
                    sub_response[f"{df_deaths_malaysia.columns[column]}"] = str(df_deaths_malaysia.iloc[row, column])
                response_results.append(sub_response)
                break

            elif client_query_start_date == None and client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_deaths_malaysia.columns)):
                    sub_response[f"{df_deaths_malaysia.columns[column]}"] = str(df_deaths_malaysia.iloc[row, column])
                response_results.append(sub_response)

            elif client_query_start_date != None and client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_deaths_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_deaths_malaysia.columns)):
                        sub_response[f"{df_deaths_malaysia.columns[column]}"] = str(df_deaths_malaysia.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_deaths_state(client_query_start_date, client_query_end_date, client_query_state):

        response_results = list()
        for row in range(len(df_deaths_state.index)):

            if client_query_start_date == df_deaths_state.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_deaths_state.columns)):
                    sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_deaths_state.columns)):
                    sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                response_results.append(sub_response)

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_deaths_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_deaths_state.columns)):
                        sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_tests_malaysia(client_query_start_date, client_query_end_date):

        response_results = list()
        for row in range(len(df_tests_malaysia.index)):

            if client_query_start_date == df_tests_malaysia.iloc[row, 0] and client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_tests_malaysia.columns)):
                    sub_response[f"{df_tests_malaysia.columns[column]}"] = str(df_tests_malaysia.iloc[row, column])
                response_results.append(sub_response)
                break

            elif client_query_start_date == None and client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_tests_malaysia.columns)):
                    sub_response[f"{df_tests_malaysia.columns[column]}"] = str(df_tests_malaysia.iloc[row, column])
                response_results.append(sub_response)

            elif client_query_start_date != None and client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_tests_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_tests_malaysia.columns)):
                        sub_response[f"{df_tests_malaysia.columns[column]}"] = str(df_tests_malaysia.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_tests_state(client_query_start_date, client_query_end_date, client_query_state):

        response_results = list()
        for row in range(len(df_tests_state.index)):

            if client_query_start_date == df_tests_state.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_tests_state.columns)):
                    sub_response[f"{df_tests_state.columns[column]}"] = str(df_tests_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_tests_state.columns)):
                    sub_response[f"{df_tests_state.columns[column]}"] = str(df_tests_state.iloc[row, column])
                response_results.append(sub_response)

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_tests_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_tests_state.columns)):
                        sub_response[f"{df_tests_state.columns[column]}"] = str(df_tests_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_hospital(client_query_start_date, client_query_end_date, client_query_state) -> dict:

        response_results = list()
        for row in range(len(df_hospital.index)):

            if client_query_start_date == df_hospital.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_hospital.columns)):
                    sub_response[f"{df_hospital.columns[column]}"] = str(df_hospital.iloc[row, column])
                response_results.append(sub_response)
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_hospital.columns)):
                    sub_response[f"{df_hospital.columns[column]}"] = str(df_hospital.iloc[row, column])
                response_results.append(sub_response)

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_hospital.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_hospital.columns)):
                        sub_response[f"{df_hospital.columns[column]}"] = str(df_hospital.iloc[row, column])
                    response_results.append(sub_response)

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
                sub_response = dict()
                for column in range(len(df_vaccine_malaysia.columns)):
                    sub_response[f"{df_vaccine_malaysia.columns[column]}"] = str(df_vaccine_malaysia.iloc[row, column])
                response_results.append(sub_response)
                break

            elif client_query_start_date == None and client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_vaccine_malaysia.columns)):
                    sub_response[f"{df_vaccine_malaysia.columns[column]}"] = str(df_vaccine_malaysia.iloc[row, column])
                response_results.append(sub_response)

            elif client_query_start_date != None and client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_vaccine_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_vaccine_malaysia.columns)):
                        sub_response[f"{df_vaccine_malaysia.columns[column]}"] = str(df_vaccine_malaysia.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_vaccine_state(client_query_start_date, client_query_end_date, client_query_state) -> dict:

        response_results = list()
        for row in range(len(df_vaccine_state.index)):

            if client_query_start_date == df_vaccine_state.iloc[row, 0] and client_query_end_date == None and client_query_state.lower() == df_vaccine_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_vaccine_state.columns)):
                    sub_response[f"{df_vaccine_state.columns[column]}"] = str(df_vaccine_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif client_query_start_date == None and client_query_end_date == None and client_query_state.lower() == df_vaccine_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_vaccine_state.columns)):
                    sub_response[f"{df_vaccine_state.columns[column]}"] = str(df_vaccine_state.iloc[row, column])
                response_results.append(sub_response)

            elif client_query_start_date != None and client_query_end_date != None and client_query_state.lower() == df_vaccine_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(df_vaccine_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_vaccine_state.columns)):
                        sub_response[f"{df_vaccine_state.columns[column]}"] = str(df_vaccine_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None