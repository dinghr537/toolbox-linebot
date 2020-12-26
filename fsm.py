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
    url = 'https://i.imgur.com/B8Y06MV.jpg'
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
        msg = "Now please input any texts and it will be translated to english.\nType 'exit!!' to exit."
        send_text_message(reply_token, msg)
        # self.go_back()

    def on_exit_transToEnglish(self):
        print("Leaving transToEnglish")

    def on_enter_transToMandarin(self, event):
        print("I'm entering transToMandarin")
        reply_token = event.reply_token
        msg = "Now please input any texts and it will be translated to Mandarin.\nType 'exit!!' to exit."
        send_text_message(reply_token, msg)
        # self.go_back()

    def on_enter_metaphysics(self, event):
        print("I'm entering metaphysics")
        reply_token = event.reply_token
        msg = "Now please input any texts that describes what you want to do and I will give you my advice.\nType 'exit!!' to exit."
        send_text_message(reply_token, msg)
        # self.go_back()

    def on_enter_latex(self, event):
        print("I'm entering latex")
        reply_token = event.reply_token
        msg = "Now please input a Mathematical formula.\nType 'exit!!' to exit."
        send_text_message(reply_token, msg)
        
        # self.go_back()

    def on_exit_transToMandarin(self):
        print("Leaving transToMandarin")




