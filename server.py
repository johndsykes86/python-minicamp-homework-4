from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

connection=sqlite3.connect('database.db')
print('Database opened successfully')

connection.execute('CREATE TABLE IF NOT EXISTS movies(movie TEXT, rating TEXT, theatre TEXT, review TEXT)')
print ('Table created successfully')
connection.close()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/addmovie', methods=["POST"])
def addmovie():
    connection=sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        movie_name = request.form['movie']
        movie_rating = request.form['rating']
        movie_theatre = request.form['theatre']
        movie_review = request.form['review']

        cursor.execute('INSERT INTO movies (movie, rating, theatre, review) VALUES (?,?,?,?)', (movie_name, movie_rating, movie_theatre, movie_review))
        connection.commit()
        message = 'Data written successfully, we hoped you enjoyed the movie. If you have any issues or concerns, please see the theatre manager. You may now close the window.'
    except:
        connection.rollback()
        message = "There was an error uploading the review, please try again by clicking the home link at the bottom."
    finally:
        return render_template('result.html', message = message)
        connection.close();
