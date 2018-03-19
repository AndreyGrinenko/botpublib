# Author: Andrei Grinenko <andrey.grinenko@gmail.com>
# License: BSD 3 clause

import sys
import datetime
import web3

TOKEN = '123456789:abcdefghijklmnopqrstuvwxyzABCDEFGHI'
REGISTER_TOKEN = '12:abcdef'

class HelloWorldMetaModel(object):
  def __init__(self):
    pass
  def predict(self, instance):
    if instance == '/start':
      return 'start'
    elif instance in ['hi', 'hello']:
      return 'hello'
    elif instance == 'how are you':
      return 'how_are_you'
    else:
      return 'unknown'

def generate_meta_model():
  return HelloWorldMetaModel()

def generate_response(instance, model, user_id, updating_data):
  current_datetime = updating_data['datetime']
  meaning = model.predict(instance)
  if meaning == 'start':
    reply = current_datetime + ': ' + 'I am habr example bot'
  elif meaning == 'hello':
    reply = current_datetime + ': ' + 'Hello, human!'
  elif meaning == 'how_are_you':
    reply = current_datetime + ': ' + 'I\'m fine, thanks!'
  else:
    reply = current_datetime + ': ' + 'Don\'t know yet'
  # TODO Add datetime
  return reply

def update_datetime():
  return str(datetime.datetime.now())

if __name__ == '__main__':
  web3.main_loop_webhooks(
                  generate_model_func=generate_meta_model,
                  generate_response_func=generate_response,
                  updates_settings={'frequency':datetime.timedelta(seconds=5),
                                    'data':{'datetime':update_datetime}},
                  list_of_sources=[{'node':'https://api.telegram.org/', 'id':{'token':TOKEN}},
                                   # {'node':'http://123.456.78.90/',
                                   #  'id':{'token':REGISTER_TOKEN}}
                                   ],
                  cash_file_name='./cash_file.txt',
                  log_file_name='./log.txt')

