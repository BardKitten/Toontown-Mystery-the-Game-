from otp.chat import ChatGarbler
from toontown.toonbase import TTLocalizer

class ToonChatGarbler(ChatGarbler.ChatGarbler):

    def __init__(self):
        self.messages = {'dog': TTLocalizer.ChatGarblerDog,
         'cat': TTLocalizer.ChatGarblerCat,
         'mouse': TTLocalizer.ChatGarblerMouse,
         'horse': TTLocalizer.ChatGarblerHorse,
         'rabbit': TTLocalizer.ChatGarblerRabbit,
         'duck': TTLocalizer.ChatGarblerDuck,
         'monkey': TTLocalizer.ChatGarblerMonkey,
         'bear': TTLocalizer.ChatGarblerBear,
         'pig': TTLocalizer.ChatGarblerPig,
         'default': TTLocalizer.ChatGarblerDefault}
