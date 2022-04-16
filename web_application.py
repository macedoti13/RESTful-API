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

class Company(Resource):
    # consulta
    def get(self, company_id):
        abort_if_company_doesnt_exist(company_id)
        company = dict(df.loc[company_id])
        return company

    # atualização 
    def set():
        pass

    # inserção
    def put():
        args = parser.parse_args()
        content = {'Symbol': args['Symbol'], 'Name': args['Name'], 'Sector': args['Sector'],
                    'Price': args['Price'], 'Price/Earnings': args['Price/Earnings'], 'Dividend Yield':args['Dividend Yield'],
                    'Earnings/Share': args['Earnings/Share'], '52 Week Low': args['52 Week Low'], 
                    '52 Week high': args['52 Week high'], 'Market Cap':args['Market Cap'], 'EBITDA':args['EBITDA'],
                    'Price/Sales':args['Price/Sales'], 'Price/Book':args['Price/Book'], 'SEC Filings':args['SEC Filings']}
        df = df.append(content, ignore_index=True)
        return content, 201

    # deleção
    def delete(self, company_id):
        abort_if_company_doesnt_exist(company_id)
        df.drop(company_id, inplace=True)
        pass

class CompanyList(Resource):
    # consulta
    def get():
        pass

    # aumenta a lista 
    def post():
        pass

api.add_resource(CompanyList, '/company')
api.add_resource(Company, '/company/<int:company_id>')

app.run(debug=True)