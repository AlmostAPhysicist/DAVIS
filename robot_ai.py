import datetime
from text_to_speech_test import *
from random import choice


# text = ''


def respond_to_text(text):
    text = text
    answer = ''
    words_in_text = text.lower().split()
    if 'introduce' in words_in_text:
        text += ' hi name function'
    words_in_text = text.lower().split()
    
    greetings = ('hi', 'hello', 'hey', 'hey there')


    dob = datetime.date(2022, 10, 1)
    def age():
        present_date = datetime.date.today()
        return f'{(present_date - dob).days} days'
    # print(age())


    answer_book = {
        'name' : 'My name is DAVis. Thuh D A V robot. ',
        'age' : f'I am {age()} old. ',
        'old' : f'I am {age()} old. ',
        'creat' : 'I was created by 2 students of class 11, namely R yan and Jut in on October first, 2022. ',
        'creator' : 'I was created by 2 students of class 11, namely R yan and Jut in on October first, 2022. ',
        'made' : 'I was created by 2 students of class 11, namely R yan and Jut in on October first, 2022. ',
        # 'do' : 'I am a robot who moves and talks based on a voice command system.',
        'function' : 'I am a robot who moves and talks based on a voice command system. ',
        'purpose' : 'I am a robot who moves and talks based on a voice command system. ',
        'work' : 'I work based on the arduino chipset. ',
        'bye' : 'Goodbye, have a nice day.'
        # 'power'
    }


    if words_in_text[0] in ['hi', 'hello', 'hey', 'hai', 'hay']:
        answer += choice(greetings).title()
        answer += '! '
        if len(words_in_text) == 1:
            answer += answer_book['name']
            answer += 'How can I help you? '
    if 'nice' in words_in_text or 'good' in words_in_text:
        if 'meet' in words_in_text or 'talking' in words_in_text:
            answer += 'It was nice talking to you too!'
    else:
        # if words_in_text[0] in ['what', 'how', 'when']:
        for word in answer_book.keys():
            if word in words_in_text or (word + 'ed') in words_in_text or (word + 's') in words_in_text:
                answer += answer_book[word]
        
    if 'how do you do' in text or 'how are you' in text:
        answer += "I'm doing great! "
        answer += 'How are you doing? '
    if 'what do you do' in text:
        answer += answer_book['function']
    if 'today' in text:
        date = datetime.date.today().strftime('%d').lstrip('0') + 'of' + datetime.date.today().strftime('%B')
        day = datetime.date.today().strftime('%A')
        if 'date' in words_in_text:
            answer += f'It is {date} today. '
        elif 'day' in words_in_text:
            answer += f'It is {day} today. '
        
    if 'source' in words_in_text:
        if 'power' in words_in_text or 'powers' in words_in_text:
            answer += 'I am powered by DC batteries. '
    if 'introduce' in words_in_text:
        answer += 'How can I help you? '
            
            

    if 'self destruct' in text:
        play_on_device('Rickroll.wav')
    else:
        play_text(answer)


