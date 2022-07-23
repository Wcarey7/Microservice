import socket
import json

Host = '127.0.0.1'
Port = 1080

#connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Host, Port))
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Connected to: ", Host, Port)





curr1 = "USD"
curr2 = "EUR"
amount = 11

data = json.dumps({"base_currency": curr1, "des_currency": curr2, "amount_to_convert": amount})
client.send(data.encode())

while True:
    recvData = client.recv(4098)
    print(recvData.decode('utf-8'))     
    break



client.close()








    





    