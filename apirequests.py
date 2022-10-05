import requests


class Songbird_Api():
    def __init__(self):
        self.sgb_api_url = "https://songbird-explorer.flare.network/api?module=account&action=tokenlist&address=0x1785BbD63338f37924F6F37BF5466F18071eC876"
        self.sgb_coinprice_btc_usd = "https://songbird-explorer.flare.network/api?module=stats&action=coinprice"
        self.sgbresponse = requests.get(self.sgb_api_url)
        self.sgb_coinprice_btc_usd_response = requests.get(self.sgb_coinprice_btc_usd)
        self.price_response_usd = self.sgb_coinprice_btc_usd_response.json()["result"]["coin_usd"]

    def songbird_response_price(self):
        result = []
        
        
        if self.price_response_usd == None:
            print("SGB/USD: not availble yet ") 
            result.append("SGB/USD: not availble yet ")
        else:
            print(self.price_response_usd)
            result.append(self.price_response_usd)
        
        return result
    
    def songbird_response_name(self):
        result = []
        for i in range(8):
            print(f"TokenName {i}: ", self.sgbresponse.json()["result"][i]["name"],"\n","TokenBalance: ",self.sgbresponse.json()["result"][i]["balance"] )
            result.append(self.sgbresponse.json()["result"][i]["name"])
            result.append(self.sgbresponse.json()["result"][i]["balance"])
        
        return result
        
        
