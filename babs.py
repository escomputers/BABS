#!/usr/bin/env python

import time
import os
import certifi
import logging
from binance.lib.utils import config_logging

from binance.spot import Spot as Client
from binance.websocket.spot.websocket_client import SpotWebsocketClient

config_logging(logging, logging.DEBUG)

os.environ['SSL_CERT_FILE'] = certifi.where()

'''
spot_client = Client(base_url="https://api.binance.com")
#logging.info(spot_client.depth("BTCUSDT"))
#logging.info(spot_client.depth("BTCUSDT", limit=10))
logging.info(spot_client.book_ticker(symbols=["BTCUSDT", "ETHUSDT"]))
'''

def message_handler(message):
    print(message)


my_client = SpotWebsocketClient(stream_url='wss://stream.binance.com:9443')
my_client.start()

'''
my_client.mini_ticker(
    id=1,
    callback=message_handler,
)
'''
'''
my_client.book_ticker(
    # symbol=["btcusdt", "ethusdt"],
    symbol="bnbusdt",
    id=2,
    callback=message_handler,
)
'''
'''
my_client.partial_book_depth(
    symbol=["btcusdt", "ltcusdt"],
    level=10,
    speed=100,
    id=3,
    callback=message_handler,
)
'''
# Subscribe to a new stream for each symbol in the list
my_client.diff_book_depth(
    symbol=["ethusdt", "ltcusdt"],
    speed=100,
    id=1,
    callback=message_handler,
)

time.sleep(30)

logging.debug("closing ws connection")
my_client.stop()