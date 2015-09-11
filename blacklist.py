#!/usr/bin/env python

import os
import sys
import constants
"""
    This class is used for reading blacklist configuration file.
    Saves each filename into Constants class.
"""

class BlacklistReader():
    def __init__(self, filen):
        self.filename = filen
        try:
            self.file = open(self.filename, 'r')
        except:
            print "parse_time.csv: error opening file for write\n"
            raise

    def read(self):
        """
        Open a file and read it's content line by line.
        Appends each line in Constants.BLACKLIST
        """
        content = self.file.readlines()
        for line in content:
            if len(line) > 3:
                constants.Constants.BLACKLIST.append(line.rstrip(" \n"))

    def to_string(self):
        s = ""
        for file in constants.Constants.BLACKLIST:
            s += file
        return s