#!/usr/bin/env python
import time
import os
import certifi
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient

config_logging(logging, logging.DEBUG)
os.environ['SSL_CERT_FILE'] = certifi.where()


def message_handler(message):
    print(message)


my_client = SpotWebsocketClient(stream_url='wss://stream.binance.com:9443')
my_client.start()
# Subscribe to a new stream for each symbol in the list
my_client.diff_book_depth(
    #symbol=["ethusdt", "ltcusdt"],
    symbol=["btcusdt"],
    speed=1000,
    id=1,
    callback=message_handler,
)
time.sleep(30)
logging.debug("closing ws connection")
my_client.stop()