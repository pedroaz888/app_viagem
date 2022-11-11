
def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino são iguais"""
    if origem == destino:
        lista_de_erros ['destino'] ='Origem e Destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se tem algum dígito"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo]="Não inclua números nesse campo"

def datas_conflitantes(data_ida, data_volta,data_pesquisa, lista_de_erros):
    """Verifica de data de ida é maior do que data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = "Datas conflitantes"
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = "Data ultrapassada"