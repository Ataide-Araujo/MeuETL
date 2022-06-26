Projeto Meu ETL do NAPP Academy (Em produção)
Gera um csv/gráfico com alguns dados sobre a covid
(de acordo com a API)para todos os
estados brasileiros (Casos confirmados, Mortes, Suspeitos,	Negativados)
ou *todos os países (Casos confirmados, mortes)

Como executar

# Clonar o projeto
- git clone https://github.com/Ataide-Araujo/MeuETL.git

# Instalar a lib utilizada para a máquina virtual
pip install virtualenv

# Abrir o terminal na pasta root onde foi clonado o projeto (a venv ficará ao lado da pasta MeuETL)
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate  (Linux ou macOS)

venv/Scripts/activate.bat  (Windows)

# Instalar as libs necessárias
pip install -r requirements.txt

# Help para ver os argumentos
python -m CovidETL -h

# Executavel em linha de comando para estado
python -m CovidETL -estado

# Executavel em linha de comando para um país
python -m CovidETL -pais
