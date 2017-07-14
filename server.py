from flask import Flask, render_template, request
import db

my_flask_app = Flask(__name__)


@my_flask_app.route('/')
def index():
    return render_template(
        'index.html', title="Карточки для изучения иностранного языка"
        )


@my_flask_app.route('/new/', methods=['GET', 'POST'])
def new_card():

    if request.method == 'POST':
        # Добавление в базу новой карточки
        # Получаем данные из полей формы
        en_meaning = str(request.form.get('en_meaning'))
        ru_meaning = str(request.form.get('ru_meaning'))
        example = str(request.form.get('example'))
        extra_info = str(request.form.get('extra_info'))

        # Сохраняем в базу
        new_card=db.Card(en_meaning, ru_meaning, example, extra_info)
        db.db_session.add(new_card)
        db.db_session.commit() 


        return str(request.form.get('en_meaning'))

    return render_template(
        'new_card.html', title="Создание новой карточки", 
        nav_link_1="/cards/", nav_link_2="/training/", 
        nav_link_1_name="Все карточки", nav_link_2_name="Тренировка"
        )


@my_flask_app.route('/cards/')
def all_cards():
    return render_template(
        'all_cards.html', title="Все карточки", 
        nav_link_1="/new/", nav_link_2="/training/", 
        nav_link_1_name="Создание новой карточки", nav_link_2_name="Тренировка",
        cards = db.db_session.query(db.Card).all()
        )


@my_flask_app.route('/training/')
def training():
    return render_template(
        'training.html', title="Тренировка", 
        nav_link_1="/new/", nav_link_2="/cards/", 
        nav_link_1_name="Создание новой карточки", nav_link_2_name="Все карточки"
        )       


if __name__ == "__main__":
    my_flask_app.run(debug=True)   