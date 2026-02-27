import argparse
from bot.orders import place_order
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    print("Order Request:")
    print(vars(args))

    response = place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    print("\nOrder Response:")
    print({
        "orderId": response.get("orderId"),
        "status": response.get("status"),
        "executedQty": response.get("executedQty"),
        "avgPrice": response.get("avgPrice"),
    })

    print("\n✅ Order executed")

if __name__ == "__main__":
    main()
