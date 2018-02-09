import logging
import argparse
parser = argparse.ArgumentParser(description="Take option")
parser.add_argument("-d", help="logginglevel", action="store_true")
args = parser.parse_args()
#user_level = getattr(logging, loglevel.upper())
logging.basicConfig(filename="example.log", level = logging.DEBUG if args.d else logging.WARNING)
logging.debug("This message should go to the log file")
logging.info("So should this")
logging.warning("And this, too")
logging.error("Finaly")
