import os
import errno
import asyncio
import logging
import argparse
from .classes.Story import Story as lit_story

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

def returnStub(stub):
    # if literotica.com in arg, trim down to the url stub
    if "literotica.com" in stub:
        pattern = "/s/"
        x = stub.find(pattern)
        return stub[x+len(pattern):]
    else:
        return stub

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
    except FileExistsError:
        pass

    # argument checking
    if args.author is None and args.story is None:
        msg="One of (-a / -s) flags must be specified"
        log.error(msg)
        raise RuntimeError(msg)

    # Store current directory and return on end
    cwd = os.getcwd()
    # change into output directory
    os.chdir(args.output)

    try:
        pass
        if args.story:

            stub = args.story
            stub = returnStub(stub)

            s = lit_story(id=stub)
            author = s.get_author()
            cat = s.get_category()
            desc = s.get_description()
            title = s.get_title()
            text = s.get_text()
            
            f = open( ("%s.html" % str(title)), "w")
            f.write( "Title: %s<br/>Author: %s<br/>Category: %s<br/>Description: %s<br/><hr/><br/>" % ( str(title), str(author), str(cat), str(desc) ) )
            for t in text:
                f.write(str(t))
            f.close()

        if args.author:
            pass

    except:
        raise
    finally:
        os.chdir(cwd)
        return
