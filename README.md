# Microservice
Currency Converter Microservice

# currency_converter UML

[UML Diagram.pdf](https://github.com/Wcarey7/Microservice/files/9215732/UML.Diagram.pdf)


# Required Python imports:

   import socket
   
   import json
   
   from forex_python.converter import CurrencyRates
   
   from forex_python.converter import CurrencyCodes
   
   
   
# Required Library Installs:

   pip install forex-python



# How to package data:


    data = json.dumps({"base_currency": curr1, "des_currency": curr2, "amount_to_convert": amount})

    *Note: {"key": value} are always of type string. Key is required in quotes with names exactly as written above.
    
    **Value: is the name of the currency as its 3 letter ISO code, like "USD".




# Example send data from client to microservice:

    client.send(data.encode())




# Microservice returns to client:

    converted_amount is a single number in the format of "11.7"
    
# Demo: 


https://user-images.githubusercontent.com/13939125/189767221-19b79533-2d98-4ba7-8e5f-a181c5ee967e.mp4


