from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock


class TextsFound:
    def __init__(self, file):
        self.file = file

    def search_text(self):
        with open(self.file, 'r') as f:
            texts = [t.strip() for t in f.readlines() if t.strip()]

        return texts


class InitialScreen(Screen):
    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)
        self.name = "initialscreen"
        self.rel_layout = RelativeLayout(size_hint=(1, 1))

        self.scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)

        texts = TextsFound('historia.txt')
        game_title = texts.search_text()[0]

        self.label = Label(text=f'{game_title}', font_size='20sp', size_hint_y=None, valign='top')

        self.scroll_view.add_widget(self.label)
        self.rel_layout.add_widget(self.scroll_view)

        self.button = Button(text='Iniciar Aventura!', size_hint=(0.5, 0.1),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_release=self.screen_change)
        self.rel_layout.add_widget(self.button)
        self.add_widget(self.rel_layout)

    def screen_change(self, instance):
        self.manager.current = "interactivescreen"


class InteractiveScreen(Screen):
    def __init__(self, **kwargs):
        super(InteractiveScreen, self).__init__(**kwargs)
        self.name = "interactivescreen"
        scroll_view = ScrollView()
        box_scroll = BoxLayout(orientation='vertical')
        button = Button(text='Iniciar game',on_release=self.start_game)
        button1 = Button(text='Continuar Game')
        button2 = Button(text='Configurações')
        box_scroll.add_widget(button)
        box_scroll.add_widget(button1)
        box_scroll.add_widget(button2)
        scroll_view.add_widget(box_scroll)
        self.add_widget(scroll_view)

    def start_game(self, instance):
        self.manager.current = 'screentextswrite'


class ScreenTextsWrite(Screen):
    def __init__(self, **kwargs):
        super(ScreenTextsWrite, self).__init__(**kwargs)
        self.name = 'screentextswrite'
        self.make_button()

    def make_button(self):
        self.button_start = Button(text='Iniciar a História',on_release=self.initialize_screen)
        self.add_widget(self.button_start)

    def initialize_screen(self,dt):
        self.remove_widget(self.button_start)
        self.cont_text = 1
        self.text_font = TextsFound('historia.txt')
        self.texts = self.text_font.search_text()

        self.scroll_view = ScrollView()
        self.text_label = Label(text='',font_size=15, halign='center', size_hint_y=None, valign='center',height=40)
        self.box_text = BoxLayout(orientation='vertical', size_hint_y=None)
        self.box_text.add_widget(self.text_label)
        self.box_text.bind(minimum_height=self.box_text.setter('height'))
        self.scroll_view.add_widget(self.box_text)
        self.add_widget(self.scroll_view)

        self.limit_line = 80
        self.cont_limit = 0
        Clock.schedule_once(self.add_next_word, 1)  # Schedule adding the first word after 0.5 seconds

    def add_next_word(self, dt):
        title = self.texts[0]
        self.text = self.texts[self.cont_text]

        def add_text(dt):
            if self.text_index < len(self.text):
                if self.cont_limit >= self.limit_line and self.text[self.text_index] == ' ':
                    self.make_label()
                    self.text_label.text += '\n'
                    self.cont_limit = 0
                self.text_label.text += self.text[self.text_index]
                self.text_index += 1
                self.cont_limit += 1
                Clock.schedule_once(add_text, 0.01)  # Schedule adding the next letter after 0.1 seconds
            else:
                Clock.schedule_once(self.add_goodLuck, 2)  # Schedule adding "Good Luck" after 2 seconds
                Clock.schedule_once(self.add_button, 5)  # Schedule adding the button after 5 seconds

        self.text_index = 0  # Start index to add text
        self.make_label()
        self.text_label.text = title + '\n'  # Add title directly
        Clock.schedule_once(add_text, 0.1)  # Start adding text letter by letter after 0.1 seconds

    def make_label(self,font_size=15,**kwargs):
        font = font_size
        label = Label(text='', font_size= 15,halign='center', size_hint_y=None, valign='center',height=40)
        self.box_text.add_widget(label)
        self.text_label = label
        font_size = 15

    def add_goodLuck(self, dt):
        msg = "Boa sorte na sua jornada!"
        self.make_label()
        self.text_label.text += '\n'
        self.text_label.text += msg

    def add_button(self, dt):
        if not any(isinstance(child, Button) for child in self.box_text.children):
            button = Button(text="Click here to start!", size_hint=(None, None), size=(200, 50),
                            pos_hint={'center_x': 0.5, 'center_y': 0.1})
            self.add_widget(button)

class RPGTextApp(App):
    def build(self):
        sm = ScreenManager()
        self.initial_screen = InitialScreen()
        self.interactive_screen = InteractiveScreen()
        self.screen_text_write = None  # Initial state, no ScreenTextsWrite instance created
        sm.add_widget(self.initial_screen)
        sm.add_widget(self.interactive_screen)
        return sm

    def on_start(self):
        # Create ScreenTextsWrite instance when the app starts
        self.screen_text_write = ScreenTextsWrite()
        self.root.add_widget(self.screen_text_write)

    def on_stop(self):
        # Remove ScreenTextsWrite instance when the app stops
        self.root.remove_widget(self.screen_text_write)


if __name__ == '__main__':
    RPGTextApp().run()
