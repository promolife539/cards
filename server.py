from flask import Flask, render_template, request, redirect, url_for
import db
from skyengparse import skyeng_info

my_flask_app = Flask(__name__)


# Главная страница
@my_flask_app.route('/')
def index():
    return render_template(
        'index.html', title="Карточки для изучения иностранного языка"
        )


def create_or_update_card(en_meaning, ru_meaning, example, extra_info):
    # Сохраняем в базу
    new_card=db.Card(en_meaning, ru_meaning, example, extra_info, 'true')
    db.db_session.add(new_card)
    db.db_session.commit()


# Страница создания новой карточки
@my_flask_app.route('/new/', methods=['GET', 'POST'])
def new_card():

    if request.method == 'POST':
        # Добавление в базу новой карточки
        # Получаем данные из полей формы
        en_meaning = str(request.form.get('en_meaning'))
        ru_meaning = str(request.form.get('ru_meaning'))
        example = str(request.form.get('example'))
        extra_info = str(request.form.get('extra_info'))

        word_data = skyeng_info(en_meaning)
        if word_data:
            ru_meaning = ru_meaning if ru_meaning else word_data['ru_meaning']
            extra_info = extra_info if extra_info else word_data['extra_info']

        create_or_update_card(en_meaning, ru_meaning, example, extra_info)

        # После отправки формы показываем листинг всех карточек
        return redirect(url_for('all_cards'))

    return render_template(
        'new_card.html', title="Создание новой карточки", 
        nav_link_1=url_for('all_cards'), nav_link_2="/training/", 
        nav_link_1_name="Все карточки", nav_link_2_name="Тренировка"
        )


# Страница редактирования карточки, должна принимать id через URL
@my_flask_app.route('/card/<int:card_id>/edit')
def edit_card(card_id):
    return render_template(
        'card.html', title="Редактирование карточки", 
        nav_link_1="/cards/", nav_link_2="/training/", 
        nav_link_1_name="Все карточки", nav_link_2_name="Тренировка",
        #TODO приём параметра через URL
        card=db.db_session.query(db.Card).get(card_id)
        )  


# Листинг всех карточек
@my_flask_app.route('/cards/', methods=['GET', 'DELETE'])
def all_cards():
    print(db.db_session.query(db.Card))
    return render_template(
        'all_cards.html', title="Все карточки", 
        nav_link_1="/new/", nav_link_2="/training/", 
        nav_link_1_name="Создание новой карточки", nav_link_2_name="Тренировка",
        cards=db.db_session.query(db.Card).all()
        )


# Страница тренировки
@my_flask_app.route('/training/')
def training():
    return render_template(
        'training.html', title="Тренировка", 
        nav_link_1="/new/", nav_link_2="/cards/", 
        nav_link_1_name="Создание новой карточки", nav_link_2_name="Все карточки"
        )       


if __name__ == "__main__":
    my_flask_app.run(debug=True)   