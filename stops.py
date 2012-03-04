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
from jsonp import jsonp

stopsURL = "http://metrotransit.org/Mobile/Nextrip.aspx?route="

def scrapeStops(route, direction) :
    result = urlfetch.fetch(stopsURL + route + "&direction=" + direction)
    stops = []
    if (result.status_code == 200):
        soup = BeautifulSoup(result.content)
        select = soup.html.body.find(id="ctl00_mainContent_NexTripControl1_ddlNexTripNode")
        links = soup.html.body.findAll(attrs={"class" : "cssLink"})
        options = select.findAll('option')
	counter = 1
        for x in options:
            stopCode = x['value']
            if stopCode != "0":
                stops.append({
                    'code': stopCode,
                    'name': x.string,
		    'stopOrder': counter
                })
		counter += 1
    return json.dumps(stops)


class MainHandler(webapp.RequestHandler):

  def get(self):
    try:
        route = self.request.get('route')
        direction = self.request.get('direction')
        if (route == "") or (direction == ""):
            raise ValueError
        memKey = route + "|" + direction
        stops = memcache.get(memKey)
        if stops is None:
            stops = scrapeStops(route, direction)
            memcache.add(memKey, stops, 60*60*24)
        self.response.out.write(jsonp(self.request, stops))
    except (ValueError, TypeError):
        self.response.out.write("<html><body><h4>Invalid Input</h4><p>route and direction are required inputs.<br /><i>Example: /direction?route=6&direction=4</i></p></body></html>")

def main():
  application = webapp.WSGIApplication([('/stops', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
