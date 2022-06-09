from CovidETL.requisitor import CovidBrasil
from CovidETL.requisitor import CovidMundo
from CovidETL.write import writer


a = CovidBrasil
b = a.requisita_estados('sp')
writer.write_brStates(archive_name='sp', contain=b)


b = CovidMundo
d = b.requisita_paises('cuba')
writer.write_allCountries(contain=d)