from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Initialisation de la base de données
# Flask-SQLAlchemy crée automatiquement la base de données en fonction du modèle
# python app.py
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///etudiants.db'
db = SQLAlchemy(app)

# Définition du modèle pour DB
class Etudiant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form['nom']
    prenom = request.form['prenom']
    age = request.form['age']

    nouvel_etudiant = Etudiant(nom=nom, prenom=prenom, age=age)
    db.session.add(nouvel_etudiant)
    db.session.commit()

    return render_template('confirmation.html', nom=nom, prenom=prenom, age=age)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

