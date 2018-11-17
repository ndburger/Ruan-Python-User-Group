
# GA01 Team Coordination and Collaboration

This project is a simulation. In this simulation, you are working as part of a programming team for PyTastic Inc., a company that provides custom programs to meet client needs. In this case, our client (MegaResearch Inc.) is looking for a program which they can use to extract weather data. Our customer requires a command line interface to our program so that it can be integrated into a large data collection system they are developing (and for which we hope to get more future projects).

You are a member of one of four PyTastic teams (Apex, Elite, Pinnacle, Ultimate) competing to provide the solution that we (PyTastic Inc.) present to our customer. The deadline to complete this project in 3 weeks (due before 5 PM September 24th).

This simulation will test your introductory Python programming skills and ability to utilize Git, GitHub, and Slack to coordinate and work as a team to write a program.

## Program Requirements:

MegaResearch Inc. requires a CLI (command line interface) to a program that returns data about current and past weather conditions in Ames. This program will provide temperature, humidity, pressure, wind speed, and direction measures in either metric or USCS (see: https://en.wikipedia.org/wiki/Imperial_and_US_customary_measurement_systems).

This program will be called AmesWeather, and must accept a string of arguments that specify the measures to return.
* `AmesWeather (<date> | "") (-M | "") (measure(-timeoffset | ""))`

This program must also provide help and version information:
* `AmesWeather (-h | --help | --version)`


CLI Parameters:
* `(<datetime> | "")`  - optional date. default is current date-time.
  * DateTime format 'MM/DD/YYYY:HH:MM' where MM/DD/YYYY is the date, and HH::MM is * the time in 24hr format. )
* `(-M | "")` - provide measures using metric system, default is USCS.
* `(measure(-timeoffset | "")...)` - List of measures with optional time-offset
  * Where:
    * Measure: { P | T | WS | WD }
      * P = pressure
      * T = temperature
      * WS = wind speed
      * WD = wind direction
    * Time-offset: {Y | M | W | D}
      * Y = year
      * M = month
      * W = week
      * D = day

The output should be the resulting requested data as a comma separated string. Any data not available should be shown as NA.

## Usage Examples:

Provide current temperature in Fahrenheit:
```
$python AmesWeather.py T
78.3
```

Provide temperature (Fahrenheit) yesterday, last week, and last year at this time:
```
$python AmesWeather.py T-D
73.3
$python AmesWeather.py T-W
75.2
$python AmesWeather.py T-Y
71.2
```

Provide current - [ ] temperature in Celsius:
```
$python AmesWeather.py -M T
25.7
```

Wind speed in km/h (kilometers per hour) on Monday, June 10, 2015 at 10 AM.
for
```
$python AmesWeather.py 6/10/2015:10:00 -M WS
5
```

Wind speed in km/h (kilometers per hour) and Temperature (Celsius) on Monday, June 10, 2015 at 10 AM, and one month before
for
```
$python AmesWeather.py 6/10/2015:10:00 -M WS WS-M T T-M
12.2,10.0,22.2,24.5
```

Wind speed in mph and Temperature (Fahrenheit) on  February 12, 2005 at 5:37 PM, and one day, month and year before
for
```
$python AmesWeather.py 02/12/2015:17:37 WS WS-M WS-D WS-Y T T-D T-M T-Y
10.2,2.3,NA,28.2,25.2,22.1,NA
```
NOTE: The measures shown in the usage examples above are not real numbers, but numbers fabricated to illustrate functionality. Your program will provide actual measures from these, and any other dates, selected.


## Program structure

You must follow the following program structure as outlined below. You can add more files to this structure if needed, but I you be required to have the following set of files:
```
/GA01
    README.md
    instructions.md
    contributors.md
    AmesWeather.py
    test_suite/
        test_script.py
        test_case_1.md
        test_case_2.md
        test_case_3.md
        test_case_4.md
        test_case_5.md
    weather/
        __init__.py
        historical.py
        current.py
```

You will create a package called 'weather'. In this package will be two modules - current and historical. Each of these modules will provide a programmer-friendly interface to historical and current weather data. The specific details about the data source and its format should be hidden in such a way that we can easily change the data source without requiring any of the code in AmesWeather.py to be rewritten  (see the concept of [abstraction](https://en.wikipedia.org/wiki/Abstraction_(software_engineering)), if you're not already familiar).

* __instructions.md__ should introduce the program and provide a user with enough information to run your application.
* __contributors.md__ should list each team member, and provide a short introduction to their role and contribution to this project (NOTE: This will require you to think about how you will distribute your work to optimize your team's capacity to accomplish work.)
* __AmesWeather.py__ is your main program that the user will run
* __test_suite__ is a directory in which you will place a file for each of at least 5 test cases used to verify the functionality of the application you've developed and a test_script.py which will run and verify the results from each of your chosen test cases. You will document some of the tests you conducted using the Test case format outlined below.
* The __weather__ folder will contain your package, which will consist of the two required modules (historical and current)

__NOTE__: Tests case format:
* Test Case #x:
    * state objective.
    * state the command being tested
    * state expected output
    * state the observed output.
    * Pass/fail Date and Version tested. (hint: these should all pass :) )

## Background:

There are both commercial and public sources of weather data. You're welcome to use any data source available on the web for this project. Though there are commercial data sources available, all the data you will need for this project is freely available.

I'd recommend using the following two: KAMW weather station data and OpenWeatherMap (a commercial provider of data - but, does offer free access to some of it's data)

### Public Weather Data:
 There are publicly available sources of historical weather data for Ames. Do a little research on this. Also, depending on your sources, you may need to parse METAR data format https://en.wikipedia.org/wiki/METAR. HINT: Is there a Python package that will help to process METAR data? Search GitHub and PyPI.

### OpenWeatherMap

OpenWeatherMap.org provides a number of useful API's to extract weather and climate data (see api.openweathermap.org ). To access this data via their API, you will need an API key. Each team will need to obtain a key for their application. To obtain this key, you register with [OpenWeatherMap](https://home.openweathermap.org/users/sign_in). The registration is free. (NOTE: Some sources of their data require a subscription, but we are only interested in using the free data. You do not need to pay for a subscription.)

The data you receive from these OpenWeatherMap API's are in json format. I've developed the following snippet of example code to help you get started.

```Python
>>> import requests
>>> r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Ames&APPID=YourTeamsOpenweathermapAppIDgoesHere')
>>> wdata=r.json()
>>> print(wdata)
{'coord': {'lon': -93.62, 'lat': 42.03}, 'sys': {'message': 0.0301, 'sunrise': 1472730071, 'id': 845, 'country': 'US', 'type': 1, 'sunset': 1472777173}, 'id': 4846834,
'name': 'Ames', 'dt': 1472737586, 'visibility': 16093, 'clouds': {'all': 1}, 'main': {'temp': 287.73, 'temp_min': 286.15, 'temp_max': 289.82, 'pressure': 1024, 'humidit
y': 93}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'wind': {'deg': 360, 'speed': 1.5}, 'base': 'stations', 'cod': 200}
>>> from pprint import pprint
>>> pprint(wdata)
{'base': 'stations',
 'clouds': {'all': 1},
 'cod': 200,
 'coord': {'lat': 42.03, 'lon': -93.62},
 'dt': 1472737586,
 'id': 4846834,
 'main': {'humidity': 93,
          'pressure': 1024,
          'temp': 287.73,
          'temp_max': 289.82,
          'temp_min': 286.15},
 'name': 'Ames',
 'sys': {'country': 'US',
         'id': 845,
         'message': 0.0301,
         'sunrise': 1472730071,
         'sunset': 1472777173,
         'type': 1},
 'visibility': 16093,
 'weather': [{'description': 'clear sky',
              'icon': '01d',
              'id': 800,
              'main': 'Clear'}],
 'wind': {'deg': 360, 'speed': 1.5}}
>>> type(wdata)
<class 'dict'>
>>> wdata['coord']
{'lon': -93.62, 'lat': 42.03}
>>> wdata['id']
4846834
>>> wdata['sys']
{'message': 0.0033, 'sunrise': 1472730071, 'id': 845, 'country': 'US', 'type': 1, 'sunset': 1472777174}
>>> wdata['clouds']
{'all': 1}
>>> wdata['main']
{'temp': 288.13, 'temp_min': 286.15, 'temp_max': 289.82, 'pressure': 1024, 'humidity': 93}
>>> wdata['name']
'Ames'
>>> wdata['dt']
1472736386
>>> wdata['weather']
[{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]
>>> wdata['wind']
{'deg': 360, 'speed': 1.5}
>>> wdata['base']
'cmc stations'
>>> wdata['cod']
200
>>> wdata['main']['temp']
288.13
>>>

```


## Rubric:

### Criteria #1: (Weighting 20%) Evidence of collaboration and usage of the provided tools:
I will review the teams gitHub repo log. I'm looking for every team member to have made a contribution. I'm also looking for evidence of strong use of branches and releases to manage the project through completion. I'm also looking for evidence that Slack was used to help organize project work (you'll be assigned to a private channel for your team communication). Finally, I will review the contributions.md file for evidence of organizational ability and focus (that is, some indication of roles, and splitting of work across the team)

Recommendations: Commit often, release once in a while (but use releases), branch development work, merge released work and have everyone contribute changes to the repo.

### Criteria #2: (Weighting 20%) Evidence of knowledge about python coding style conventions, syntax, and organization using modules and packages:

I'm looking for broad rich use of the Python language (using fully the concepts we covered in class). Your program must be organized into a structure with at least 2 modules, organized into a single package, and run by a central .py file called AmesWeather.py (see directory structure outlined above). I will use a linter to determine the level of code compliance with PEP8 (I'm not looking for perfect alignment, but general alignment - as PEP8 states, "Foolish Consistency is the Hobgoblin of Little Minds" there are times when it makes sense to do something different - but make sure you know that you are taking liberties with the style, and limit this to as few exceptions as possible.).

### Criteria #3: (Weighting 20%) Error Handling and Evidence of good Design Choices

Your program should recognize and handle errors gracefully. Also, as with any "real world" programming requirements, some reasonable design choices must be made.  These choices should not violate the requirements, but rather, address the inherent "whitespace" the exists in any requirements set. (i.e. handling of a leap-year is not in the requirements, therefore must be a design decision: there will be other similar dilemmas faced. Be sure to document such behavior in your user instructions)

### Criteria #4: (weighting 30%) Quality of Program

The code works properly and properly and adequately addresses the requirements given. It uses appropriate data sources that produce the best available results. Feel free to add extra functionality, but I must see the basic functionality outlined in this assignment.

### Competitive Assessment: 0-10%

In this simulation, you are competing against other teams to supply the solution to our customer. Based on the evaluation of the first four criteria, the four teams will be ranked. The highest team will receive 10 points, the second highest 7.5, the third, 5.0, and the fourth 2.5.

## WOW Factor: Possible 10 bonus points

The “WOW factor” is a reward for exceptional work that adds exceptional and useful functionality that goes beyond the stated requirements. This bonus is at my discretion; not all additional functional will be considered "good" additions to the program.

## NOTE ON QUESTIONS AND CLARIFICATIONS:
As part of this simulation, I'll be playing the role of your manager at PyTastic Inc. I will be a source of information and help, but like in any business environment, if you utilize too much of my time (asking unnecessary questions, or questions you could have answered yourself with a bit of work) it will affect your team assessment.


#### NOTE ON TEAM MEMBER PARTICIPATION:
My expectation is that all team members will participate fully in the project, as evidenced by GitHub commits, Slack postings, and other indicators. It may happen that one of your team members drops out or does not participate. If this is an issue, I would ask that before you contact me, that you make every effort to work things out as a team. Only after you've exhausted this avenue should you request that I intervene/mediate.
