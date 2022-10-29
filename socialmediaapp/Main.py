import Constants as keys
from telegram.ext import *
import Responces as R


print("Bot started ...")


def startcommand(update, context):
    update.message.reply_text("type something random to start")


def helpcommand(update, context):
    update.message.reply_text("if you need help try it on google")


def handlemessage(update, context):
    text = str(update.message.text).lower()
    response = R.sampleresponces(text)

    update.message.replytext(response)


def error(update, context):
    print(f"Update { update } caused error{context.error}")


def main():
    updater = Updater(keys.Apikey, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", startcommand))
    dp.add_handler(CommandHandler("help", helpcommand))

    dp.add_handler(MessageHandler(Filters.text, handlemessage))

    dp.add_error_handler(error)

    updater.start_polling(2)
    updater.idle()


main()
