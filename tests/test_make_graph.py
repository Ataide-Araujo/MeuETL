from CovidETL import MakeGraph
import pytest


class TestMakeGraph:
    def test_tipo_instancia(self):
        instanced=MakeGraph()
        assert isinstance(instanced, MakeGraph)
    

    def test_faltando_parametro_stado(self):
        msg = 'File name must be string!'
        with pytest.raises(TypeError) as error:
            MakeGraph.processState()
        assert str(error.value) == msg


    def test_erro_parametro_int_stado(self):
        msg = 'File name must be string!'
        with pytest.raises(ValueError) as error:
            MakeGraph.processState(1)
        assert str(error.value) == msg


    def test_faltando_parametro_pais(self):
        msg = 'File name must be string!'
        with pytest.raises(TypeError) as error:
            MakeGraph.processCountry()
        assert str(error.value) == msg


    def test_erro_parametro_int_pais(self):
        msg = 'File name must be string!'
        with pytest.raises(ValueError) as error:
            MakeGraph.processCountry(2)
        assert str(error.value) == msg