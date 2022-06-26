from argparse import ArgumentParser

class TestArg:
    def test_type_options_help(self):
        parser = ArgumentParser()
        estado =parser.add_argument("-estado", help="Traz todos os estados do Brasil", action="store_true")
        pais = parser.add_argument("-pais", help="Traz todos os países do Mundo", action="store_true")
        assert isinstance(parser, ArgumentParser)
        assert estado.option_strings == ['-estado']
        assert estado.help == 'Traz todos os estados do Brasil'
        assert pais.option_strings == ['-pais']
        assert pais.help == 'Traz todos os países do Mundo'