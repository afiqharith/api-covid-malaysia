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

class DataHandler:
    def __init__(self) -> None:
        pass
        
    def get_cases_malaysia(client_query_date) -> dict:
        for row in range(len(df_cases_malaysia.index)):
            if client_query_date == df_cases_malaysia.iloc[row, 0]:
                cases_new = int(df_cases_malaysia.iloc[row, 1])
                cases_import = int(df_cases_malaysia.iloc[row, 2])
                cases_recovered = int(df_cases_malaysia.iloc[row, 3])
                cluster_import = int(df_cases_malaysia.iloc[row, 4])
                cluster_religious = int(df_cases_malaysia.iloc[row, 5])
                cluster_community = int(df_cases_malaysia.iloc[row, 6])
                cluster_highRisk = int(df_cases_malaysia.iloc[row, 7])
                cluster_education = int(df_cases_malaysia.iloc[row, 8])
                cluster_detentionCentre = int(df_cases_malaysia.iloc[row, 9])
                cluster_workplace = int(df_cases_malaysia.iloc[row, 10])

                results = {
                    "cases_new": cases_new,
                    "cases_import": cases_import,
                    "cases_recovered": cases_recovered,
                    "cluster_import": cluster_import,
                    "cluster_religious": cluster_religious,
                    "cluster_community": cluster_community,
                    "cluster_highRisk": cluster_highRisk,
                    "cluster_education": cluster_education,
                    "cluster_detentionCentre": cluster_detentionCentre,
                    "cluster_workplace": cluster_workplace
                }
                break

            else:
                results = None

        return results

    def get_state_cases(client_query_date, client_query_state) -> dict:
        for row in range(len(df_cases_state.index)):
            if client_query_date == df_cases_state.iloc[row, 0] and client_query_state.lower() == df_cases_state.iloc[row, 1].lower():
                cases_import = int(df_cases_state.iloc[row, 2])
                cases_new = int(df_cases_state.iloc[row, 3])
                cases_recovered = int(df_cases_state.iloc[row, 4])

                results = {
                    "cases_import": cases_import,
                    "cases_new": cases_new,
                    "cases_recovered": cases_recovered
                }
                break
            else:
                results = None
        return results

    def get_deaths_malaysia(client_query_date):
        for row in range(len(df_detahs_malaysia.index)):
            if client_query_date == df_detahs_malaysia.iloc[row, 0]:
                deaths_new = int(df_detahs_malaysia.iloc[row, 1])
                deaths_new_dod = int(df_detahs_malaysia.iloc[row, 2])
                deaths_bid = int(df_detahs_malaysia.iloc[row, 3])
                deaths_bid_dod = int(df_detahs_malaysia.iloc[row, 4])

                results = {
                    "deaths_new": deaths_new,
                    "deaths_new_dod": deaths_new_dod,
                    "deaths_bid": deaths_bid,
                    "deaths_bid_dod": deaths_bid_dod,
                }
                break
            else:
                results = None
        return results

    def get_deaths_state(client_query_date, client_query_state):
        for row in range(len(df_deaths_state.index)):
            if client_query_date == df_deaths_state.iloc[row, 0] and client_query_state == df_deaths_state.iloc[row, 1]:
                deaths_new = int(df_deaths_state.iloc[row, 2])
                deaths_new_dod = int(df_deaths_state.iloc[row, 3])
                deaths_bid = int(df_deaths_state.iloc[row, 4])
                deaths_bid_dod = int(df_deaths_state.iloc[row, 5])

                results = {
                    "deaths_new": deaths_new,
                    "deaths_new_dod": deaths_new_dod,
                    "deaths_bid": deaths_bid,
                    "deaths_bid_dod": deaths_bid_dod
                }
                break
            else:
                results = None
        return results