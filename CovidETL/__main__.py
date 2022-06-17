from CovidETL import CovidBrasil, CovidMundo, Check
from CovidETL import writer
from CovidETL import Args
from CovidETL import MakeGraph

def main():
    args = Args.args_params()

    if Check.check_api():
        if args.estado:
            archive_name='casos_Todos_estados'
            state = CovidBrasil
            dados = state.requisita_estados()
            writer.write_brStates(archive_name=archive_name,contain=dados)
            MakeGraph.processState(f'{archive_name}.csv')

        elif args.pais:
            archive_name='casos_Todos_paises'
            country = CovidMundo
            dados = country.requisita_paises()
            writer.write_allCountries(archive_name=archive_name,contain=dados)
            MakeGraph.processCountry(f'{archive_name}.csv')


if __name__ == '__main__':
    main()
