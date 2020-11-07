import os
import errno
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
    parser.add_argument('-s', '--story', default=None, help="The story to download. pass in the part after the /s/*")
    parser.add_argument('-a', '--author', default=None, help="The author to mirror.")
    parser.add_argument('-o', '--output', default="output", help="The directory to write files. default: %(default)s")
    args = parser.parse_args()

    # Create output directory if it doesn't exist
    try:
        os.makedirs(args.output)
    except OSError as e:
        if e.errno != errno.EEXIST:
            pass
        else:
            raise e
    
    # argument checking
    if args.author is None and args.story is None:
        msg="One of (-a / -s) flags must be specified"
        log.error(msg)
        raise RuntimeError(msg)

    return
