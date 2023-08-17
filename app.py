from flask import Flask, render_template, request, url_for, redirect, flash
from form.forms import MoveForm
from game_logic import Game


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


@app.route('/')
def index():
    Game(2, 0)
    return render_template('index.html')


@app.route('/game/<current_room>', methods=['GET', 'POST'])
def game(current_room):
    form = MoveForm()
    game = Game()
    if current_room == 'Подземелье':
        flash('Вчерашний поход к барону явно удался. Сейчас вы в пыльной непонятной комнате и Ваше самочуствие после '
              'бурной ночи оставляет желать лучшего. Глоток свежего воздуха - вот лучшее решение. Пора пробираться ' 
              'к балкону', category='primary')
    if request.method == 'POST':
        direction = form.way.data
        steps = form.number_steps.data
        for _ in range(steps):
            game.move(direction)
            current_room = game.current_room
        if current_room == 'Балкон':
            flash('Вы выбрались на чистый воздух и можете вдохнуть полной грудью', category='primary')
        return redirect(url_for('game', current_room=current_room))

    return render_template('game.html', current_room=current_room, form=form)



if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
