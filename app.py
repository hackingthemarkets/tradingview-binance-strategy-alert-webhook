import json, config
from flask import Flask, request, jsonify, render_template
from response import order,usdtBalance,positions

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    # print(request.data)
    data = json.loads(request.data)

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Nice try, invalid passphrase"
        }

    symbol=data['ticker'][0:-8]+"/USDT"
    side = data['strategy']['order_action']
    price=data['strategy']['order_price']
    amount = usdtBalance()/price

    if(positions(symbol)):
        position=positions(symbol)
        existSide='buy' if(position['side'])=='long' else 'sell'
        if(existSide!=side):
            amount=position['contracts']
            order_response = order(symbol, side,amount, price)

        amount =usdtBalance()

    order_response = order(symbol, side,amount, price)

    if order_response:
        return {
            "code": "success",
            "message": "order executed"
        }
    else:
        print("order failed")

        return {
            "code": "error",
            "message": "order failed"
        }