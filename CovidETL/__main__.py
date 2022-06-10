from CovidETL import CovidBrasil, CovidMundo
from CovidETL import writer



if __name__ == '__main__':


    a = CovidBrasil.requisita_estados('sp')
    writer.write_brStates(archive_name='sp',contain=a)


    # b = CovidMundo
    # d = b.requisita_paises('cuba')
    # writer.write_allCountries(contain=d)