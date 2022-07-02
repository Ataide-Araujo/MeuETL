import logging
import csv
from .make_dir import make_dir

logger = logging.getLogger(__name__) #contém o nome do módulo


class writer:
    HEADER_STATES = ('Id', 'UF', 'Estado', 'Casos confirmados', 'Mortes', 'Suspeitos', 'Negativados', 'Monitorado até' )
    HEADER_COUNTRY = ('País', 'Casos confirmados', 'Mortes', 'Atualizado até')

    @classmethod
    def write_brStates(cls, file_name=None, header=HEADER_STATES, contain=None):
        make_dir(file_name)
        logger.info('Diretório criado...')
        with open(f'{file_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            for item in contain:
                wr.writerow(item)
            logger.info('Gravado em csv com sucesso!')

    
    @classmethod
    def write_allCountries(cls, file_name=None, header=HEADER_COUNTRY,contain=None):
        make_dir(file_name)
        logger.info('Diretório criado...')
        with open(f'{file_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            for item in contain:
                wr.writerow(item)
            logger.info('Gravado em csv com sucesso!')
