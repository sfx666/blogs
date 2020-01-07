from flask import Flask
from flask_script import Manager

app = Flask(__name__)




manager = Manager()



if __name__ == '__main__':
    manager.run()
