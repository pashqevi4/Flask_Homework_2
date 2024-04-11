# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет
# удалён cookie-файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, request, render_template, make_response, url_for, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        context = {
            'name': request.form.get('name'),
            'email': request.form.get('email')
        }
        response = make_response(render_template('hello_page.html', **context))
        # response = make_response(redirect(url_for('hello', **context)))
        response.set_cookie('name', context['name'])
        response.set_cookie('email', context['email'])
        return response
    if request.cookies.get('name'):
        res = make_response(render_template('form.html'))
        res.set_cookie('name', '', 0)
        res.set_cookie('email', '', 0)
        return res
    return render_template('form.html')


# @app.route('/hello/')
# def hello():
#     return render_template('hello_page')


if __name__ == '__main__':
    app.run(debug=True)
