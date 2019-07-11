from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
bot=ChatBot('Nova',read_only=True)
trainer=ChatterBotCorpusTrainer(bot)
trainer.train('C:/Users/Sharqua\Anaconda3\Lib\site-packages\chatterbot_corpus\data\english')
while True:
    user=input('You:')
    if user.strip() != 'bye':
        response=bot.get_response(user)
        print('Nova:',response)
    if user.strip() == 'bye':
        print('Nova:Signing off.')
        break
