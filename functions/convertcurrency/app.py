from requests import get
import json
from uuid import uuid4
from datetime import datetime
# import sys
# sys.path.insert(0, '.')
# from functions.getgamesonsale.app import lambda_hadler as getgamesonsale

def create_payload(game, brl):
    return {
        "id": str(uuid4()),
        "title": game.get("title"),
        "normalPrice": "{:.2f}".format(game.get("normalPrice") * brl),
        "salePrice": "{:.2f}".format(game.get("salePrice") * brl),
        "timestamp": datetime.now().isoformat()
    }

def lambda_handler(event, context):
    params = {'base': 'USD'}
    currency_api_response = get("https://api.exchangerate.host/latest", params = params)        

    return create_payload(event, json.loads(currency_api_response.content).get("rates").get("BRL"))

# if __name__ == "__main__":
#     games = getgamesonsale({}, {})
#     print(lambda_hadler(games[0], {}))