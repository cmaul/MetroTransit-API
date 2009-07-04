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


class MainHandler(webapp.RequestHandler):

  def get(self):
    defaultHtml = '''<html>
	<body>
		<h1>Metro Transit API</h1>
		<p>This API provides data from MetroTransit.org in a JSON encoded format.</p>
		<p>Currently Supported Interfaces:<br />
		<ul>
			<li>routes - Displays the list of all routes provided by MetroTransit.</li>
			<li>direction - Displays the list of potential directions for a given route.</li>
			<li>stops - Displays the list of stops given a route and a direction</li>
			<li>nextrip - Displays a list of times for the bus to arrive given a stop, direction, and route.  Some times are based on bus GPS data.</li>
		</ul></p>
		<h3>Routes</h3>
		<p><i>Example: http://metrotransitapi.appspot.com/routes</i><br /><br />
		Sample output:<br /><br />
		{"2": "2 Franklin Av - Riverside Av - U o", "3": "3 U of M - Como Av - Energy Park D", "4": "4 New Brighton - Johnson St - Brya", "5": "5 Brklyn Center - Fremont - 26th A", "6": "6 U of M - Hennepin - Xerxes - Fra", "7": "7 Plymouth Av - Riverside - 27th A", "9": "9 Glenwood Av - Wayzata Blvd - Ced", "10": "10 Central Av - University Av - Nor", "11": "11 Columbia Heights - 2nd St NE - 4", "12": "12 Uptown - Excelsior Blvd - Hopkin", "14": "14 Robbinsdale - West Broadway Av -", "16": "16 U of M - University Av - Midway", "17": "17 Minnetonka Blvd - Uptown - Washi", "18": "18 Nicollet Av - South Bloomington", "19": "19 Olson Memorial Hwy - Penn Av N -", "21": "21 Uptown - Lake St - Selby Av", "22": "22 Brklyn Ctr - Lyndale Av N - Ceda", "23": "23 Uptown - 38th St - Highland Vill", "24": "24 Franklin - 36th Av S - 42nd Av S", "27": "27 26th St - 28th St - Lake St - Mi", "46": "46 50th St - 42nd St - 46th St LRT-", "54": "54 Ltd Stop - W 7St - Airport - MOA", "55": "55 Hiawatha LRT - Mpls - Airport -", "56": "56 Light Rail Shuttle - Lindbergh -", "62": "62 Rice St - Little Canada - Shorev", "63": "63 Grand Av - 3rd St - Sunray - McK", "64": "64 Payne - Maryland - White Bear Av", "65": "65 Dale St - Co Rd B - Rosedale", "67": "67 W Minnehaha - Wabasha - Smith -", "68": "68 Jackson St - Robert St - 5th Av", "70": "70 St Clair Av - W 7th - Burns Av -", "71": "71 Little Canada - Edgerton - Conco", "74": "74 46St - Randolph - W 7St - E 7St", "80": "80 Maplewood - White Bear Av - Sunr", "84": "84 Rosedale - Snelling - 46th St LR", "94": "94 Express - Minneapolis - St Paul", "121": "121 U of M - Campus Connector", "444": "444 MVTA - MOA - Eagan - Burnsville", "445": "445 MVTA - MOA - Eagan - Cedarvale -", "515": "515 Southdale - 66th St - Bloomingto", "538": "538 Southdale - York Av - Southtown", "539": "539 France Av - Penn Av - Normandal", "540": "540 Edina - Richfield - 77th St - MO", "675": "675 Express - Mound - Wayzata - Ridg", "720": "720 Shuttle - Maple Grove - Starlite", "721": "721 Ltd Stop - Brooklyn Center - New", "722": "722 Brooklyn Ctr - Humboldt Av N - S", "723": "723 Starlite - North Henn Comm Colle", "724": "724 Ltd Stop - Target Campus - Starl"}<br />
		</p>
		<h3>Direction</h3>
		<p><i>Example: http://metrotransitapi.appspot.com/direction?route=4</i><br /><br />
		Required parameters:<ul><li>route</li></ul>
		Sample output:<br /><br />
		{"1": "SOUTHBOUND", "4": "NORTHBOUND"}		
		</p>
		<h3>Stops</h3>
		<p><i>Example: http://metrotransitapi.appspot.com/stops?route=6&direction=1</i><br /><br />
		Required parameters:<ul><li>route</li><li>direction</li></ul>
		{"ONBE": "ONTARIO \/ BEACON ", "VVWO": "VALLEY VIEW\/WOODDALE", "4SCE": "4 ST NE \/ CENTRAL ", "WAHE": "WASHINGTON \/HENNEPIN", "HEUP": "HENNEPIN \/ UPTOWN TS", "77CO": "77 ST \/ COMPUTER ", "1S1A": "1 ST \/ 1 AV N ", "78PI": "78 ST \/ PICTURE DR ", "FRHE": "FRANKLIN \/ HENNEPIN ", "MCTC": "MPLS COMM TECH COLL ", "SODA": "SOUTHDALE ", "OAWA": "OAK \/ WASHINGTON ", "MNTC": "MINN DR TRANSIT CTR ", "FRPK": "FRANCE \/ PARKLAWN ", "AR7N": "ARRIVE \/ 7 ST NIC ", "50FR": "50 ST \/ FRANCE ", "36HE": "36 ST \/ HENNEPIN ", "39SH": "39 ST\/ SHERIDAN AV S", "4S15": "4 ST \/ 15 AV SE ", "LV7N": "LEAVE 7 ST\/ NICOLLET", "8SHE": "8 ST \/ HENNEPIN ", "50XR": "50 ST \/ XERXES "}<br />
		</p>
		<h3>Nextrip</h3>
		<p><i>Example: http://metrotransitapi.appspot.com/nextrip?route=6&direction=1&stop=HEUP</i><br /><br />
		Required parameters:<ul><li>route</li><li>direction</li><li>stop</li></ul>
		Sample output:<br /><br />
		{"6B": "10:31 AM", "6D": "11:02 AM", "6E": "11:17 AM"}<br />
		</p>
		<br /><br />
		Developed by Corey Maul.  Very loosely based on yourmuni by mihaysa (<a href="http://yourmuni.appspot.com">http://yourmuni.appspot.com</a>)<br /><br />
		Full source code is available at: <a href="http://github.com/cmaul/MetroTransit-API">http://github.com/cmaul/MetroTransit-API</a>
	</body>
</html>'''

    self.response.out.write(defaultHtml)


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
