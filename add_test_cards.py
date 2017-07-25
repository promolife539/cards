from db import db_session, Card

cards = [
    {
        'en_meaning': 'Puppy',
        'ru_meaning': 'Щенок',
        'example': 'National charity, Hearing Dogs for Deaf People, which has a training centre at Cliffe, near Selby, is appealing for volunteers to take in puppies and young dogs for anything up to six weeks.',
        'extra_info':'ˈpʌpi',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Squirrel',
        'ru_meaning': 'Белка',
        'example': 'Tree-dwelling squirrels have lovely bushy tails, and we realised that the little ones, from the look of them, were also from one such splendid family line.',
        'extra_info':'ˈskwɪrəl',
        'score': '1',
        'is_active': 1,
    },
    {
        'en_meaning': 'Truck',
        'ru_meaning': 'Грузовик',
        'example': 'There will be classic and vintage cars, racing cars, go-carts, bikes, trucks , service vehicles and just about anything else with wheels.',
        'extra_info':'trʌk',
        'score': '2',
        'is_active': 1,
    }      
]

# в цикле создаём объект card, это объект класса Card
for c in cards:
    card = Card(c['en_meaning'], c['ru_meaning'], c['example'], c['extra_info'], c['score'], c['is_active'])
    db_session.add(card)

db_session.commit()