from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.uix.screenmanager import WipeTransition

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

class InteractiveScreen(Screen):
    def __init__(self,**kwargs):
        super(InteractiveScreen,self).__init__(**kwargs)
        self.name = "interactivescreen"

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

