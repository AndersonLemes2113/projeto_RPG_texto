from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.uix.screenmanager import WipeTransition
from kivy.clock import Clock

class InitialScreen(Screen):
    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)
        self.name = "initialscreen"
        self.rel_layout = RelativeLayout(size_hint=(1, 1))

        self.scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)

        self.label = Label(text='', font_size='20sp', size_hint_y=None, valign='top')

        self.scroll_view.add_widget(self.label)
        self.rel_layout.add_widget(self.scroll_view)

        self.button = Button(text='Iniciar Aventura!', size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_release=self.screen_change)
        self.rel_layout.add_widget(self.button)
        self.add_widget(self.rel_layout)

    def screen_change(self, instance):
        self.manager.current = "interactivescreen"

from kivy.clock import Clock

class InteractiveScreen(Screen):
    def __init__(self, **kwargs):
        super(InteractiveScreen, self).__init__(**kwargs)
        self.name = "interactivescreen"
        self.text_font = """O sombrio poder do jovem Malbordus está chegando a seu ápice. Os elfos que o criaram \natribuíram-lhe uma tarefa final: reaver os cinco artefatos do Dragão escondidos por séculos\n na cidade perdida de Vatos, em algum lugar no Deserto dos Crânios. Somente quando os tiver \nem seu poder ele será capaz e rebelar-se e submeter Allansia. Cada dia que passa o aproxima \nmais desse objetivo, e somente VOCÊ pode detê-lo!"""
        self.text_label = Label(text='', halign='center')
        box_text = BoxLayout(orientation='vertical')
        box_text.add_widget(self.text_label)
        self.add_widget(box_text)
        self.words = self.text_font.split()
        self.current_word_index = 0  # índice da palavra atual
        Clock.schedule_once(self.add_next_word, 0.5)  # agendar a adição da primeira palavra após 2 segundos
    
    def add_next_word(self, dt):
        if self.current_word_index < len(self.words):
            word = self.words[self.current_word_index]
            # Verifica se adicionar a palavra ultrapassa o limite de 50 caracteres por linha
            if len(self.text_label.text.split('\n')[-1]) + len(word) > 50:
                self.text_label.text += '\n'  # Adiciona uma nova linha
            self.text_label.text += word + ' '  # Adiciona a palavra
            self.current_word_index += 1
            Clock.schedule_once(self.add_next_word, 0.5)  # Agendar a adição da próxima palavra após 2 segundos

class RPGTextApp(App):
    def build(self):
        sm = ScreenManager(transition=WipeTransition())
        self.initial_screen = InitialScreen()
        self.interactive_screen = InteractiveScreen()
        sm.add_widget(self.initial_screen)
        sm.add_widget(self.interactive_screen)

        return sm

if __name__ == '__main__':
    app = RPGTextApp()
    app.run()


