
from flask import Flask, render_template, request
from helpers import todo

app: Flask = Flask(__name__)

todo_list: list[todo] = []
todo_count: int = 0
 
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/guess_game', methods=["GET", "POST"])
def create_guess_game():
    if request.method == "POST":     
        title: str = request.form['title']
        usr_guess: str = request.form['usr_guess']
 
        if title == '':
            return render_template("guess_game.html")
 
        new_todo: todo = todo(title, usr_guess)
        todo_list.append(new_todo)
 
        return render_template("success.html", title=title, usr_guess=usr_guess)
    return render_template("guess_game.html")


if __name__ == '__main__':
    app.run(debug=True)