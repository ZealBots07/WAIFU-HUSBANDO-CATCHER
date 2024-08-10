class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6170772579"
    sudo_users = "6170772579", "6765826972"
    GROUP_ID = -1002133033983
    TOKEN = "7298455205:AAFUCtuFf2lTOJAXYcgL0tiXHDVglCKUp3s"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "zealanime_fun"
    UPDATE_CHAT = "zealanime_fun"
    BOT_USERNAME = "Husbando_zealBot"
    CHARA_CHANNEL_ID = "-1002133033983"
    api_id = 28408158
    api_hash = "ddda6703b42211276b28252aca309a2d"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
