from .requisitor import CovidMundo
from pytz import country_names

class Group:
    def group_all_countries():
        state = country_names
        lista = list()
        for sigla, pais in state.items():
            pais = CovidMundo.RepCountry(pais)
            print(f'Gravando o país: {pais}')
            country = CovidMundo(pais)
            oneCountry = country.requisita_paises()
            if oneCountry is not None:
                lista.append(oneCountry)
        return lista