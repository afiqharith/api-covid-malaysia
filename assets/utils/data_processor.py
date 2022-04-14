from .helper import PathHelper
import pandas as pd
import numpy as np
import datetime

class DataHandlerEpidemic:
    def __init__(self) -> None:
        self.client_query_start_date: str = None
        self.client_query_end_date: str = None
        self.client_query_state: str = None
        self.helper = PathHelper()

    @property
    def client_query_start_date(self) -> str:
        return self._client_query_start_date
    
    @client_query_start_date.setter
    def client_query_start_date(self, param) -> None:
        if type(param) == str or type(param) == type(None):
            self._client_query_start_date = param
        else:
            raise Exception("Invalid value for start date.")

    @property
    def client_query_end_date(self) -> str:
        return self._client_query_end_date
    
    @client_query_end_date.setter
    def client_query_end_date(self, param) -> None:
        if type(param) == str or type(param) == type(None):
            self._client_query_end_date = param
        else:
            raise Exception("Invalid value for end date.")
    
    @property
    def client_query_state(self) -> str:
        return self._client_query_state
    
    @client_query_state.setter
    def client_query_state(self, param) -> None:
        if type(param) == str or type(param) == type(None):
            self._client_query_state = param
        else:
            raise Exception("Invalid value for state.")

    def get_cases_national(self) -> dict:
        df_cases_national = pd.read_csv(self.helper.cases_national_url).fillna(0)

        response_results = list()
        for row in range(len(df_cases_national.index)):

            if self.client_query_start_date == df_cases_national.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_cases_national.columns)):
                    if isinstance(df_cases_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_cases_national.columns[column]}"] = int(df_cases_national.iloc[row, column])
                    else:
                        sub_response[f"{df_cases_national.columns[column]}"] = str(df_cases_national.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_cases_national.columns)):
                    if isinstance(df_cases_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_cases_national.columns[column]}"] = int(df_cases_national.iloc[row, column])
                    else:
                        sub_response[f"{df_cases_national.columns[column]}"] = str(df_cases_national.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_cases_national.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_cases_national.columns)):
                        if isinstance(df_cases_national.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_cases_national.columns[column]}"] = int(df_cases_national.iloc[row, column])
                        else:
                            sub_response[f"{df_cases_national.columns[column]}"] = str(df_cases_national.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_cases_state(self) -> dict:
        df_cases_state = pd.read_csv(self.helper.cases_state_url).fillna(0)

        response_results = list()
        for row in range(len(df_cases_state.index)):

            if self.client_query_start_date == df_cases_state.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_cases_state.columns)):
                    if isinstance(df_cases_state.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_cases_state.columns[column]}"] = int(df_cases_state.iloc[row, column])
                    else:
                        sub_response[f"{df_cases_state.columns[column]}"] = str(df_cases_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_cases_state.columns)):
                    if isinstance(df_cases_state.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_cases_state.columns[column]}"] = int(df_cases_state.iloc[row, column])
                    else:
                        sub_response[f"{df_cases_state.columns[column]}"] = str(df_cases_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(df_cases_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_cases_state.columns)):
                        if isinstance(df_cases_state.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_cases_state.columns[column]}"] = int(df_cases_state.iloc[row, column])
                        else:
                            sub_response[f"{df_cases_state.columns[column]}"] = str(df_cases_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_cases_state_all(self) -> dict:
        df_cases_state_all = pd.read_csv(self.helper.cases_state_url).fillna(0)
        response_results = list()

        for row in range(len(df_cases_state_all.index)):
            if self.client_query_start_date == df_cases_state_all.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_cases_state_all.columns)):
                    if isinstance(df_cases_state_all.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_cases_state_all.columns[column]}"] = int(df_cases_state_all.iloc[row, column])
                    else:
                        sub_response[f"{df_cases_state_all.columns[column]}"] = str(df_cases_state_all.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_cases_state_all.columns)):
                    if isinstance(df_cases_state_all.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_cases_state_all.columns[column]}"] = int(df_cases_state_all.iloc[row, column])
                    else:
                        sub_response[f"{df_cases_state_all.columns[column]}"] = str(df_cases_state_all.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(df_cases_state_all.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_cases_state_all.columns)):
                        if isinstance(df_cases_state_all.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_cases_state_all.columns[column]}"] = int(df_cases_state_all.iloc[row, column])
                        else:
                            sub_response[f"{df_cases_state_all.columns[column]}"] = str(df_cases_state_all.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_deaths_national(self) -> dict:
        df_deaths_national = pd.read_csv(self.helper.deaths_national_url).fillna(0)

        response_results = list()
        for row in range(len(df_deaths_national.index)):

            if self.client_query_start_date == df_deaths_national.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_deaths_national.columns)):
                    if isinstance(df_deaths_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_deaths_national.columns[column]}"] = int(df_deaths_national.iloc[row, column])
                    else:
                        sub_response[f"{df_deaths_national.columns[column]}"] = str(df_deaths_national.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_deaths_national.columns)):
                    if isinstance(df_deaths_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_deaths_national.columns[column]}"] = int(df_deaths_national.iloc[row, column])
                    else:
                        sub_response[f"{df_deaths_national.columns[column]}"] = str(df_deaths_national.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_deaths_national.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_deaths_national.columns)):
                        if isinstance(df_deaths_national.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_deaths_national.columns[column]}"] = int(df_deaths_national.iloc[row, column])
                        else:
                            sub_response[f"{df_deaths_national.columns[column]}"] = str(df_deaths_national.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_deaths_state(self) -> dict:
        df_deaths_state = pd.read_csv(self.helper.deaths_state_url).fillna(0)

        response_results = list()
        for row in range(len(df_deaths_state.index)):

            if self.client_query_start_date == df_deaths_state.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_deaths_state.columns)):
                    if isinstance(df_deaths_state.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_deaths_state.columns[column]}"] = int(df_deaths_state.iloc[row, column])
                    else:
                        sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_deaths_state.columns)):
                    if isinstance(df_deaths_state.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_deaths_state.columns[column]}"] = int(df_deaths_state.iloc[row, column])
                    else:
                        sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_deaths_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_deaths_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_deaths_state.columns)):
                        if isinstance(df_deaths_state.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_deaths_state.columns[column]}"] = int(df_deaths_state.iloc[row, column])
                        else:
                            sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_deaths_state_all(self) -> dict:
        df_deaths_state = pd.read_csv(self.helper.deaths_state_url).fillna(0)

        response_results = list()
        for row in range(len(df_deaths_state.index)):

            if self.client_query_start_date == df_deaths_state.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_deaths_state.columns)):
                    if isinstance(df_deaths_state.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_deaths_state.columns[column]}"] = int(df_deaths_state.iloc[row, column])
                    else:
                        sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_deaths_state.columns)):
                    if isinstance(df_deaths_state.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_deaths_state.columns[column]}"] = int(df_deaths_state.iloc[row, column])
                    else:
                        sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_deaths_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_deaths_state.columns)):
                        if isinstance(df_deaths_state.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_deaths_state.columns[column]}"] = int(df_deaths_state.iloc[row, column])
                        else:
                            sub_response[f"{df_deaths_state.columns[column]}"] = str(df_deaths_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_tests_national(self) -> dict:
        df_tests_national = pd.read_csv(self.helper.tests_national_url).fillna(0)

        response_results = list()
        for row in range(len(df_tests_national.index)):

            if self.client_query_start_date == df_tests_national.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_tests_national.columns)):
                    if isinstance(df_tests_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_tests_national.columns[column]}"] = int(df_tests_national.iloc[row, column])
                    else:
                        sub_response[f"{df_tests_national.columns[column]}"] = str(df_tests_national.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_tests_national.columns)):
                    if isinstance(df_tests_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_tests_national.columns[column]}"] = int(df_tests_national.iloc[row, column])
                    else:
                        sub_response[f"{df_tests_national.columns[column]}"] = str(df_tests_national.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_tests_national.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_tests_national.columns)):
                        if isinstance(df_tests_national.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_tests_national.columns[column]}"] = int(df_tests_national.iloc[row, column])
                        else:
                            sub_response[f"{df_tests_national.columns[column]}"] = str(df_tests_national.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_tests_state(self) -> dict:
        df_tests_state = pd.read_csv(self.helper.tests_state_url).fillna(0)

        response_results = list()
        for row in range(len(df_tests_state.index)):

            if self.client_query_start_date == df_tests_state.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_tests_state.columns)):
                    if isinstance(df_tests_state.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_tests_state.columns[column]}"] = int(df_tests_state.iloc[row, column])
                    else:
                        sub_response[f"{df_tests_state.columns[column]}"] = str(df_tests_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_tests_state.columns)):
                    if isinstance(df_tests_state.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_tests_state.columns[column]}"] = int(df_tests_state.iloc[row, column])
                    else:
                        sub_response[f"{df_tests_state.columns[column]}"] = str(df_tests_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_tests_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_tests_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_tests_state.columns)):
                        if isinstance(df_tests_state.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_tests_state.columns[column]}"] = int(df_tests_state.iloc[row, column])
                        else:
                            sub_response[f"{df_tests_state.columns[column]}"] = str(df_tests_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_hospital(self) -> dict:
        df_hospital = pd.read_csv(self.helper.hospital_general_url).fillna(0)

        response_results = list()
        for row in range(len(df_hospital.index)):

            if self.client_query_start_date == df_hospital.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_hospital.columns)):
                    if isinstance(df_hospital.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_hospital.columns[column]}"] = int(df_hospital.iloc[row, column])
                    else:
                        sub_response[f"{df_hospital.columns[column]}"] = str(df_hospital.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_hospital.columns)):
                    if isinstance(df_hospital.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_hospital.columns[column]}"] = int(df_hospital.iloc[row, column])
                    else:
                        sub_response[f"{df_hospital.columns[column]}"] = str(df_hospital.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_hospital.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_hospital.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_hospital.columns)):
                        if isinstance(df_hospital.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_hospital.columns[column]}"] = int(df_hospital.iloc[row, column])
                        else:
                            sub_response[f"{df_hospital.columns[column]}"] = str(df_hospital.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None


class DataHandlerVaccination:
    def __init__(self) -> None:
        self.client_query_start_date: str = None
        self.client_query_end_date: str = None
        self.client_query_state: str = None
        self.helper = PathHelper()

    @property
    def client_query_start_date(self) -> str:
        return self._client_query_start_date
    
    @client_query_start_date.setter
    def client_query_start_date(self, param) -> None:
        if type(param) == str or type(param) == type(None):
            self._client_query_start_date = param
        else:
            raise Exception("Invalid value for start date.")

    @property
    def client_query_end_date(self) -> str:
        return self._client_query_end_date
    
    @client_query_end_date.setter
    def client_query_end_date(self, param) -> None:
        if type(param) == str or type(param) == type(None):
            self._client_query_end_date = param
        else:
            raise Exception("Invalid value for end date.")
    
    @property
    def client_query_state(self) -> str:
        return self._client_query_state
    
    @client_query_state.setter
    def client_query_state(self, param) -> None:
        if type(param) == str or type(param) == type(None):
            self._client_query_state = param
        else:
            raise Exception("Invalid value for state.")
        
    def get_vaccination_progress_national(self) -> dict:
        df_vaccination_progress_national = pd.read_csv(self.helper.vaccination_progress_national_url).fillna(0)

        response_results = list()
        for row in range(len(df_vaccination_progress_national .index)):

            if self.client_query_start_date == df_vaccination_progress_national.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_vaccination_progress_national.columns)):
                    if isinstance(df_vaccination_progress_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_vaccination_progress_national.columns[column]}"] = int(df_vaccination_progress_national.iloc[row, column])
                    else:
                        sub_response[f"{df_vaccination_progress_national.columns[column]}"] = str(df_vaccination_progress_national.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(df_vaccination_progress_national.columns)):
                    if isinstance(df_vaccination_progress_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{df_vaccination_progress_national.columns[column]}"] = int(df_vaccination_progress_national.iloc[row, column])
                    else:
                        sub_response[f"{df_vaccination_progress_national.columns[column]}"] = str(df_vaccination_progress_national.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(df_vaccination_progress_national.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_vaccination_progress_national.columns)):
                        if isinstance(df_vaccination_progress_national.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{df_vaccination_progress_national.columns[column]}"] = int(df_vaccination_progress_national.iloc[row, column])
                        else:
                            sub_response[f"{df_vaccination_progress_national.columns[column]}"] = str(df_vaccination_progress_national.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_vaccination_progress_state(self) -> dict:
        df_vaccination_progress_state = pd.read_csv(self.helper.vaccination_progress_state_url).fillna(0)
        
        response_results = list()
        for row in range(len(df_vaccination_progress_state.index)):

            if self.client_query_start_date == df_vaccination_progress_state.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == df_vaccination_progress_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_vaccination_progress_state.columns)):
                    if df_vaccination_progress_state.columns[column].isdigit():
                        sub_response[f"{df_vaccination_progress_state.columns[column]}"] = int(df_vaccination_progress_state.iloc[row, column])
                    else:
                        sub_response[f"{df_vaccination_progress_state.columns[column]}"] = str(df_vaccination_progress_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == df_vaccination_progress_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(df_vaccination_progress_state.columns)):
                    if df_vaccination_progress_state.columns[column].isdigit():
                        sub_response[f"{df_vaccination_progress_state.columns[column]}"] = int(df_vaccination_progress_state.iloc[row, column])
                    else:
                        sub_response[f"{df_vaccination_progress_state.columns[column]}"] = str(df_vaccination_progress_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == df_vaccination_progress_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(df_vaccination_progress_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(df_vaccination_progress_state.columns)):
                        if df_vaccination_progress_state.columns[column].isdigit():
                            sub_response[f"{df_vaccination_progress_state.columns[column]}"] = int(df_vaccination_progress_state.iloc[row, column])
                        else:
                            sub_response[f"{df_vaccination_progress_state.columns[column]}"] = str(df_vaccination_progress_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_vaccination_registration_national(self) -> dict:
        get_vaccination_registration_national = pd.read_csv(self.helper.vaccination_registration_national_url).fillna(0)

        response_results = list()
        for row in range(len(get_vaccination_registration_national .index)):

            if self.client_query_start_date == get_vaccination_registration_national.iloc[row, 0] and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(get_vaccination_registration_national.columns)):
                    if isinstance(get_vaccination_registration_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{get_vaccination_registration_national.columns[column]}"] = int(get_vaccination_registration_national.iloc[row, column])
                    else:
                        sub_response[f"{get_vaccination_registration_national.columns[column]}"] = str(get_vaccination_registration_national.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None:
                sub_response = dict()
                for column in range(len(get_vaccination_registration_national.columns)):
                    if isinstance(get_vaccination_registration_national.iloc[row, column], (np.int64, np.float64)):
                        sub_response[f"{get_vaccination_registration_national.columns[column]}"] = int(get_vaccination_registration_national.iloc[row, column])
                    else:
                        sub_response[f"{get_vaccination_registration_national.columns[column]}"] = str(get_vaccination_registration_national.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None:
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")

                if client_query_start_date_conversion <= datetime.datetime.strptime(get_vaccination_registration_national.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(get_vaccination_registration_national.columns)):
                        if isinstance(get_vaccination_registration_national.iloc[row, column], (np.int64, np.float64)):
                            sub_response[f"{get_vaccination_registration_national.columns[column]}"] = int(get_vaccination_registration_national.iloc[row, column])
                        else:
                            sub_response[f"{get_vaccination_registration_national.columns[column]}"] = str(get_vaccination_registration_national.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None

    def get_vaccination_registration_state(self) -> dict:
        
        get_vaccination_registration_state = pd.read_csv(self.helper.vaccination_registration_state_url).fillna(0)
        
        response_results = list()
        for row in range(len(get_vaccination_registration_state.index)):

            if self.client_query_start_date == get_vaccination_registration_state.iloc[row, 0] and self.client_query_end_date == None and self.client_query_state.lower() == get_vaccination_registration_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(get_vaccination_registration_state.columns)):
                    if get_vaccination_registration_state.columns[column].isdigit():
                        sub_response[f"{get_vaccination_registration_state.columns[column]}"] = int(get_vaccination_registration_state.iloc[row, column])
                    else:
                        sub_response[f"{get_vaccination_registration_state.columns[column]}"] = str(get_vaccination_registration_state.iloc[row, column])
                response_results.append(sub_response)
                break

            elif self.client_query_start_date == None and self.client_query_end_date == None and self.client_query_state.lower() == get_vaccination_registration_state.iloc[row, 1].lower():
                sub_response = dict()
                for column in range(len(get_vaccination_registration_state.columns)):
                    if get_vaccination_registration_state.columns[column].isdigit():
                        sub_response[f"{get_vaccination_registration_state.columns[column]}"] = int(get_vaccination_registration_state.iloc[row, column])
                    else:
                        sub_response[f"{get_vaccination_registration_state.columns[column]}"] = str(get_vaccination_registration_state.iloc[row, column])
                response_results.append(sub_response)

            elif self.client_query_start_date != None and self.client_query_end_date != None and self.client_query_state.lower() == get_vaccination_registration_state.iloc[row, 1].lower():
                client_query_start_date_conversion = datetime.datetime.strptime(self.client_query_start_date, "%Y-%m-%d")
                client_query_end_date_conversion = datetime.datetime.strptime(self.client_query_end_date, "%Y-%m-%d")
                if client_query_start_date_conversion <= datetime.datetime.strptime(get_vaccination_registration_state.iloc[row, 0], "%Y-%m-%d") <= client_query_end_date_conversion:
                    sub_response = dict()
                    for column in range(len(get_vaccination_registration_state.columns)):
                        if get_vaccination_registration_state.columns[column].isdigit():
                            sub_response[f"{get_vaccination_registration_state.columns[column]}"] = int(get_vaccination_registration_state.iloc[row, column])
                        else:
                            sub_response[f"{get_vaccination_registration_state.columns[column]}"] = str(get_vaccination_registration_state.iloc[row, column])
                    response_results.append(sub_response)

        if len(response_results) > 0:
            return response_results
        else:
            return None


if __name__ =="__main__":
    pass