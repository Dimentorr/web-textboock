from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdjfowunecru093w8nrcmiw3rncow-38c0r0238'


# Изначально мы находимся на ведении
@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('main_page.html', title='Главная',
                           title_page='Введение')


@app.route('/ui', methods=['GET', 'POST'])
def ui():
    return render_template('ui.html', title="Пользовательский интерфейс",
                           title_page='Пользовательский интерфейс')


@app.route('/programs', methods=['GET', 'POST'])
def use_programs():
    return render_template('use_programs.html', title="Програмное обеспечение", title_page='Используемое ПО')


@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    return render_template('create_progect.html', title="Создание проекта", title_page='Создание игрового проекта')


@app.route('/import', methods=['GET', 'POST'])
def import_file():
    return render_template('import_file.html', title="Работа с файлами",
                           title_page='Работа с файлами', subtitle_page='Импорт файлов')


@app.route('/slice', methods=['GET', 'POST'])
def slice_sprites():
    return render_template('slise_sprite.html', title="Работа с файлами",
                           title_page='Работа с файлами', subtitle_page='Порезка спрайтов')


@app.route('/bd', methods=['GET', 'POST'])
def bd():
    return render_template('bd.html', title="Разработка игры",
                           title_page='Разработка игры', subtitle_page='База данных')


@app.route('/generate_cart', methods=['GET', 'POST'])
def generate_cart():
    return render_template('generate_cart.html', title="Разработка игры",
                           title_page='Разработка игры', subtitle_page='Генерация карты')


@app.route('/logic_enemies', methods=['GET', 'POST'])
def logic_enemies():
    return render_template('logic_enemies.html', title="Разработка игры",
                           title_page='Разработка игры', subtitle_page='Логика врагов')


@app.route('/placement_towers', methods=['GET', 'POST'])
def placement_towers():
    return render_template('placement_towers.html', title="Разработка игры",
                           title_page='Разработка игры', subtitle_page='Размещение башен')


@app.route('/logic_towers', methods=['GET', 'POST'])
def logic_towers():
    return render_template('logic_towers.html', title="Разработка игры",
                           title_page='Разработка игры', subtitle_page='Логика башен')


@app.route('/end', methods=['GET', 'POST'])
def end():
    return render_template('end.html', title="Условия окончания уровня", title_page='Разработка игры',
                           subtitle_page='Условия окончания уровня')


@app.route('/conclusion', methods=['GET', 'POST'])
def conclusion():
    return render_template('conclusion.html', title="Заключение", title_page='Заключение')


if True:
    app.run(port=8000, host='127.0.0.1', debug=True)
