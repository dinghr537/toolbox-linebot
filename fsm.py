from transitions.extensions import GraphMachine
from utils import send_text_message
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction
from utils import send_text_message, send_button_message, send_image_message

def choose_dest_languages(reply_token):
    title = "再問你一個問題～"
    text = '翻譯成啥？'
    btn = [
        MessageTemplateAction(
            label = '英文',
            text ='trans to en'
        ),
        MessageTemplateAction(
            label = '中文',
            text = 'trans to zh'
        ),
        MessageTemplateAction(
            label = '俄文',
            text = 'trans to ru'
        ),
        MessageTemplateAction(
            label = '退出',
            text = 'exit!!'
        )
    ]
    url = 'https://i.imgur.com/sOMIYvL.png'
    send_button_message(reply_token, title, text, btn, url)

def ready_to_translate(language, reply_token):
    title = "Type something!"
    text = f"It will be translated to {language}."
    btn = [
        MessageTemplateAction(
            label = '退出',
            text ='exit!!'
        )
    ]
    url = 'https://i.imgur.com/9zJe9mt.png'
    send_button_message(reply_token, title, text, btn, url)

def ready_to_play(reply_token):
    title = "Type something!"
    text = f"玄學時間到了～"
    btn = [
        MessageTemplateAction(
            label = '退出',
            text ='exit!!'
        )
    ]
    url = 'https://i.imgur.com/8rOFegT.png'
    send_button_message(reply_token, title, text, btn, url)

def ready_for_latex(reply_token):
    title = "Type something!"
    text = f"LaTeX is coming!!!"
    btn = [
        MessageTemplateAction(
            label = '退出',
            text ='exit!!'
        )
    ]
    url = 'https://i.imgur.com/slxN5o9.png'
    send_button_message(reply_token, title, text, btn, url)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_translate(self, event):
        text = event.message.text
        return text.lower() == "translate"

    def is_going_to_transToEnglish(self, event):
        text = event.message.text
        return text.lower() == "trans to en"

    def is_going_to_transToMandarin(self, event):
        text = event.message.text
        return text.lower() == "trans to zh"

    def is_going_to_transToRussian(self, event):
        text = event.message.text
        return text.lower() == "trans to ru"

    def is_going_to_metaphysics(self, event):
        text = event.message.text
        return text.lower() == "metaphysics"

    def is_going_to_latex(self, event):
        text = event.message.text
        return text.lower() == "latex"

    def on_enter_translate(self, event):
        print("I'm entering translate")

        reply_token = event.reply_token
        # msg = "Now please choose your dest language\nType 'exit!!' to exit."
        choose_dest_languages(reply_token)

    def on_enter_transToEnglish(self, event):
        print("I'm entering transToEnglish")

        reply_token = event.reply_token
        ready_to_translate("English", reply_token)
        #msg = "Now please input any texts and it will be translated to english.\nType 'exit!!' to exit."
        #send_text_message(reply_token, msg)
        # self.go_back()

    def on_exit_transToEnglish(self):
        print("Leaving transToEnglish")

    def on_enter_transToMandarin(self, event):
        print("I'm entering transToMandarin")
        reply_token = event.reply_token
        ready_to_translate("Mandarin", reply_token)
        # self.go_back()

    def on_enter_transToRussian(self, event):
        print("I'm entering transToRussian")
        reply_token = event.reply_token
        ready_to_translate("Russian", reply_token)
        # self.go_back()

    def on_enter_metaphysics(self, event):
        print("I'm entering metaphysics")
        reply_token = event.reply_token
        ready_to_play(reply_token)
        # self.go_back()

    def on_enter_latex(self, event):
        print("I'm entering latex")
        reply_token = event.reply_token
        ready_for_latex(reply_token)
        
        # self.go_back()

    def on_exit_transToMandarin(self):
        print("Leaving transToMandarin")




