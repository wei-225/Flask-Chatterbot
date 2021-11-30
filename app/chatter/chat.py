from app import app
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = None
language_setting = "english"
support_languages = {"english", "chinese"}


def set_bot(language):
    global bot
    global language_setting

    assert language in support_languages
    if language != language_setting:
        language_setting = language

        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train("chatterbot.corpus.{}".format(language_setting))

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

        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train("chatterbot.corpus.{}".format(language_setting))

        app.logger.info("Bot is ready")

    return bot
