Projeto Meu ETL do NAPP Academy (Em produção)
Gera um csv/gráfico com alguns dados sobre a covid
(de acordo com a API)para todos os
estados brasileiros (Casos confirmados, Mortes, Suspeitos,	Negativados)
ou *todos os países (Casos confirmados, mortes)

Como executar

- Clonar o projeto

# Criar um ambiente virtual
python -m venv venv

# Instalar as libs necessárias
pip install -r requirements.txt

# Help para ver os argumentos
python -m CovidETL -h

# Executavel em linha de comando para estado
python -m CovidETL -estado

# Executavel em linha de comando para um país
python -m CovidETL -pais
