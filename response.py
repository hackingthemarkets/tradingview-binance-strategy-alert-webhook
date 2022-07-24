from turtle import position
import ccxt
import config
import math
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)

exchange = exchange_class({
    'apiKey': config.API_KEY,
    'secret': config.API_SECRET,
    'options': {'defaultType': 'future', }
})



def order(symbol, side, amount, price):
    try:
        order = exchange.createLimitOrder(symbol, side, amount, price)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return order

def usdtBalance():
    balance=exchange.fetchBalance()['total']['USDT']
    balance=(math.floor(balance/3*100)/100)

    return balance



def positions(symbol):
    exchange.fetchPositions(symbols=[symbol]) #GetPositions

# positions=exchange.fetchPositions(symbols=["ETH/USDT"]) #GetPositions





# lst=(exchange.symbols)

# with open('symbols.json', 'w') as f:
#     json.dump(lst, f)



# print(exchange.createLimitOrder(symbol='ETH/USDT', side='buy', amount=0.01, price=1500)) #createLimitOrder

# exchange.fetchPositions(symbols=["ETC/USDT"]) #GetPositions