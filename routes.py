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

routeURL = "http://metrotransit.org/Mobile/Nextrip.aspx"

def scrapeRoutes(self) :
    result = urlfetch.fetch(routeURL)
    routes = []
    if (result.status_code == 200):
        soup = BeautifulSoup(result.content)
        links = soup.html.body.findAll(attrs={"class" : "cssLink"})
        select = soup.html.body.find(id="ctl00_mainContent_NexTripControl1_ddlNexTripRoute")
        options = select.findAll('option')
        for x in options:
            routeNum = x['value']
            if routeNum != '0':
                routes.append({
                    'number' : routeNum,
                    'name' : x.string
                })
    return json.dumps(routes, sort_keys=True)


class MainHandler(webapp.RequestHandler):

  def get(self):
    routes = memcache.get("routes")
    if routes is None:
        routes = scrapeRoutes(self)
        memcache.add("routes", routes, 60 * 60 * 24)
    self.response.out.write(routes)
    

def main():
  application = webapp.WSGIApplication([('/routes', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
