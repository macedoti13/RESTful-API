from email import message
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

app.run(debug=True)