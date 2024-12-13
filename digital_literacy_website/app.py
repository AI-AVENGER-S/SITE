from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница с памятками
@app.route('/tips')
def tips():
    return render_template('tips.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Страница с опросом
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # Обработка ответов на опрос (можно сохранить в базу данных или файл)
        answers = request.form
        print(answers)  # Для отладки, можно убрать позже
        return redirect(url_for('tips'))  # Перенаправление на страницу "Спасибо"
    return render_template('survey.html')


if __name__ == '__main__':
    app.run(debug=True)