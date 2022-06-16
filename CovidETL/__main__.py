from CovidETL import CovidBrasil, CovidMundo, Group, Check
from CovidETL import writer
from CovidETL import Args

def main():
    args = Args.args_params()

    if Check.check_api():
        if args.estado:
            state = CovidBrasil(state=args.estado)
            dados = state.requisita_estados()
            writer.write_brStates(archive_name=args.estado,contain=dados)
        elif args.pais:
            country = CovidMundo(country=args.pais)
            dados = country.requisita_paises()
            writer.write_oneCountry(archive_name=args.pais,contain=dados)
        
        elif args.all:
            oneCountry = Group.group_all_countries()
            writer.write_allCountries(archive_name='All_Contries', contain=oneCountry)
            

if __name__ == '__main__':
    main()
