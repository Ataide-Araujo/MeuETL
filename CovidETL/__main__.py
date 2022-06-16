from CovidETL import CovidBrasil, CovidMundo, Check
from CovidETL import writer
from CovidETL import Args

def main():
    args = Args.args_params()

    if Check.check_api():
        if args.estado:
            state = CovidBrasil
            dados = state.requisita_estados()
            writer.write_brStates(archive_name='Todos_estados',contain=dados)
            
        elif args.pais:
            country = CovidMundo
            dados = country.requisita_paises()
            writer.write_allCountries(archive_name='Todos_paises',contain=dados)


if __name__ == '__main__':
    main()
