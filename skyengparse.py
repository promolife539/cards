import requests
from db import db_session, Card

def skyeng_info(en_word):

    response = requests.get('http://dictionary.skyeng.ru/api/public/v1/words/search?search=' + en_word)
    word_info = response.json()

    new_card = None 
    
    for item in word_info:
        en_meaning = item.get('text')
        if en_word == en_meaning:
            a = 0
            noun = item.get('meanings')[a].get('partOfSpeechCode')
            if noun != 'n':
                a += 1
            ru_meaning = item.get('meanings')[a].get('translation').get('text')
            img_url = item.get('meanings')[a].get('imageUrl')
            extra_info = item.get('meanings')[a].get('transcription')
            new_card = {
                'en_meaning': en_meaning.capitalize(),
                'ru_meaning': ru_meaning.capitalize(),
                'extra_info': extra_info,
                'img_url': img_url,
            }


    return new_card

if __name__ == '__main__':
    print(skyeng_info(input('Введите слово: ')))
