import requests
from datetime import datetime
import logging
import sys
import re
from unidecode import unidecode
# import pydantic

logger = logging.getLogger(__name__) #contém o nome do módulo
logger.setLevel(logging.INFO) #seta mensagens de info (erros, warnings, critical)
logging.basicConfig(level=logging.INFO)


# state = country_names
# for y,x in state.items():
#     print(x)
class CovidBrasil:
    def requisita_estados(states=None):
        # Lista casos por estado
        if states is None:
            logging.warning('É obrigatório informar um estado (ex: sp)')
            sys.exit()
        request = requests.get('https://covid19-brazil-api.now.sh/api/status/v1')
        if request.status_code != 200:
            logger.warning('API fora do ar.')
            sys.exit()

        request = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{states}').json()

        try:
            request['uid']
        except KeyError:
            logging.error(f' Estado "{states}" não encontrado! ')
            sys.exit()

        # Parser
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




class CovidMundo:
    def __init__(self, country):
        self.country = country

    @classmethod
    def check_api(cls):
        request = requests.get('https://covid19-brazil-api.now.sh/api/status/v1')
        if request.status_code != 200:
            logger.warning('API fora do ar.')
            sys.exit()
        logger.info('API ON!')
        return True


    @staticmethod
    def RepCountry(country):
        return re.sub('\&|\'|\.|\!|\?|\(|\)|\ç','',unidecode(country))


    def getCountry(self):
        return self.country


    def requisita_paises(self):
        # Lista de casos por país
        request = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1/{self.country}').json()

        try:
            request['data']['country']
            # Parser
            item = request['data']
            country = item['country']
            confirmed = item['confirmed']
            deaths = item['deaths']
            datenow = item['updated_at'].split('T')[0]
            datenow = datetime.fromisoformat(datenow).strftime('%d-%m-%Y')
            requested_list1 = (country, confirmed, deaths, datenow)
            return requested_list1
        except KeyError:
            logging.error(f' País "{self.country}" não encontrado! ')
        

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

