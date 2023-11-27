from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


class TelaInicial(Screen):
    def __init__(self,**kwargs):
        super(TelaInicial,self).__init__(**kwargs)
        self.box = BoxLayout(orientation='horizontal')
        self.button = Button(text='Iniciar Aventura!',on_release=self.adicionar_label)
        self.box.add_widget(self.button)
        self.add_widget(self.box)
    
    def adicionar_label(self,instancia):
        texto = ''' Pronto para iniciar uma aventura nesse mundo onde todo seu sucesso só depende das suas escolhas?\nAqui nesse mundo você irá ver o benefício do esforço e da perseverança. Aqui nada lhe será dado, \nporém seu esforço lhe dará os resultados procurados! \nAqui você irá reviver o seu dom da leitura. Aqui você aprender a dominar \ndons que nem sabia que estavam dormentes em você.'''
        
        self.caracteres = texto

        self.box.remove_widget(self.button)
        self.label = Label(text=f"{texto}")
        self.box.add_widget(self.label)
        

class Gerenciador(ScreenManager):
    def __init__(self,**kwargs):
        super(Gerenciador,self).__init__(**kwargs)
        self.tela_inicial = TelaInicial()
        self.add_widget(self.tela_inicial)
    

class RPG_Texto(App):
    def build(self):
        return Gerenciador()


if __name__ == '__main__': 
    aplicação = RPG_Texto()
    aplicação.run()

