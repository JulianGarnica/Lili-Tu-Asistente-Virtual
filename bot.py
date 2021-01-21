from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Lili')

# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.spanish")

def chatbot_response(usuario):
    respuesta = chatbot.get_response(usuario)
    return str(respuesta)