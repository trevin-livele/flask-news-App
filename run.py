# from flask import Flask, render_template
# from distutils.log import Debug
# from app import app
import requests
# app = Flask(__name__)


# if __name__ == '__main__':
#     app.run()


from distutils.log import debug
from app import app


if __name__ == '__main__':
    app.run()