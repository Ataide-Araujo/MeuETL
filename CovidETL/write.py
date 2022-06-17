import logging
import csv

logger = logging.getLogger(__name__) #contém o nome do módulo
logger.setLevel(logging.INFO) #seta mensagens de info (erros, warnings, critical)
logging.basicConfig(level=logging.INFO)

class writer():
    HEADER_STATES = ('Id', 'UF', 'Estado', 'Casos confirmados', 'Mortes', 'Suspeitos', 'Negativados', 'Monitorado até' )
    HEADER_COUNTRY = ('País', 'Casos confirmados', 'Mortes', 'Atualizado até')

    @classmethod
    def write_brStates(cls, archive_name=None, header=HEADER_STATES, contain=None):
        with open(f'{archive_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            for item in contain:
                wr.writerow(item)
            logger.info('Gravado com sucesso!')

    
    @classmethod
    def write_allCountries(cls, archive_name=None, header=HEADER_COUNTRY,contain=None):
        with open(f'{archive_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            for item in contain:
                wr.writerow(item)
            logger.info('Gravado com sucesso!')
