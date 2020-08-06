from flask_table import Table, Col
class Results(Table):
    id = Col('Id', show=False)
    base_currency = Col('Base Currency')
    pair_currency = Col('Pair Currency')
    bid_rate = Col('Bid')
    ask_rate = Col('Ask')
