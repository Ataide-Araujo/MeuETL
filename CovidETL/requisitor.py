import requests
from datetime import datetime
import logging


logger = logging.getLogger(__name__) #contém o nome do módulo
logger.setLevel(logging.INFO) #seta mensagens de info (erros, warnings, critical)
logging.basicConfig(level=logging.INFO)


class Check:
    @classmethod
    def check_api(cls, url=None):
        url = url or 'https://covid19-brazil-api.now.sh/api/status/v1'
        request = requests.get(url)
        if request.status_code != 200:
            logger.warning('API fora do ar.')
            return False
        logger.info('API ON!')
        return True


class CovidBrasil:
    def requisita_estados():
        # Lista casos por estado
        request = requests.get(f'https://covid19-brazil-api.now.sh/api/report/v1').json()
        
        # Parser
        requested_list = list()
        for item in request['data']:
            id = item['uid']
            uf = item['uf']
            state = item['state']
            cases = item['cases']
            deaths = item['deaths']
            suspects = item['suspects']
            refuses = item['refuses']
            datenow = item['datetime'].split('T')[0]
            datenow = datetime.fromisoformat(datenow).strftime('%d-%m-%Y')
            requested_list.append((id,uf,state, cases, deaths, suspects, refuses, datenow))
        return requested_list



class CovidMundo:
    def requisita_paises():
        # Lista de todos os países
        request = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/countries').json()
        
        # parser
        requested_list = list()
        for item in request['data']:
            country = item['country']
            confirmed = item['confirmed']
            deaths = item['deaths']
            datenow = item['updated_at'].split('T')[0]
            datenow = datetime.fromisoformat(datenow).strftime('%d-%m-%Y')
            requested_list.append((country, confirmed, deaths, datenow))
        return requested_list
