import pandas as pd
import matplotlib.pyplot as plt


class MakeGraph:
    def processState(archive):
        df = pd.read_csv(archive)
        use_graph=list()
        for colunm_name in df.columns[3:7]:
            use_graph.append(colunm_name)

        for colunm in use_graph:
            # data
            df = df.sort_values(by=colunm, ascending=False).head(10)
            uf = df['UF'].values.tolist()
            dados = df[colunm].values.tolist()

            # graph details
            window = plt.figure(figsize=(15,10))
            plt.title(f'Os 10 estados com mais {colunm}', weight='bold', fontsize='30')
            plt.ylabel('Escala', weight='bold')
            plt.xticks(rotation=20)
            result = plt.bar(uf,dados, label=colunm, color='red')
            plt.bar_label(result, padding=2)
            plt.grid()
            plt.show()

            
    def processCountry(archive):
        df = pd.read_csv(archive)
        use_graph=list()
        for colunm_name in df.columns[1:3]:
            use_graph.append(colunm_name)

        for colunm in use_graph:
            # data
            df = df.sort_values(by=colunm, ascending=False).head(10)
            uf = df['País'].values.tolist()
            dados = df[colunm].values.tolist()

            # graph details
            window = plt.figure(figsize=(15,7))
            plt.title(f'Os 10 países com mais {colunm}', weight='bold', fontsize='30')
            plt.ylabel('Escala', weight='bold')
            plt.xticks(rotation=20)
            result = plt.bar(uf,dados, label=colunm, color='red')
            plt.bar_label(result, padding=2)
            plt.grid()
            plt.show()



