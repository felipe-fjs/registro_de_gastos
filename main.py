from app import app
import os 


def run():

    if not os.path.exists(f"{os.getcwd()}/db/meudb.db"):
        print('oi')
        with open('./db/meudb.db', 'w') as arc:
            arc.write('')
    print('oi')
    app.run()

if __name__ == '__main__':
    run()
