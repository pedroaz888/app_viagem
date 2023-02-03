from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label="Data da pesquisa", disabled=True, initial=datetime.today())
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'data_ida': 'Data de ida', 'data_volta': 'Data da volta',  'informacoes':'Informações extra',
                  'classe_viagem':'Classe do vôo'}
        widgets = {
            'data_ida' : DatePicker(),
            'data_volta' : DatePicker()

        }

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros= {}
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        datas_conflitantes(data_ida, data_volta,data_pesquisa, lista_de_erros)

        if lista_de_erros is not None:
            for error in lista_de_erros:
                mensagem_erro = lista_de_erros[error]
                self.add_error(error, mensagem_erro)

        return self.cleaned_data

class PessoasForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['email','nome']
