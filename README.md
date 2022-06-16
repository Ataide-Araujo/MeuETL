Projeto Meu ETL do NAPP Academy (Em produção)
Gera um csv com alguns dados sobre a covid
para todos os estados brasileiros ou *todos os países
(cidade ou país, casos, mortes, atualizado em)

Como executar

- Clonar o projeto

# Criar um ambiente virtual
-python -m venv venv

# Instalar as libs necessárias
- pip install -r requirements.txt

# Help para ver os argumentos
- python -m CovidETL -h

# Executavel em linha de comando para estado
python -m CovidETL -estado

# Executavel em linha de comando para um país
python -m CovidETL -pais
