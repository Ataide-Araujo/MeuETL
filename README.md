Projeto Meu ETL do NAPP Academy (Em produção)
Gera um csv com alguns dados sobre a covid
(cidade ou país, casos, mortes, atualizado em)

Como executar

- Clonar o projeto

# Criar um ambiente virtual
-python -m venv venv

# Instalar as libs necessárias
- pip install -r requeriments.txt

# Help para ver os argumentos
- python -m CovidETL -h

# Executavel em linha de comando para estado
python -m CovidETL -estado 'sigla do estado'

# Executavel em linha de comando para um país
python -m CovidETL -pais 'nome do país'

# Executável em linha de comando para *todos os países
Python -m CovidETL --all
