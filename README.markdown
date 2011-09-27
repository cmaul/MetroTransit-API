# Metro Transit API

This API provides data from MetroTransit.org in a JSON encoded format.  Sample runs at http://metrotransitapi.appspot.com.

Currently Supported Interfaces:

* routes - Displays the list of all routes provided by MetroTransit.
* direction - Displays the list of potential directions for a given route.
* stops - Displays the list of stops given a route and a direction
* nextrip - Displays a list of times for the bus to arrive given a stop,
  direction, and route

## Routes

Example: *http://metrotransitapi.appspot.com/routes*

### Sample output:

    [{"name": "55 - Hiawatha Light Rail", "number": 55}, {"name": "888 - Northstar Commuter Rail", "number": 888}, {"name": "2 - Franklin Av - Riverside Av - U of M - 8th St SE", "number": 2}, {"name": "3 - U of M - Como Av - Energy Park Dr - Maryland Av", "number": 3}, {"name": "4 - New Brighton - Johnson St - Bryant Av - Southtown", "number": 4}, {"name": "5 - Brklyn Center - Fremont - 26th Av - Chicago - MOA", "number": 5}, {"name": "6 - U of M - Hennepin - Xerxes - France - Southdale", "number": 6}, ... ]

## Direction

Example: *http://metrotransitapi.appspot.com/direction?route=4*

### Required parameters:

* route

### Sample output:

    [{"code": 4, "name": "NORTHBOUND"}, {"code": 1, "name": "SOUTHBOUND"}]


## Stops

Example: *http://metrotransitapi.appspot.com/stops?route=6&direction=1*

### Required parameters:

* route
* direction

### Sample output:
    [{"stopOrder": 1, "code": "ONBE", "name": "Ontario St SE and Beacon St SE"}, {"stopOrder": 2, "code": "4S15", "name": "4th St SE and 15th Ave SE"}, {"stopOrder": 3, "code": "4SCE", "name": "4th St SE and Central Ave SE"}, {"stopOrder": 4, "code": "1S1A", "name": "1st Ave N and 1st St N"}, {"stopOrder": 5, "code": "7SNI", "name": "Nicollet Mall and 7th St S"}, {"stopOrder": 6, "code": "8SHE", "name": "Hennepin Ave and 8th St"}, {"stopOrder": 7, "code": "MCTC", "name": "Minneapolis Comm and Tech College"}, {"stopOrder": 8, "code": "FRHE", "name": "Hennepin Ave and Franklin Ave"}, {"stopOrder": 9, "code": "HEUP", "name": "Uptown Transit Station"}, {"stopOrder": 10, "code": "36HE", "name": "Hennepin Ave and 36th St W"}, {"stopOrder": 11, "code": "39SH", "name": "39th St and Sheridan Ave S"}, {"stopOrder": 12, "code": "50XR", "name": "Xerxes Ave and 50th St W"}, {"stopOrder": 13, "code": "50FR", "name": "France Ave and 50th St W"}, {"stopOrder": 14, "code": "VVWO", "name": "Valley View Rd and Wooddale Ave"}, {"stopOrder": 15, "code": "SODA", "name": "Southdale Transit Center"}, {"stopOrder": 16, "code": "PKGA", "name": "Gallagher Dr and Parklawn Ave"}, {"stopOrder": 17, "code": "FRMN", "name": "France Between 76th St and Minnesota Dr"}, {"stopOrder": 18, "code": "MNTC", "name": "Minnesota Dr and France Ave"}, {"stopOrder": 19, "code": "77CO", "name": "77th St W and Computer Ave"}, {"stopOrder": 20, "code": "78PI", "name": "Picture Dr and 78th St W"}]

## Nextrip

Example: *http://metrotransitapi.appspot.com/nextrip?route=6&direction=1&stop=HEUP*

### Required parameters:

* route
* direction
* stop

### Sample output:

    [{"time": "9 Min", "actual": true, "number": "6B", "name": "France Av \/Southdale \/ Via Woodale"}, {"time": "7:50", "actual": false, "number": "6E", "name": "Minn Drive \/ Xerxes Av \/ Southdale"}, {"time": "8:05", "actual": false, "number": "6D", "name": "Southdale\/France Av"}, {"time": "8:18", "actual": false, "number": "6E", "name": "Minn Drive \/ Xerxes Av \/ Southdale"}, {"time": "8:32", "actual": false, "number": "6B", "name": "France Av \/Southdale \/ Via Woodale"}, {"time": "8:47", "actual": false, "number": "6E", "name": "Minn Drive \/ Xerxes Av \/ Southdale"}]


## Info & License

Developed by Corey Maul. Very loosely based on yourmuni by mihaysa (http://yourmuni.appspot.com)

Full source code is available at: http://www.github.com/cmaul/MetroTransit-API/ 

Copyright (c) 2011 Corey Maul
 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


