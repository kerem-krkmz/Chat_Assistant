import nltk
from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')


from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

from tkinter import Tk, Frame, Scrollbar, Listbox, RIGHT, Y, LEFT, BOTH, Entry, X, Button, END
from kivymd.uix.button import MDRectangleFlatButton
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

forgot = """
#:kivy 1.0
#:import APP_NAME config.APP_NAME
#:import COMPANY_NAME config.COMPANY_NAME
MDScreen:
    name: "forgot"
    MDLabel:
        text: APP_NAME
        halign: "center"
        pos_hint: {"center_y": .8}
        font_style: "H3"

    MDLabel:
        text: "Forgot Password"
        halign: "center"
        pos_hint: {"center_y":.73}
        font_style: "Subtitle2"

    MDTextField:
        hint_text: "Username or Email"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: .75,0.08
        # mode: "rectangle"

    MDRaisedButton:
        text: "Forgot Password"
        pos_hint: {"center_x": 0.5, "center_y":0.5}
        size_hint: .7,0.05
        on_release: app.change_screen("verification")

    MDTextButton:
        text: f"[color=#000000]Don't have an account?[/color] Sign up"
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.4}
        on_release: app.change_screen("signup")

    MDTextButton:
        text: f"[b][color=#000000]Back To[/color] Login[/b]"
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.33}
        on_release: app.change_screen("login")

    MDLabel:
        text: f"[font=Icons] {md_icons['copyright']}[/font]  [font=Roboto]{COMPANY_NAME} 2020[/font]"
        markup: True
        halign: "center"
        pos_hint: {"center_y":0.05}



"""

home = """
#:kivy 1.0
#:import APP_NAME config.APP_NAME
#:import COMPANY_NAME config.COMPANY_NAME
<Tabs>:
    BoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "You can start talking  by pressing the microphone button."
            halign: "center"
        
        MDBottomAppBar:
            MDToolbar:
                mode: "free-end" #free-end,end 
                type: "bottom"
                icon: "microphone-outline"
               
        
<Tabs2>:
    BoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "You can start  by pressing the text button."
            halign: "center"
        
        MDBottomAppBar:
            MDToolbar:
                mode: "free-end" #free-end,end 
                type: "bottom"
                icon: "comment-text-multiple-outline"
                on_action_button: app.write_chat()

MDScreen:
    name: "home"
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title: APP_NAME
        MDTabs:
            id: android_tabs

            Tabs:
                text: f"Voice Assistant"
            Tabs2:
                text: "Chat-Bot Assistant"
                font_style: 'Subtitle2'


"""

login = """
#:kivy 1.0
#:import APP_NAME config.APP_NAME
#:import COMPANY_NAME config.COMPANY_NAME
MDScreen:
    name: "login"

    MDLabel:
        text: APP_NAME
        halign: "center"
        pos_hint: {"center_y": .8}
        font_style: "H3"

    MDLabel:
        text: "Log in"
        halign: "center"
        pos_hint: {"center_y":.73}
        font_style: "Subtitle2"

    MDTextField:
        hint_text: "Username or Email"
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        size_hint: .75,0.085
        # mode: "rectangle"

    MDTextField:
        hint_text: "Password"
        pos_hint: {"center_x":0.5, "center_y":0.57}
        size_hint: .75,0.085
        password: True
        # mode: "rectangle"

    MDRaisedButton:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y":0.48}
        size_hint: .7,0.05
        on_release: app.change_screen("home")

    MDTextButton:
        text: "Forgot password?"
        pos_hint: {"center_x":0.5, "center_y":0.4}
        on_release: app.change_screen("forgot")

    MDTextButton:
        text: f"[color=#000000]Don't have an account?[/color] Sign up"
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.33}
        on_release: app.change_screen("signup")

    MDLabel:
        text: f"[font=Icons] {md_icons['copyright']}[/font]  [font=Roboto]{COMPANY_NAME} 2020[/font]"
        markup: True
        halign: "center"
        pos_hint: {"center_y":0.05}



"""

signup = """
#:kivy 1.0
#:import APP_NAME config.APP_NAME
#:import COMPANY_NAME config.COMPANY_NAME
MDScreen:
    name: "signup"
    MDLabel:
        text: APP_NAME
        halign: "center"
        pos_hint: {"center_y": .8}
        font_style: "H3"

    MDLabel:
        text: "Sign up"
        halign: "center"
        pos_hint: {"center_y":.73}
        font_style: "Subtitle2"

    MDTextField:
        hint_text: "Email"
        pos_hint: {"center_x": 0.5, "center_y": 0.65}
        size_hint: .75,0.08
        # mode: "rectangle"

    MDTextField:
        hint_text: "Fullname"
        pos_hint: {"center_x":0.5, "center_y":0.57}
        size_hint: .75,0.08
        # mode: "rectangle"

    MDTextField:
        hint_text: "Username"
        pos_hint: {"center_x":0.5, "center_y":0.49}
        size_hint: .75,0.08
        # mode: "rectangle"

    MDTextField:
        hint_text: "Password"
        pos_hint: {"center_x":0.5, "center_y":0.41}
        size_hint: .75,0.08
        password: True
        # mode: "rectangle"

    MDRaisedButton:
        text: "Sign up"
        pos_hint: {"center_x": 0.5, "center_y":0.31}
        size_hint: .7,0.05

    MDTextButton:
        text: f"[color=#000000]Have an account?[/color] Log in"
        markup: True
        pos_hint: {"center_x":0.5, "center_y":0.22}
        on_release: app.change_screen("login")

    MDLabel:
        text: f"[font=Icons] {md_icons['copyright']}[/font]  [font=Roboto]{COMPANY_NAME} 2020[/font]"
        markup: True
        halign: "center"
        pos_hint: {"center_y":0.05}



"""

verification = """
#:kivy 1.0
#:import APP_NAME config.APP_NAME
#:import COMPANY_NAME config.COMPANY_NAME
MDScreen:
    name: "verification"
    MDLabel:
        text: APP_NAME
        halign: "center"
        pos_hint: {"center_y": .8}
        font_style: "H3"

    MDLabel:
        text: "Account verification"
        halign: "center"
        pos_hint: {"center_y":.73}
        font_style: "Subtitle2"

    MDLabel:
        text: "We've sent a verification code to your email."
        halign: "center"
        pos_hint: {"center_y":.67}
        font_style: "Body2"

    MDTextField:
        hint_text: "Enter your verification Code"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: .75,0.08
        max_text_length: 6
        # mode: "rectangle"

    MDRaisedButton:
        text: "Submit"
        pos_hint: {"center_x": 0.5, "center_y":0.52}
        size_hint: .7,0.05

    MDTextButton:
        text: "Resend code"
        pos_hint: {"center_x": 0.5, "center_y":0.45}
        on_release: app.change_screen("verification")

    MDLabel:
        text: "Never share your verification code to anyone."
        halign: "center"
        pos_hint: {"center_y":.4}
        font_style: "Caption"

    MDLabel:
        text: f"[font=Icons] {md_icons['copyright']}[/font]  [font=Roboto]{COMPANY_NAME} 2020[/font]"
        markup: True
        halign: "center"
        pos_hint: {"center_y":0.05}
"""


class Tabs(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab on home screen'''


class Tabs2(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab on home screen'''


class PALDEMICApp(MDApp):
    def change_screen(self, name):
        screen_manager.current = name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_string(login))
        screen_manager.add_widget(Builder.load_string(signup))
        screen_manager.add_widget(Builder.load_string(forgot))
        screen_manager.add_widget(Builder.load_string(verification))
        screen_manager.add_widget(Builder.load_string(home))
        self.theme_cls.theme_style = "Light"

        return screen_manager

    def write_chat(self):
        bot = ChatBot("Pal Chatbot")

        convo = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome.",
            "What is your name",
            "My name is Pal what's your name?",
            "I'm glad."
        ]

        trainer = ListTrainer(bot)
        trainer.train(convo)

        main = Tk()
        main.geometry("500x650")
        main.title("paldemi chatbot")

        def ask_from_bot():
            query = textF.get()
            answer_from_bot = bot.get_response(query)
            msgs.insert(END, "You:" + query)
            print(type(answer_from_bot))
            msgs.insert(END, "Bot:" + str(answer_from_bot))
            textF.delete(0, END)

        frame = Frame(main)

        sc = Scrollbar(frame)
        msgs = Listbox(frame, width=80, height=20)

        sc.pack(side=RIGHT, fill=Y)
        msgs.pack(side=LEFT, fill=BOTH, pady=10)
        frame.pack()

        textF = Entry(main, font=("Verdana", 20))
        textF.pack(fill=X, pady=10)

        btn = Button(main, text="CHAT WITH BOT", font=("Verdana", 20), command=ask_from_bot)
        btn.pack()

        def enter_function(event):
            btn.invoke()

        main.bind("<Return>", enter_function)

        main.mainloop()


if __name__ == "__main__":
    PALDEMICApp().run()
