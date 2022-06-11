from CovidETL import CovidBrasil, CovidMundo
from CovidETL import writer
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-estado","--estado", help="Informe a sigla do estado", type=str)
    parser.add_argument("-pais","--pais", help="Informe o nome do país", type=str)
    args = parser.parse_args()
  

    if args.estado:
        a = CovidBrasil.requisita_estados(states=args.estado)
        writer.write_brStates(archive_name=args.estado,contain=a)
    elif args.pais:

        b = CovidMundo
        d = b.requisita_paises(country=args.pais)
        writer.write_allCountries(archive_name=args.pais,contain=d)