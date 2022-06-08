from pytz import country_names
import requests
from datetime import datetime
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

def requisita_estados():
    # Lista casos por estado
    request = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp').json()
    id = request['uid']
    uf = request['uf']
    state = request['state']
    cases = request['cases']
    deaths = request['deaths']
    suspects = request['suspects']
    refuses = request['refuses']
    datenow = request['datetime'].split('T')[0]
    datenow = datetime.fromisoformat(datenow).strftime('%d-%m-%Y')
    requested_list = (id,uf,state, cases, deaths, suspects, refuses, datenow)
    return requested_list

def requisita_paises():
    # Lista de casos por país
    request = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/cuba').json()
    item = request['data']
    country = item['country']
    confirmed = item['confirmed']
    deaths = item['deaths']
    datenow = item['updated_at'].split('T')[0]
    datenow = datetime.fromisoformat(datenow).strftime('%d-%m-%Y')
    requested_list = (country, confirmed, deaths, datenow)
    return requested_list


# '''(PADRÃO) Lista casos por todos estados brasileiros
# https://covid19-brazil-api.now.sh/api/report/v1'''
# r = requests.get('https://covid19-brazil-api.now.sh/api/report/v1').json()





# '''Lista casos no brasil em data específica.
# https://covid19-brazil-api.now.sh/api/report/v1/brazil/20200318
# r = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/20200318').json()'''
# r = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/{self.country}/{self.date}').json()



# '''Consultar status da API
# https://covid19-brazil-api.now.sh/api/status/v1'''
# r = requests.get('https://covid19-brazil-api.now.sh/api/status/v1').json()

