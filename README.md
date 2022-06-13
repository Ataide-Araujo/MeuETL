Projeto Meu ETL do NAPP Academy (Em produção)

Como executar:

- Clonar o projeto

# Criar um ambiente virtual
-python -m venv venv

# Instalar as libs necessárias
- pip install -r requeriments.txt

# Help para ver os argumentos
- python -m CovidETL -h

# Executavel em linha de comando para estado
python -m CovidETL -estado 'sigla do estado'

ou

# Executavel em linha de comando para país
python -m CovidETL -pais 'nome do país'
