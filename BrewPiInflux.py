# Copyright 2012 BrewPi
# This file is part of BrewPi.

# BrewPi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# BrewPi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with BrewPi.  If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime
import time

import urllib, urllib2

class BrewPiInfluxLogger:
    """
    This class logs temperature data to influxdb.
    """
    def __init__(self, baseurl, dbname, dbuser, dbpass):
        self.baseurl = baseurl
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpass = dbpass
        self.url = "%s/db/%s/series?u=%s&p=%s" % (self.baseurl, self.dbname, self.dbuser, self.dbpass)

	def addToSeries(row):

		cols = ["BeerTemp", "BeerSet", "BeerAnn", "FridgeTemp", "FridgeSet", "FridgeAnn", "RoomTemp", "State"]

		points = [ [row["BeerTemp"]], [row["BeerSet"]], [row["BeerAnn"]], [row["FridgeTemp"]], [row["FridgeSet"]], [row["FridgeAnn"]], [row["RoomTemp"]], [row["State"]] ]

		payload = dict( name = "temperatures", columns = cols, points = points)

		data = urllib.urlencode(payload)
		request = urllib2.Request(influxDBUrl, data)
		try: 
			response = urllib2.urlopen(request)
		except urllib2.URLError, e:
		    print e
