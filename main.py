import logging
import os
import sys

from format.index import Index
from format.mpls import Mpls

logging.basicConfig(level=logging.DEBUG, format='%(name)-32s: %(levelname)-8s %(message)s')

if __name__ == '__main__':
    # Index(sys.argv[1] + "/index.bdmv")

    for file in os.listdir(sys.argv[1] + "/PLAYLIST/"):
        Mpls(sys.argv[1] + "/PLAYLIST/" + file)
