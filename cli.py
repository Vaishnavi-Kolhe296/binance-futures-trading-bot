import argparse

from validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

from client import get_client
from orders import place_market_order, place_limit_order
from logging_config import logger


# Create parser
parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:
    # Validation
    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    # Get Binance client
    client = get_client()

    # MARKET ORDER
    if args.type.upper() == "MARKET":

        order = place_market_order(
            client,
            args.symbol,
            args.side,
            args.quantity
        )

    # LIMIT ORDER
    elif args.type.upper() == "LIMIT":

        if args.price is None:
            raise ValueError("Price is required for LIMIT orders")

        order = place_limit_order(
            client,
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    # Logging
    logger.info(f"Order Created: {order}")

    # Output
    print("\nOrder Successful!")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])

except Exception as e:

    logger.error(str(e))
    print("Error:", e)