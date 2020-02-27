# from chatterbot import ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
import logging

bot = ChatBot(
  'Default responses chat bot',
  storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
  logic_adapters = [
    {
      'import_path': 'chatterbot.logic.BestMatch',
      'default_response': "Sorry, but I don't know the answer yet. D:",
      'maximum_similarity_threshold': 0.90
    }
  ],
  filters = [
    'chatterbot.filters.RepetitiveResponseFilter'
  ],
  database = './chatterbot-database'
)

# CONVERSATION_ID = bot.storage.create('wilhem_dy_')

def get_feedback():
  text = input()

  if 'y' in text.lower():
    return True
  elif 'n' in text.lower():
    return False
  else:
    print("Assuming no... D:")
    return False

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)
# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")
print("Read only bot = ", bot.read_only)

print('You can always press ctrl + c for exit.')
print("Type something to beign")

while True:
  try:
    input_statement = Statement(text=input())
    response = bot.generate_response(
        input_statement
    )
    print('\n Is "{}" a coherent response to "{}"? \n'.format(
        response.text,
        input_statement.text
    ))
    if get_feedback() is False:
      print('I would like that you teach me the right answer!')
      correct_response = Statement(text=input())
      bot.learn_response(correct_response, input_statement)
      response = correct_response
      print('Thanks! I will renember that.')
    
    print(response)

  except (KeyboardInterrupt, EOFError, SystemExit):
    break
