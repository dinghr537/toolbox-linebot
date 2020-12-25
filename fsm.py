from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

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
