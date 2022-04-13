from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

df = pd.read_csv('constituents-financials.csv')
df['Market Cap'] = df['Market Cap'].astype('float64')

app.run(debug=True)