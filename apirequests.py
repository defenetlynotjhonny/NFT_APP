import requests


class Songbird_Api():
    def __init__(self):
        self.sgb_api_url = "https://songbird-explorer.flare.network/api?module=account&action=tokenlist&address=0x1785BbD63338f37924F6F37BF5466F18071eC876"
        self.sgb_coinprice_btc_usd = "https://songbird-explorer.flare.network/api?module=stats&action=coinprice"
        self.sgbresponse = requests.get(self.sgb_api_url)
        self.sgb_coinprice_btc_usd_response = requests.get(self.sgb_coinprice_btc_usd)

    def songbird_response(self,req="none"):

        self.price_response_usd = self.sgb_coinprice_btc_usd_response.json()["result"]["coin_usd"]
        
        print("Songbird network awnser: \n",)
        result = []
        if req =="name":
            for i in range(10):
                print(f"TokenName {i}: ", self.sgbresponse.json()["result"][i]["name"],"\n","TokenBalance: ",self.sgbresponse.json()["result"][i]["balance"] )
                result.append(self.sgbresponse.json()["result"][i]["name"])
                result.append(self.sgbresponse.json()["result"][i]["balance"])
        elif req == "price":
            if self.price_response_usd == None:
                print("SGB/USD: not availble yet ") 
                result.append("SGB/USD: not availble yet ")
            else:
                print(self.price_response_usd)
                result.append(self.price_response_usd)
        else:
            print("invalid input")
            result.append("invalid input")
        return result
    
    def songbird_response_name():
        name_output = {}
        
        pass
        
        
