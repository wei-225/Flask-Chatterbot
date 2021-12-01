import ssl
from app import app
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, UbuntuCorpusTrainer

bot = None
language_setting = "chinese"
support_languages = {"english", "chinese", "ubuntu"}


def disable_ssl():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context


def train_bot():
    global bot
    global language_setting

    if language_setting == "ubuntu":
        trainer = UbuntuCorpusTrainer(bot)
        trainer.train()
    else:
        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train("chatterbot.corpus.{}".format(language_setting))


def set_bot(language):
    global bot
    global language_setting

    assert language in support_languages
    if language != language_setting:
        language_setting = language

        disable_ssl()

        train_bot()

    app.logger.info("Bot set to {}".format(language_setting))


def get_bot():
    global bot
    global language_setting

    if not bot:
        bot = ChatBot(
            "WebBot",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=[
                "chatterbot.logic.MathematicalEvaluation",
                # "chatterbot.logic.TimeLogicAdapter",
                "chatterbot.logic.BestMatch",
            ],
        )

        disable_ssl()

        train_bot()

        app.logger.info("Bot is ready")

    return bot
