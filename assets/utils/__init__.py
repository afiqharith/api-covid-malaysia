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
        self.client_query_start_date = None
        self.client_query_end_date = None
        self.client_query_state = None
    
    @property
    def client_query_start_date(self) -> str:
        return self._client_query_start_date
    
    @client_query_start_date.setter
    def client_query_start_date(self, start_date) -> None:
        if type(start_date) == str or type(start_date) == type(None):
            self._client_query_start_date = start_date
        else:
            raise Exception("Invalid value for start date.")

    @property
    def client_query_end_date(self) -> str:
        return self._client_query_end_date
    
    @client_query_end_date.setter
    def client_query_end_date(self, end_date) -> None:
        if type(end_date) == str or type(end_date) == type(None):
            self._client_query_end_date = end_date
        else:
            raise Exception("Invalid value for end date.")
    
    @property
    def client_query_state(self) -> str:
        return self._client_query_state
    
    @client_query_state.setter
    def client_query_state(self, state) -> None:
        if type(state) == str or type(state) == type(None):
            self._client_query_state = state
        else:
            raise Exception("Invalid value for state.")

    def get_cases_malaysia(self) -> dict:

        response_results = list()
        for row in range(len(df_cases_malaysia.index)):

            if self.client_query_start_date == df_cases_malaysia.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_cases_malaysia.columns)):
                    sub_response[f"{df_cases_malaysia.columns[column]}"] = str(df_cases_malaysia.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_cases_malaysia.columns)):
                    sub_response[f"{df_cases_malaysia.columns[column]}"] = str(df_cases_malaysia.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_cases_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_cases_malaysia.columns)):
                        sub_response[f"{df_cases_malaysia.columns[column]}"] = str(df_cases_malaysia.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_cases_state(self) -> dict:
        
        response_results = list()
        for row in range(len(df_cases_state.index)):

            if self.client_query_start_date == df_cases_state.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_cases_state.columns)):
                    sub_response[f"{df_cases_state.columns[column]}"] = str(df_cases_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_cases_state.columns)):
                    sub_response[f"{df_cases_state.columns[column]}"] = str(df_cases_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(df_cases_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_cases_state.columns)):
                        sub_response[f"{df_cases_state.columns[column]}"] = str(df_cases_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_deaths_malaysia(self) -> dict:

        response_results = list()
        for row in range(len(df_deaths_malaysia.index)):

            if self.client_query_start_date == df_deaths_malaysia.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_deaths_malaysia.columns)):
                    sub_response[f"{df_deaths_malaysia.columns[column]}"] = str(df_deaths_malaysia.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_deaths_malaysia.columns)):
                    sub_response[f"{df_deaths_malaysia.columns[column]}"] = str(df_deaths_malaysia.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_deaths_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_deaths_malaysia.columns)):
                        sub_response[f"{df_deaths_malaysia.columns[column]}"] = str(df_deaths_malaysia.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_deaths_state(self) -> dict:

        response_results = list()
        for row in range(len(df_deaths_state.index)):

            if self.client_query_start_date == df_deaths_state.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_deaths_state.columns)):
                    sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_deaths_state.columns)):
                    sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_deaths_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_deaths_state.columns)):
                        sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_tests_malaysia(self) -> dict:

        response_results = list()
        for row in range(len(df_tests_malaysia.index)):

            if self.client_query_start_date == df_tests_malaysia.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_tests_malaysia.columns)):
                    sub_response[f"{df_tests_malaysia.columns[column]}"] = str(df_tests_malaysia.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_tests_malaysia.columns)):
                    sub_response[f"{df_tests_malaysia.columns[column]}"] = str(df_tests_malaysia.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_tests_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_tests_malaysia.columns)):
                        sub_response[f"{df_tests_malaysia.columns[column]}"] = str(df_tests_malaysia.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_tests_state(self) -> dict:

        response_results = list()
        for row in range(len(df_tests_state.index)):

            if self.client_query_start_date == df_tests_state.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_tests_state.columns)):
                    sub_response[f"{df_tests_state.columns[column]}"] = str(df_tests_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_tests_state.columns)):
                    sub_response[f"{df_tests_state.columns[column]}"] = str(df_tests_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_tests_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_tests_state.columns)):
                        sub_response[f"{df_tests_state.columns[column]}"] = str(df_tests_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_hospital(self) -> dict:

        response_results = list()
        for row in range(len(df_hospital.index)):

            if self.client_query_start_date == df_hospital.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_hospital.columns)):
                    sub_response[f"{df_hospital.columns[column]}"] = str(df_hospital.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_hospital.columns)):
                    sub_response[f"{df_hospital.columns[column]}"] = str(df_hospital.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

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
        self.client_query_start_date = None
        self.client_query_end_date = None
        self.client_query_state = None

    @property
    def client_query_start_date(self) -> str:
        return self._client_query_start_date
    
    @client_query_start_date.setter
    def client_query_start_date(self, start_date) -> None:
        if type(start_date) == str or type(start_date) == type(None):
            self._client_query_start_date = start_date
        else:
            raise Exception("Invalid value for start date.")

    @property
    def client_query_end_date(self) -> str:
        return self._client_query_end_date
    
    @client_query_end_date.setter
    def client_query_end_date(self, end_date) -> None:
        if type(end_date) == str or type(end_date) == type(None):
            self._client_query_end_date = end_date
        else:
            raise Exception("Invalid value for end date.")
    
    @property
    def client_query_state(self) -> str:
        return self._client_query_state
    
    @client_query_state.setter
    def client_query_state(self, state) -> None:
        if type(state) == str or type(state) == type(None):
            self._client_query_state = state
        else:
            raise Exception("Invalid value for state.")
        
    def get_vaccine_malaysia(self) -> dict:

        response_results = list()
        for row in range(len(df_vaccine_malaysia .index)):

            if self.client_query_start_date == df_vaccine_malaysia.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_vaccine_malaysia.columns)):
                    sub_response[f"{df_vaccine_malaysia.columns[column]}"] = str(df_vaccine_malaysia.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_vaccine_malaysia.columns)):
                    sub_response[f"{df_vaccine_malaysia.columns[column]}"] = str(df_vaccine_malaysia.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_vaccine_malaysia.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_vaccine_malaysia.columns)):
                        sub_response[f"{df_vaccine_malaysia.columns[column]}"] = str(df_vaccine_malaysia.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_vaccine_state(self) -> dict:

        response_results = list()
        for row in range(len(df_vaccine_state.index)):

            if self.client_query_start_date == df_vaccine_state.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_vaccine_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_vaccine_state.columns)):
                    sub_response[f"{df_vaccine_state.columns[column]}"] = str(df_vaccine_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_vaccine_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_vaccine_state.columns)):
                    sub_response[f"{df_vaccine_state.columns[column]}"] = str(df_vaccine_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_vaccine_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(df_vaccine_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_vaccine_state.columns)):
                        sub_response[f"{df_vaccine_state.columns[column]}"] = str(df_vaccine_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None