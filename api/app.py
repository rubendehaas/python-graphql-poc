from app.database import init_db
from app import app

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0',port=5000,debug=True)