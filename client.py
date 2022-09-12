import socket
import json

Host = '127.0.0.1'
Port = 1080

#connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Host, Port))
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Connected to: ", Host, Port)



while True:
    curr1 = input("Enter first currency name: ")
    curr2 = input("Enter second currency name: ")
    amount = float(input("Enter amount to convert: "))

    data = json.dumps({"base_currency": curr1, "des_currency": curr2, "amount_to_convert": amount})
    client.send(data.encode())
    
    recvData = client.recv(4098)
    print("Conversion: ", recvData.decode('utf-8'))    
     
    goAgain = input("Continue? Y/N: ")
    if goAgain == "N":
        break


client.close()








    





    
