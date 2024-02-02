# Python API Projects
## Table of Contents
* [Introduction](https://github.com/PrameshKhanal/python-api-projects/blob/main/README.md#introduction)
* [Modules, Libraries and Installations](https://github.com/PrameshKhanal/python-api-projects#modules-libraries-and-installations)
* [HSL API - Stop Schedule Display](https://github.com/PrameshKhanal/python-api-projects/blob/main/README.md#hsl-api---stop-schedule-display)
## Introduction
### 🚀 API Fun Projects

Welcome to my API Fun Projects repository! Here, I create small Python projects using different public APIs.

### 🔍 Explore the Subfolders:
* Each subfolder has a different project, showing how to use APIs in Python.
* Check out the code to see how I make interesting things with data from various APIs.

### 🛠️ Learning and Trying Out:
* These projects are my way of learning and trying out new things with Python and APIs.
* See how to get, process, and show data from different APIs while improving your coding skills.

### 🌟 Get Involved:
* Explore, add your own touch, or share your ideas.
* I'd love to hear your thoughts and ideas to make these projects even better.

### 🚧 Still Building:
* This repository is always changing as I add new projects. Keep an eye out for updates!

[Back to Top](#table-of-contents)
  
## Modules, Libraries and Installations
The modules and libraries can be installed using the [Python package installer 'pip'](https://pypi.org/project/pip/)
- **json**
  - **Official Link:** [json - Python Standard Library](https://docs.python.org/3/library/json.html)
  - **Installation:**

    Python has a built-in package called _json_, which can be used to work with JSON data

- **datetime, timedelta, time**
  - **Official Link:** [datetime - Python Standard Library](https://docs.python.org/3/library/datetime.html)
  - **Installation:**

    Python has a module named _datetime_ to work with dates and times

- **pytz**
  - **Official Link:** [pytz - World Timezone Definitions for Python](https://pypi.org/project/pytz/)
  - **Installation:**
    ```bash
    pip install pytz
    ```

- **PrettyTable**
  - **Official Link:** [PrettyTable - A Simple Python Library for Table Representation](https://github.com/jazzband/prettytable)
  - **Installation:**
    ```bash
    python -m pip install -U prettytable
    ```

- **os**
  - **Official Link:** [os - Python Standard Library](https://docs.python.org/3/library/os.html)
  - **Installation:**
  
    Built-in _os_ module

- **urllib.request**
  - **Official Link:** [urllib.request - Python Standard Library](https://docs.python.org/3/library/urllib.request.html)
  - **Installation:**
    ```bash
    pip install urllib
    ```
[Back to Top](#table-of-contents)

## HSL API - Stop Schedule Display
The Python program utilizes the Digitransit's [Routing API](https://digitransit.fi/en/developers/apis/1-routing-api/) to display the stop/station schedule using [GraphQL query](https://digitransit.fi/en/developers/apis/1-routing-api/stops/#query-stops-by-name-or-number). The variable definition `"stopName": "V6110"` can be modified to include the desired name of the stops. To be able to access the API, user needs to [register and use the API keys](https://digitransit.fi/en/developers/api-registration/). In this case, the API key is accesed from environment variable using `subscription_key = os.environ.get('HSL_SUBSCRIPTION_KEY')`. API request was sent using `urllib.request` and the data is stored in `json` format in the `parsed_response` variable. The UNIX date and time information from the `parsed_response` variable are first stored in 4 different variable, converted to Helsinki timezone using the `convert_date_time()` function and added in the table. 


### Program output | [VIEW FILE](https://github.com/PrameshKhanal/python-api-projects/blob/main/HSL%20API%20-%20Stop%20Schedule%20Display/HSL_stops_schedule.py)
* `Route Number`: displays the bus/train/tram numbers for a stop (in this case `V6110` stop)
* `Scheduled arrival`: displays the secheduled arrival time
* `Real time arrival`: displays the real time arrival at the stop
* `Delay`: displays the delay based on the `Scheduled` and `Real time` arrivals

![schedule_display](https://github.com/PrameshKhanal/python-api-projects/assets/7952696/b5def655-de96-47bb-aceb-70707d2b216b)

[Back to Top](#table-of-contents)
