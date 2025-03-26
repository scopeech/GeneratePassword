from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_password(length=15, use_digits=True, use_letters=True, use_symbols=True):
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Выберите хотя бы один тип символов"

    return ''.join(random.choice(chars) for _ in range(length))


@app.route("/", methods=['GET', 'POST'])
def index():
    passwords = []
    if request.method == "POST":
        length = int(request.form.get('length', 15))
        count = int(request.form.get('count', 18))

        use_digits = 'use_digits' in request.form
        use_letters = 'use_letters' in request.form
        use_symbols = 'use_symbols' in request.form

        passwords = [
            generate_password(
                length,
                use_digits=use_digits,
                use_letters=use_letters,
                use_symbols=use_symbols
            )
            for _ in range(count)
        ]

    return render_template("index.html", passwords=passwords)


if __name__ == '__main__':
    app.run(debug=True)