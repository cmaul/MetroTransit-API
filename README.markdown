# Metro Transit API

This API provides data from MetroTransit.org in a JSON encoded format.

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

    [{"code": "OAWA", "name": "Oak St SE and Washington Ave SE"}, {"code": "4S15", "name": "4th St SE and 15th Ave SE"}, {"code": "4SCE", "name": "4th St SE and Central Ave SE"}, {"code": "1S1A", "name": "1st Ave N and 1st St"}, {"code": "7SNI", "name": "Nicollet Mall and 7th St S"}, {"code": "8SHE", "name": "Hennepin Ave and 8th St"}, ... ]

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

Full source code is available at: http://www.github.com/cmaul/ 

Copyright (c) 2009 Corey Maul
 
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


