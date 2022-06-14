import logging
import csv



class writer():
    HEADER_STATES = ('Id', 'UF', 'Estado', 'Casos confirmados', 'Mortes', 'Suspeitos', 'Negativados', 'Monitorado até' )
    HEADER_COUNTRY = ('País', 'Casos confirmados', 'Mortes', 'Atualizado até')

    @classmethod
    def write_brStates(cls, archive_name=None, header=HEADER_STATES, contain=None):
        with open(f'casos_{archive_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            wr.writerow(contain)

    
    @classmethod
    def write_allCountries(cls, archive_name=None, header=HEADER_COUNTRY,contain=None):
        if contain is None:
            contain = ['Não há dados para esse país']
        with open(f'dados_{archive_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            wr.writerow(contain)