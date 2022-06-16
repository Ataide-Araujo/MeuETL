from argparse import ArgumentParser

class Args():
    def args_params():
        parser = ArgumentParser()
        parser.add_argument("-estado", help="Traz todos os estados do Brasil", action="store_true")
        parser.add_argument("-pais", help="Traz todos os países do Mundo", action="store_true")
        args = parser.parse_args()
        return args
