from app import app
import os

def run(__name__):
    if not os.path.exists(f"{os.getcwd()}/db/meudb.db"):
        print('oi')
        with open('./db/meudb.db', 'w') as arc:
            arc.write('')
    print('oi')
    app.run()