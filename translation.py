class Translation(object):
    START_TEXT = """<b>Hello 👋, This Is An 𝗔𝗣𝗜 𝗜𝗗 & 𝗛𝗔𝗦𝗛 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 𝗕𝗢𝗧,\n\nI Can Help You Get Your Telegram API ID & HASH, Make Sure You Read Terms & Conditions Of Running This Bot.\n\nEnter Your Telegram Number To Get Thr APP-ID From my.telegram.org\n\nPress /start At Any Stage To Re-Enter Your Details</b>"""
    AFTER_RECVD_CODE_TEXT = """I see!
now please send the Telegram code that you received from Telegram!

this code is only used for the purpose of getting the APP ID from my.telegram.org

/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@SpEcHlDe"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
