from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
bot=ChatBot('Nova',read_only=True)#you can change the read_only to false if you want your bot to learn from the chatting experience.
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
