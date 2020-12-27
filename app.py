# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from flask import send_from_directory
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction
from utils import send_text_message, send_button_message, send_image_message
from google.cloud import translate_v2 as translate
import html
import random
from sympy import preview

from fsm import TocMachine
from utils import send_text_message

load_dotenv()
translate_client = translate.Client()

URL = "https://hrworld.monster:8000"

metaphysics_results = ["尚可", "大吉", "挺不錯的", "可以考慮", "這好嗎？這不好！", "小吉", "凶", "大凶", "你瘋了？", "這種事就隨便啦", "可惜天機不可洩漏"]

machine = TocMachine(
    states=["user", "translate", "transToEnglish", "transToMandarin", "transToRussian", "metaphysics", "latex"],
    transitions=[
        {
            "trigger": "advance",
            "source": "translate",
            "dest": "transToEnglish",
            "conditions": "is_going_to_transToEnglish",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "translate",
            "conditions": "is_going_to_translate",
        },
        {
            "trigger": "advance",
            "source": "translate",
            "dest": "transToMandarin",
            "conditions": "is_going_to_transToMandarin",
        },
        {
            "trigger": "advance",
            "source": "translate",
            "dest": "transToRussian",
            "conditions": "is_going_to_transToRussian",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "metaphysics",
            "conditions": "is_going_to_metaphysics",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "latex",
            "conditions": "is_going_to_latex",
        },
        {"trigger": "go_back", "source": ["transToEnglish", "transToMandarin", "transToRussian", "translate", "metaphysics", "latex"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

def welcome_with_different_title(title, event):
    text = '啥事？'
    btn = [
        MessageTemplateAction(
            label = '翻譯',
            text ='translate'
        ),
        MessageTemplateAction(
            label = '玄學時間',
            text = 'metaphysics'
        ),
        MessageTemplateAction(
            label = '生成latex圖片',
            text = 'latex'
        ),
    ]
    url = 'https://i.imgur.com/B8Y06MV.jpg'
    # print(f"event.reply_token: {event.reply_token}")
    send_button_message(event.reply_token, title, text, btn, url)


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # print("=========\n events:\n")
    # print(events)
    # print(body)
    # print("============ finish \n")
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        if event.message.text.lower() == 'fsm':
            send_image_message(event.reply_token, URL + '/show-fsm')
            continue
        elif machine.state == "translate":
            if event.message.text == "exit!!":
                machine.go_back()
                welcome_with_different_title('Welcome Back!', event)
                continue
            response = machine.advance(event)
            if response == False:
                send_text_message(event.reply_token, "Invalid input, try again please!")
            continue
        elif machine.state == "transToEnglish":
            if event.message.text == "exit!!":
                machine.go_back()
                welcome_with_different_title('Welcome Back!', event)
                continue
            target = 'en'
            result = translate_client.translate(event.message.text, target_language=target)
            send_text_message(event.reply_token, html.unescape(result["translatedText"]))
            continue
        elif machine.state == "transToMandarin":
            if event.message.text == "exit!!":
                machine.go_back()
                welcome_with_different_title('Welcome Back!', event)
                continue
            target = 'zh_TW'
            result = translate_client.translate(event.message.text, target_language=target)
            send_text_message(event.reply_token, html.unescape(result["translatedText"]))
            continue
        elif machine.state == "transToRussian":
            if event.message.text == "exit!!":
                machine.go_back()
                welcome_with_different_title('Welcome Back!', event)
                continue
            target = 'ru'
            result = translate_client.translate(event.message.text, target_language=target)
            send_text_message(event.reply_token, html.unescape(result["translatedText"]))
            continue
        elif machine.state == "metaphysics":
            if event.message.text == "exit!!":
                machine.go_back()
                welcome_with_different_title('Welcome Back!', event)
                continue
            result = metaphysics_results[random.randint(0,len(metaphysics_results)-1)]
            send_text_message(event.reply_token, result)
            continue
        elif machine.state == "latex":
            if event.message.text == "exit!!":
                machine.go_back()
                welcome_with_different_title('Welcome Back!', event)
                continue
            formula = r"$$" + event.message.text + r"$$"
            preview(formula, viewer='file', filename='test.png', dvioptions=['-D','1200'])
            url = "test.png"
            send_image_message(event.reply_token, URL + '/test.png')
            continue
        response = machine.advance(event)
        if response == False:
            title = '請先選擇要使用的功能'    
            welcome_with_different_title(title, event)
            # send_button_message(event.reply_token, title, text, btn, url)
            # send_text_message(event.reply_token, "Try again")

        # send_text_message(event.reply_token, "what's up")
    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

@app.route("/test.png", methods=["GET"])
def show_latex():
    return send_file("test.png", mimetype="image/png")

# @app.route('/test.png', methods=['GET', 'POST'])
# def download():
#     uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
#     return send_from_directory(directory="./", filename="test.png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, ssl_context=('/usr/local/etc/trojan/cert.crt', '/usr/local/etc/trojan/private.key'))
