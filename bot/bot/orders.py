import logging
from .client import get_client
from .validators import validate_order

def place_order(symbol, side, order_type, quantity, price=None):
    validate_order(symbol, side, order_type, quantity, price)

    client = get_client()

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logging.info(f"Request: {params}")

    try:
        response = client.futures_create_order(**params)
        logging.info(f"Response: {response}")
        return response
    except Exception as e:
        logging.error(str(e))
        raise
