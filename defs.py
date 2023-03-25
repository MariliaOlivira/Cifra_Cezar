import string
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import selenium

print("my part")
alfa = list(string.ascii_lowercase)
export = []
count = 0
def cezar_recursivo():
    dict = {}
    dict.keys = alfa
    print(dict)

cezar_recursivo()

def cifra_cesar_encode(texto: str, chave: int) -> str:
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            indice = (ord(letra) - 97 + chave) % 26
            resultado += chr(indice + 97)
        else:
            resultado += letra
    return resultado


def cifra_cesar_decode(texto: str, chave: int) -> str:
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            indice = (ord(letra) - 97 - chave) % 26
            resultado += chr(indice + 97)
        else:
            resultado += letra
    return resultado

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class CifraCesarForm(FlaskForm):
    texto = StringField('Texto:', validators=[DataRequired()])
    chave = IntegerField('Chave:', validators=[DataRequired(), NumberRange(min=1, max=25)])
    encode_button = SubmitField('Codificar')
    decode_button = SubmitField('Decodificar')

def cifra_cesar_encode(texto: str, chave: int) -> str:
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            indice = (ord(letra) - 97 + chave) % 26
            resultado += chr(indice + 97)
        else:
            resultado += letra
    return resultado


def cifra_cesar_decode(texto: str, chave: int) -> str:
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            indice = (ord(letra) - 97 - chave) % 26
            resultado += chr(indice + 97)
        else:
            resultado += letra
    return resultado


@app.route('/', methods=['GET', 'POST'])
def cifra_cesar():
    form = CifraCesarForm()
    if form.validate_on_submit():
        texto = form.texto.data
        chave = form.chave.data
        if form.encode_button.data:
            texto_codificado = cifra_cesar_encode(texto, chave)
            flash(f'Texto codificado: {texto_codificado}')
        else:
            texto_decodificado = cifra_cesar_decode(texto, chave)
            flash(f'Texto decodificado: {texto_decodificado}')
    return render_template('cifra_cesar.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
