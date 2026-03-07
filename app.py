from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from models import db, User
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sayza_gizli_anahtar_123' # Form güvenliği için şart
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # Veritabanı dosyası

db.init_app(app)

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.username.data} için hesap oluşturuldu!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Kayıt Ol', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Bu komut veritabanını otomatik oluşturur
    app.run(debug=True)
