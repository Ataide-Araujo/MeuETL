import logging
from CovidETL import CovidBrasil, CovidMundo
from CovidETL import writer
import argparse
from pytz import country_names


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-estado","--estado", help="Informe a sigla do estado", type=str)
    parser.add_argument("-pais","--pais", help="Informe o nome do país", type=str)
    parser.add_argument("--all", help="Pega todos os países da lista", action="store_true")
    args = parser.parse_args()
  

    if args.estado:
        state = CovidBrasil.requisita_estados(states=args.estado)
        writer.write_brStates(archive_name=args.estado,contain=state)
    elif args.pais:

        country = CovidMundo
        dados = country.requisita_paises(country=args.pais)
        writer.write_allCountries(archive_name=args.pais,contain=dados)
    
    elif args.all:
        state = country_names
        for sigla, pais in state.items():
            pais = CovidMundo.RepCountry(pais)
            print(f'Gravando o país: {pais}')
            country = CovidMundo(pais)
            oneCountry = country.requisita_paises()
            writer.write_allCountries(archive_name=pais, contain=oneCountry)