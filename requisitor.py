from pytz import country_names
import requests
import json
# import pydantic

# state = country_names
# for y,x in state.items():
#     print(x)
# # class CovidBrasil:
# #     def __init__(self, country = None, state = None, specific_date = None **kwargs):
            # self.country = country
            # self.state = state
            # self.specific_date = specific_date
# #         super().__init__(**kwargs)

# #     def requisita(self):



# '''(PADRÃO) Lista casos por todos estados brasileiros
# https://covid19-brazil-api.now.sh/api/report/v1'''
# r = requests.get('https://covid19-brazil-api.now.sh/api/report/v1').json()



# '''Lista casos por estado brasileiro
# https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp
# r = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp').json()'''
# r = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/{self.country}/uf/{self.state}').json()



# '''Lista casos no brasil em data específica.
# https://covid19-brazil-api.now.sh/api/report/v1/brazil/20200318
# r = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/20200318').json()'''
# r = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/{self.country}/{self.date}').json()



# '''Lista casos por país
# https://covid19-brazil-api.now.sh/api/report/v1/brazil
# r = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/Guatemala').json()'''
# r = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/{self.country}').json()


# '''Consultar status da API
# https://covid19-brazil-api.now.sh/api/status/v1'''
# r = requests.get('https://covid19-brazil-api.now.sh/api/status/v1').json()

