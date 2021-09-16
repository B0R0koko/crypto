from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('styles.kv')

class MainLay(Widget):
    pass


class UserUI(App):
    def build(self):
        return MainLay()

if __name__ == "__main__":
    app = UserUI()
    app.run()






