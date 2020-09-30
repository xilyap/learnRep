# coding: utf-8
import requests

class Rate:
    def __init__(self, format='value'):
        self.format = format
        self.diff = True
    
    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']
    
    def make_format(self, currency, field = 'Value'):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        
        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                return response[currency]
            
            if self.format == 'value':
                return response[currency][field]
        
        return 'Error'
    
    def find_max(self):
        response = self.exchange_rates()
        cur_list = {x:response[x]["Value"]/response[x]["Nominal"] for x in response}
        return(self.make_format(max(cur_list, key=cur_list.get),'Name'))
    
    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format (self.diff == False)
        или изменение курса за 1 день (self.diff == True)"""
        cur = 'EUR'
        if (self.format == 'value') and (self.diff == True):
            return self.make_format(cur) - self.make_format(cur,'Previous')
        else:
            return self.make_format(cur)
    
    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format (self.diff == False)
        или изменение курса за 1 день (self.diff == True)"""
        cur = 'USD'
        if (self.format == 'value') and (self.diff == True):
            return self.make_format(cur) - self.make_format(cur,'Previous')
        else:
            return self.make_format(cur)

    def AZN(self):
        """Возвращает курс азербайджанского маната на сегодня в формате self.format"""
        return self.make_format('AZN')