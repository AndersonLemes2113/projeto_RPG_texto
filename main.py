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

        self.button = Button(text='Iniciar Aventura!', size_hint=(0.5, 0.1),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_release=self.screen_change)
        self.rel_layout.add_widget(self.button)
        self.add_widget(self.rel_layout)

    def screen_change(self, instance):
        self.manager.current = "interactivescreen"


class TextsFound:
    def __init__(self, file):
        self.file = file

    def search_text(self):
        with open(self.file, 'r') as f:
            texts = [t.strip() for t in f.readlines() if t.strip()]

        return texts


class InteractiveScreen(Screen):
    def __init__(self, **kwargs):
        super(InteractiveScreen, self).__init__(**kwargs)
        self.name = "interactivescreen"
        self.show_text_onScreen()

    def show_text_onScreen(self):
        self.text_font = TextsFound('historia.txt')
        self.texts = self.text_font.search_text()
        self.text_label = Label(text='', halign='left')
        self.box_text = BoxLayout(orientation='vertical')
        self.limit_line = 50
        self.cont_limit = 0
        self.box_text.add_widget(self.text_label)
        self.add_widget(self.box_text)
        Clock.schedule_once(self.add_next_word, 1)  # Schedule adding the first word after 0.5 seconds

    def add_next_word(self, dt):
        title = self.texts[0]
        self.text = self.texts[1]

        def add_text(dt):
            if self.text_index < len(self.text):
                if self.cont_limit >= self.limit_line:
                    self.text_label.text += '\n'
                    self.cont_limit = 0
                self.text_label.text += self.text[self.text_index]
                self.text_index += 1
                self.cont_limit += 1
                Clock.schedule_once(add_text, 0.1)  # Agendar a adição da próxima letra após 0.1 segundos
            else:
                Clock.schedule_once(self.add_goodLuck, 2)  # Agendar a adição de "Boa Sorte" após 2 segundos
                Clock.schedule_once(self.add_button, 5)  # Agendar a adição do botão após 5 segundos

        self.text_index = 0  # Inicia o índice para adicionar o texto
        self.text_label.text = title + '\n'  # Adiciona o título diretamente
        Clock.schedule_once(add_text, 0.1)  # Inicia a adição do texto letra por letra após 0.1 segundos

    def add_goodLuck(self, dt):
        msg = "Boa Sorte na sua Jornada!"
        self.text_label.text += '\n'
        self.text_label.text += msg

    def add_button(self, dt):
        if not any(isinstance(child, Button) for child in self.box_text.children):
            button = Button(text="Clique aqui Para iniciar!", size_hint=(None, None), size=(200, 50),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
            self.box_text.add_widget(button)


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
