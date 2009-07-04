#!/usr/bin/env python
#
# MetroTransit API
# Corey Maul (chmaul AT gmail DOT com)
#
# Copyright (c) 2009 Corey Maul
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup
from google.appengine.api import memcache
from django.utils import simplejson as json
import re

stopsURL = "http://nextrip.metc.state.mn.us/NextripText.aspx?route="

def scrapeDirection(self) :
	
	for key in self.request.params.keys():
		if (key == 'route'):
			route = self.request.get(key)
		elif (key == 'direction'):
			direction = self.request.get(key)
		elif (key == 'stop'):
			stop = self.request.get(key)
	
	result = urlfetch.fetch(stopsURL + route + "&direction=" + direction + "&stop=" + stop)
	if (result.status_code == 200):
		soup = BeautifulSoup(result.content)
		depart = soup.html.body.find(attrs={'id':re.compile("gvNextrip$")})
		if depart is None:
			return json.dumps({})
		departRows = depart.findAll("tr")
		departures = {}
		for x in departRows:
			route = x.find(attrs={'id':re.compile("RouteNo$")})
			if (route):
				routeStr = route.string
				depTime = x.find(attrs={'id':re.compile("Departs$")})
				depTimeStr = depTime.string
				departures[routeStr] = depTimeStr
	return	json.dumps(departures)


class MainHandler(webapp.RequestHandler):

  def get(self):
    departures = scrapeDirection(self)
    self.response.out.write(departures)

def main():
  application = webapp.WSGIApplication([('/nextrip', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
