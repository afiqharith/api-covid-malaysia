import configparser
import os

class Configuration:
    def __init__(self) -> None:
        self.config_path = os.path.join(os.getcwd(), "assets", "utils", "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

        self.cases_malaysia_url = self.config["COVID_CASES_URL"]["MALAYSIA"]
        self.cases_state_url = self.config["COVID_CASES_URL"]["STATE"]
        self.deaths_malaysia_url = self.config["COVID_DEATHS_URL"]["MALAYSIA"]
        self.deaths_state_url = self.config["COVID_DEATHS_URL"]["STATE"]
        self.tests_malaysia_url = self.config["COVID_TESTS_URL"]["MALAYSIA"]
        self.tests_state_url = self.config["COVID_TESTS_URL"]["STATE"]
        self.hospital_general_url = self.config["COVID_HOSPITAL_URL"]["GENERAL"]
        self.vaccine_malaysia_url = self.config["VACCINE_URL"]["MALAYSIA"]
        self.vaccine_state_url = self.config["VACCINE_URL"]["STATE"]

    @property
    def config_path(self) -> str:
        return self._config_path
    
    @config_path.setter
    def config_path(self, param):
        self._config_path = param

class PathHelper(Configuration):
    def __init__(self) -> None:
        super().__init__()