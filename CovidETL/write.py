import logging
import csv
import os

logger = logging.getLogger(__name__) #contém o nome do módulo
logger.setLevel(logging.INFO) #seta mensagens de info (erros, warnings, critical)
logging.basicConfig(level=logging.INFO)


class writer:
    HEADER_STATES = ('Id', 'UF', 'Estado', 'Casos confirmados', 'Mortes', 'Suspeitos', 'Negativados', 'Monitorado até' )
    HEADER_COUNTRY = ('País', 'Casos confirmados', 'Mortes', 'Atualizado até')

    @classmethod
    def write_brStates(cls, file_name=None, header=HEADER_STATES, contain=None):
        if not os.path.exists(f'{os.getcwd()}/{file_name}'):
            os.makedirs(f'{os.getcwd()}/{file_name}')
        os.chdir(f'{os.getcwd()}/{file_name}')
        with open(f'{file_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            for item in contain:
                wr.writerow(item)
            logger.info('Gravado com sucesso!')

    
    @classmethod
    def write_allCountries(cls, file_name=None, header=HEADER_COUNTRY,contain=None):
        if not os.path.exists(f'{os.getcwd()}/{file_name}'):
            os.makedirs(f'{os.getcwd()}/{file_name}')
        os.chdir(f'{os.getcwd()}/{file_name}')
        with open(f'{file_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            for item in contain:
                wr.writerow(item)
            logger.info('Gravado com sucesso!')
