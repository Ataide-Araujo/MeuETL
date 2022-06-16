from argparse import ArgumentParser

class Args():
    def args_params():
        parser = ArgumentParser()
        parser.add_argument("-estado","--estado", help="Informe a sigla do estado", type=str)
        parser.add_argument("-pais","--pais", help="Informe o nome do país", type=str)
        parser.add_argument("--all", help="Pega todos os países da lista", action="store_true")
        args = parser.parse_args()
        return args
