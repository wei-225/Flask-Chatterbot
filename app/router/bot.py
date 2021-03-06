from app import app
from app.chatter import chat
from flask import request


@app.route("/set_language", methods=["POST", "GET"])
def set_language():
    language = request.values.get("language")
    chat.set_bot(language)


@app.route("/response", methods=["POST", "GET"])
def response():
    chatbot = chat.get_bot()
    text = request.values.get("msg")
    return str(chatbot.get_response(text))
