from app.database import init_db
from app import app

if __name__ == '__main__':
    init_db()
    app.run()