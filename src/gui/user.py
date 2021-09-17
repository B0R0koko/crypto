from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder
from src.utils.keysgenerator import PrivateKeyGenerator, PublicKeyGenerator

Builder.load_file('src/gui/styles.kv')

class MainLay(Widget):
    
    def generate_address(self, path):
        if path == '':
            self.ids.generated_address.text = 'Empty address'
            return
        private_key = PrivateKeyGenerator.generate_from_png(path)
        public_key = PublicKeyGenerator().generate_key(private_key)
        private_key = str(hex(private_key))
        public_key = str(hex(public_key[0]))
        self.ids.generated_address.text = f'Private Address: {private_key}\nPublic Address: {public_key}'
        return
        

class UserUI(App):
    def build(self):
        return MainLay()

if __name__ == "__main__":
    app = UserUI()
    app.run()