from datetime import datetime


def sampleresponces(input_text):
    usermessage = str(input_text).lower()

    if usermessage in ("hello", "hi", "selam",):
        return "Hey! How's it going?"

    if usermessage in ("who are you", "who are you?",):
        return "i am koki's bot !"

    if usermessage in ("time", "time?", "what time is it now"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y , %H:%M:%S")

        return str(date_time)

    return "I don't understand you"
