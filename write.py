import logging
import csv



class writer():
    header_states = ('Id', 'UF', 'Estado', 'Casos confirmados', 'Mortes', 'Suspeitos', 'Negativados', 'Monitorado até' )
    header_country = ('País', 'Casos confirmados', 'Mortes', 'Atualizado até')

    @classmethod
    def write_brStates(cls, archive_name=None, header=header_states, contain=None):
        with open(f'casos_{archive_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            wr.writerow(contain)

    
    @classmethod
    def write_allCountries(cls, archive_name=None, header=header_country,contain=None):
        with open(f'dados_{archive_name}.csv', 'w') as file:
            wr = csv.writer(file, delimiter=',')
            wr.writerow(header)
            wr.writerow(contain)