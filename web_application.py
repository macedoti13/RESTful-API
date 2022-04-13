from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)

df = pd.read_csv('constituents-financials.csv')

# columns in the 'int64' data type causes problems for the api, I just turned it into 'float64'
df['Market Cap'] = df['Market Cap'].astype('float64')

def abort_if_company_doesnt_exist(company_id):
    """ Aborts if the user tries to search for a company that doesn't exist

    Args:
        company_id (int64): company index in the dataframe (from 0 to 504)
    """
    if company_id not in df.index:
        abort(404, message=f'Company {company_id} doesn\'t exist')

parser = reqparse.RequestParser()
parser.add_argument('Symbol')
parser.add_argument('Name')
parser.add_argument('Sector')
parser.add_argument('Price')
parser.add_argument('Price/Earnings')
parser.add_argument('Dividend Yield')
parser.add_argument('Earnings/Share') 
parser.add_argument('52 Week Low') 
parser.add_argument('52 Week High') 
parser.add_argument('Market Cap') 
parser.add_argument('EBITDA')
parser.add_argument('Price/Sales') 
parser.add_argument('Price/Book') 
parser.add_argument('SEC Filings')

app.run(debug=True)