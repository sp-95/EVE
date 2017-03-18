from wit import Wit
import uuid
from datetime import date, timedelta
from cStringIO import StringIO
import sys

import letter
import mailing
import note


WIT_AI_TOKEN = 'RKQDGHZBNPMYBX5Q3MAVVQNK3WHIGEXM'


def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def send(request, response):
    print(response['text'])

def get_date(request):
    context = request['context']
    entities = request['entities']

    day = first_entity_value(entities, 'day')
    if day == 'yesterday':
        context['date'] = '{:%B %d %Y}'.format(date.today() - timedelta(1))
    elif day == 'tomorrow':
        context['date'] = '{:%B %d %Y}'.format(date.today() + timedelta(1))
    else:
        context['date'] = '{:%B %d %Y}'.format(date.today())
    return context

def gen_letter(request):
    context = request['context']
    old_stdout = sys.stdout
    sys.stdout = sys.__stdout__
    context['file'] = letter.main()
    sys.stdout = old_stdout
    return context

def send_mail(request):
    context = request['context']
    old_stdout = sys.stdout
    sys.stdout = sys.__stdout__
    context['status'] = mailing.main()
    sys.stdout = old_stdout
    return context

def take_note(request):
    context = request['context']
    note.main()
    return context

actions = {
    'send': send,
    'getDate': get_date,
    'genLetter': gen_letter,
    'sendMail': send_mail,
    'takeNote': take_note,
}

client = Wit(access_token=WIT_AI_TOKEN, actions=actions)

def chat(message):
    session_id = uuid.uuid1()

    sys.stdout = mystdout = StringIO()
    context = client.run_actions(session_id, message)
    sys.stdout = sys.__stdout__
    return mystdout.getvalue().rstrip('\n')


def main():
    message = raw_input("Enter a message: ")
    print(chat(message))

if __name__ == '__main__':
    main()