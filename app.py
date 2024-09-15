# app.py
from . import app, db
from .routes import init_db, add_sample_data

if __name__ == '__main__':
    init_db()
    add_sample_data()
    app.run(debug=True)