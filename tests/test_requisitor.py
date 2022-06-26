from CovidETL import CovidBrasil, CovidMundo, Check


class TestRequisitor:
    def test_retorno_api_status_on(self):
        assert Check.check_api()


    def test_retorno_api_status_off(self):
        url ='https://covid19-brazil-api.now.sh/api/status/v99'
        assert Check.check_api(url) == False


    def test_requisita_estados_tipo_instancia(self):
        estado = CovidBrasil()
        dado = CovidBrasil.requisita_estados()
        assert isinstance(estado, CovidBrasil)
        assert isinstance(dado, list)


    def test_requisita_pais_tipo_instancia(self):
        pais = CovidMundo()
        dado = CovidMundo.requisita_paises()
        assert isinstance(pais, CovidMundo)
        assert isinstance(dado, list)
