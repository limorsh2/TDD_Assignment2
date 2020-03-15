import requests


class BrakingBad:

    """
    @ref: https://github.com/shevabam/breaking-bad-quotes#get-v1quotes
    """

    base = 'https://breaking-bad-quotes.herokuapp.com/v1/'

    @staticmethod
    def get_random_quote():
        req = requests.get(BrakingBad.base + 'quotes')
        quote = req.json()
        return quote[0]['quote']

    @staticmethod
    def get_list_quotes(num):
        req = requests.get(BrakingBad.base + 'quotes/' + str(num))
        list_quotes = req.json()
        res = []
        for i in range(num):
            res.append(list_quotes[i]['quote'])
        return res


print(BrakingBad.get_random_quote())

#print(BrakingBad.get_list_quotes(3))
