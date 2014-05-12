__author__ = 'vardelean'

from pprint import pprint


def log(topic, data):
    print ">>>vwh:%s:" % str(topic)
    pprint(data)
    print "<<<<"
