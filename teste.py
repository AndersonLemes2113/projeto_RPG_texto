from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class ScrollView_class(Screen):
    def __init__(self,**kwargs):
        super(ScrollView_class, self).__init__(**kwargs)
        scrollView = ScrollView()
        box = BoxLayout(orientation='vertical', size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))
        for c in range(0, 50):
            label = Label(text='Olá, Mundo!', size_hint_y=None, height=100)
            box.add_widget(label)

        scrollView.add_widget(box)
        self.add_widget(scrollView)

class Meuapp(App):
    def build(self):
        return ScrollView_class()

if __name__ == '__main__':
    Meuapp().run()
