import asyncio
import logging
import argparse

handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter(
        style="{",
        fmt="[{name}:{filename}] {levelname} - {message}"
    )
)

log = logging.getLogger("literotica_dl")
log.setLevel(logging.INFO)
log.addHandler(handler)

def main():
    # Handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-V', '--version', action='version', version='v0.0.1')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    args = parser.parse_args()
    return
