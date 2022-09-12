from ast import While
import socket
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
#from pip._vendor import requests
import requests
import datetime as dt
import json;


class CurrencyConverter:

    def __init__(self, url):
        self.url = 'https://api.exchangerate.host/latest'
        self.response = requests.get(url)
        self.data = self.response.json()
        self.rates = self.data.get('rates')

    def convert(self, amount, base_currency, des_currency):
        if base_currency != 'AED':
            amount = amount / self.rates[base_currency]

        # Limiting the result to 2 decimal places
        amount = round(amount * self.rates[des_currency], 2)
        # Add comma every 3 numbers
        amount = '{:,}'.format(amount)
        print("Converted amount: ", amount)
        return amount


def main():
    converter = CurrencyConverter('https://api.exchangerate.host/latest')

    c = CurrencyCodes()

    Host = '127.0.0.1'
    Port = 1080

    # Create socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((Host, Port))
    serverSocket.listen()
    print("Server listening on: ", Host, Port)
    connSocket, addr = serverSocket.accept()
    print('Connect by ', str(addr))


    while True:
        try:

            recv_data = connSocket.recv(4098)

            data = json.loads(recv_data.decode())

            given_base_currency = data.get("base_currency")
            given_des_currency = data.get("des_currency")
            given_amount = data.get("amount_to_convert")

            print("Received from client: \n", given_base_currency, given_des_currency, given_amount)

            converted_amount = converter.convert(given_amount, given_base_currency, given_des_currency)

            connSocket.send(converted_amount.encode())
        except:
            pass


if __name__ == "__main__":
    main()
