from typing import List
import configparser
import os

class Configuration:
    def __init__(self) -> None:
        self.config_path = os.path.join(os.getcwd(), "assets", "utils", "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

        self.cases_national_url = self.config["Cases"]["National"]
        self.cases_state_url = self.config["Cases"]["State"]

        self.deaths_national_url = self.config["Deaths"]["National"]
        self.deaths_state_url = self.config["Deaths"]["State"]

        self.tests_national_url = self.config["Tests"]["National"]
        self.tests_state_url = self.config["Tests"]["State"]

        self.hospital_general_url = self.config["Hospital"]["General"]

        self.vaccination_progress_national_url = self.config["VaccinationProgress"]["National"]
        self.vaccination_progress_state_url = self.config["VaccinationProgress"]["State"]

        self.vaccination_registration_national_url = self.config["VaccinationRegistration"]["National"]
        self.vaccination_registration_state_url = self.config["VaccinationRegistration"]["State"]

    @property
    def config_path(self) -> str:
        return self._config_path
    
    @config_path.setter
    def config_path(self, param):
        self._config_path = param

class Documentation(Configuration):
    def __init__(self) -> None:
        super().__init__()

    @property
    def all_available_fields(self) -> List:
        return self.config.sections()
    
    @property
    def epidemic_fields(self) -> List:
        return self.all_available_fields[:4]

    @property
    def cases_param(self) -> List:
        return [field for field,_ in self.config.items("Cases")]
    
    @property
    def deaths_param(self) -> List:
        return [field for field,_ in self.config.items("Deaths")]
    
    @property
    def tests_param(self) -> List:
        return [field for field,_ in self.config.items("Tests")]

    @property
    def hospital_param(self) -> List:
        return [field for field,_ in self.config.items("Hospital")]
    
    @property
    def vaccination_fields(self) -> List:
        return self.all_available_fields[4:6]

    @property
    def vaccination_progress_param(self) -> List:
        return [field for field,_ in self.config.items("VaccinationProgress")]

    @property
    def vaccination_registration_param(self) -> List:
        return [field for field,_ in self.config.items("VaccinationRegistration")]
    
    @property
    def available_states(self) -> List:
        return ["Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang", "Perak", "Perlis", "Pulau Pinang", "Sabah", "Sarawak", "Selangor", "Terengganu", "W.P. Kuala Lumpur", "W.P. Labuan", "W.P. Putrajaya"]

class PathHelper(Configuration):
    def __init__(self) -> None:
        super().__init__()