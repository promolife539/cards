from flask import Flask, render_template, request

my_flask_app = Flask(__name__)


@my_flask_app.route('/')
def index():
    return render_template('index.html', title="Карточки для изучения иностранного языка")


@my_flask_app.route('/new/')
def all_news():
    return render_template('new_card.html', title="Создание новой карточки", 
        nav_link_1="/cards/", nav_link_2="/training/", 
        nav_link_1_name="Все карточки", nav_link_2_name="Тренировка")


@my_flask_app.route('/cards/')
def all_cards():
    return render_template('all_cards.html', title="Все карточки", 
        nav_link_1="/new/", nav_link_2="/training/", 
        nav_link_1_name="Создание новой карточки", nav_link_2_name="Тренировка",
        cards = [1, 2, 3, 4, 5, 6, 7, {'name': 'HELLLO'}])


@my_flask_app.route('/training/')
def training():
    return render_template('training.html', title="Тренировка", 
        nav_link_1="/new/", nav_link_2="/cards/", 
        nav_link_1_name="Создание новой карточки", nav_link_2_name="Все карточки")       


if __name__ == "__main__":
    my_flask_app.run(debug=True)   