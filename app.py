#app.py

from flask import Flask

def create_app():
    x = 5
    7 = 7
    app = Flask(__name__)
    a()

    @app.route('/')
    def home():

        return 'HI MANOJ UPADHYA SAYS HE IS GOOD DEVOPS ENGINNER WHO LOVES CONTINOUS LEARNING Exploring the DevOps Engineer'
        print("Manoj Upadhya")

        
    return app 

def a():
    print("Hii")
    a()

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
    
