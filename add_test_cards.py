from db import db_session, Card

cards = [
    {
        'en_meaning': 'Puppy',
        'ru_meaning': 'Щенок',
        'example': 'National charity, Hearing Dogs for Deaf People, which has a training centre at Cliffe, near Selby, is appealing for volunteers to take in puppies and young dogs for anything up to six weeks.',
        'extra_info': 'ˈpʌpi',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Squirrel',
        'ru_meaning': 'Белка',
        'example': 'Tree-dwelling squirrels have lovely bushy tails, and we realised that the little ones, from the look of them, were also from one such splendid family line.',
        'extra_info': 'ˈskwɪrəl',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Truck',
        'ru_meaning': 'Грузовик',
        'example': 'There will be classic and vintage cars, racing cars, go-carts, bikes, trucks , service vehicles and just about anything else with wheels.',
        'extra_info': 'trʌk',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Unjustified',
        'ru_meaning': 'Необоснованный, неоправданный',
        'example': 'Unjustified price increases.',
        'extra_info': 'ˌənˈjəstəˌfīd',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Impeachment',
        'ru_meaning': 'Импичмент, сомнение, обвинение',
        'example': '',
        'extra_info': '',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Train',
        'ru_meaning': 'Поезд',
        'example': 'A freight train.',
        'extra_info': '',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Wine',
        'ru_meaning': 'Вино',
        'example': 'He opened a bottle of red wine.',
        'extra_info': 'wīn',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Roomy',
        'ru_meaning': 'Вместительный, просторный',
        'example': 'The open-plan lounge and dining room offer bright and roomy accommodation.',
        'extra_info': 'ˈro͝omē,ˈro͞omē',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Props',
        'ru_meaning': 'Реквизит, бутафория',
        'example': 'Erika gets props for the great work she did on the music.',
        'extra_info': 'präps',
        'score': '0',
        'is_active': 1,
    },
    {
        'en_meaning': 'Rag',
        'ru_meaning': 'Тряпка',
        'example': 'He wiped his hands on an oily rag.',
        'extra_info': 'rag',
        'score': '0',
        'is_active': 1,
    }      
]

# в цикле создаём объект card, это объект класса Card
for c in cards:
    card = Card(c['en_meaning'], c['ru_meaning'], c['example'], c['extra_info'], c['score'], c['is_active'])
    db_session.add(card)

db_session.commit()
