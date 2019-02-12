'''

cad-exchange-rates.py

@jaarsolares

'''

import requests, json

class DownloadRates:

    def __init__(self, xch_rate_code, file_format, number_of_days):
        '''
        Initialize the object with the:
            URL
            Exchange rate code
        '''
        self.urlpath = 'https://www.bankofcanada.ca/valet'
        self.xch_rate_code = self.normalizeXchRateCode(xch_rate_code=xch_rate_code)
        self.file_format = self.normalizeXchgRateFormat(file_format=file_format)
        self.datefilter = f'?recent={number_of_days}'

    def normalizeXchRateCode(self, xch_rate_code=None):
        '''
        This function gets the right RBC Valet exchange rate code for
        the download.
        '''
        if not xch_rate_code:
            print('There was no exchange rate detected, defaulting to USD.')
            xch_rate_code = 'USD'
        return f'FX{xch_rate_code}CAD'

    def normalizeXchgRateFormat(self, file_format=None):
        '''
        Based on the user desired file format, return the string that has
        to go in the URL path.
        /observations/FXUSDCAD/json
        /observations/FXUSDCAD/xml
        /observations/FXUSDCAD/csv
        '''
        dict_formats = {
            'json': f'/observations/{self.xch_rate_code}/json',
            'csv': f'/observations/{self.xch_rate_code}/csv',
            'xml': f'/observations/{self.xch_rate_code}/xml'
            }
        if not file_format:
            print('There was no preferred file format, defaulting to JSON.')
            file_format = 'json'
        return dict_formats[file_format]

    def downloadFromRBCValet(self):
        '''
        This function downloads the exchange rates and looks for
        exceptions
        '''
        if not self.urlpath or not self.xch_rate_code:
            print('ERROR, need to have URL path and exchange rate code.')
            raise UnboundLocalError
        else:
            pass
        tmp_url = self.urlpath + self.file_format + self.datefilter
        # print(tmp_url)
        response = requests.get(tmp_url)
        if response.status_code == 200:
            self.response = response.json()
        else:
            print(f'Error: response {response}')
            self.response = ''
            raise NotImplementedError


if __name__=="__main__":
    download_usd_cad = DownloadRates(xch_rate_code='USD', file_format='json', number_of_days=7)
    download_usd_cad.downloadFromRBCValet()
    print(download_usd_cad.response)