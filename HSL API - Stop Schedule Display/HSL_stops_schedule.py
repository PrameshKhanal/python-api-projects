#========================================================================================================================================#
# Simple Python project that displays the bustop schedule on the output console. This Project utilizes the API and data from             #
# Digitransit (© Digitransit 2024).                                                                                                      #
#                                                                                                                                        #
# Digitransit Platform, an open-source journey planning solution, amalgamates various open-source components for route planning.         #
# It features a mobile-friendly user interface, map tile serving, geocoding, and data conversion tools.                                  # 
# Route planning algorithms and APIs are powered by Open Trip Planner (OTP). For more information about Digitransit,                     #
# visit: https://digitransit.fi/en/. Digitransit is supported by Helsinki Region Transportation (HSL), Fintraffic,and Waltti Solutions   #
# Oy                                                                                                                                     #
#========================================================================================================================================#


import json
from datetime import datetime, timedelta
import time
from pytz import timezone
from prettytable import PrettyTable
import pytz
import os
import urllib.request

# Function that returns converts the UNIX date and time to Heksinki timezone
def convert_date_time(unix_date,unix_time):
  utc = pytz.utc
  fmt = '%a %d-%b-%Y'
  time_fmt = '%H:%M:%S'
  utc_dt = utc.localize(datetime.utcfromtimestamp(unix_date))
  utc_time = utc.localize(datetime.utcfromtimestamp(unix_time))
  hki_tz = timezone('Europe/Helsinki')
  hki_dt = utc_dt.astimezone(hki_tz)
  return hki_dt.strftime(fmt), utc_time.strftime(time_fmt)

def main():
  # GraphQL query
  graphql_query = '''
    query GetStops($stopName: String!) {
      stops(name: $stopName) {
      name
      stoptimesWithoutPatterns(numberOfDepartures: 5) {
        serviceDay
        scheduledArrival
        realtimeArrival
        arrivalDelay
        trip {
          route {
            shortName
          }
        }
        headsign
      }
    }
  }
  '''
  # Variable values
  variables = {
    "stopName": "V6110" # V6110 is the stop ID and can be modified according to need
  }

  # Request payload
  payload = {
    "query": graphql_query,
    "variables": variables
  }
  api_endpoint = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"

  # Get subscription key from environment variable
  subscription_key = os.environ.get('HSL_SUBSCRIPTION_KEY')

  if not subscription_key:
    raise ValueError("HSL_SUBSCRIPTION_KEY environment variable not set.")
  
  # Request headers
  hdr = {
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache',
    'digitransit-subscription-key': subscription_key,
  }

  # Convert payload to JSON
  data = json.dumps(payload).encode('utf-8')
  req = urllib.request.Request(api_endpoint, data=data, headers=hdr, method='POST')
  response = urllib.request.urlopen(req)

  # Perform action only if status code = 200
  if response.status == 200:
    json_response = response.read().decode('utf-8')
    parsed_response = json.loads(json_response)

    try:
      table = PrettyTable()
      # Create the table headers
      table.field_names = ['Service Day', 'Route Number', 'Scheduled arrival', 'Real time arrival', 'Delay']

      for index in range(5):
        schArrival_Date  = parsed_response['data']['stops'][0]['stoptimesWithoutPatterns'][index]['serviceDay']
        schArrival_time  = parsed_response['data']['stops'][0]['stoptimesWithoutPatterns'][index]['scheduledArrival']
        realArrival_time = parsed_response['data']['stops'][0]['stoptimesWithoutPatterns'][index]['realtimeArrival']
        delay_time       = parsed_response['data']['stops'][0]['stoptimesWithoutPatterns'][index]['arrivalDelay']
        route_number     = parsed_response['data']['stops'][0]['stoptimesWithoutPatterns'][index]['trip']['route']['shortName']

        schArrivalDate, schArrivalTime   = convert_date_time(schArrival_Date,schArrival_time)
        realArrivalDate, realArrivalTime =  convert_date_time(schArrival_Date,realArrival_time)
        delayDate, delayTime = convert_date_time(schArrival_Date,abs(delay_time))

        # If UNIX delay time is -ve
        if delay_time < 0:
          table.add_row([schArrivalDate, route_number, schArrivalTime, realArrivalTime, (delayTime + ' Early')])
        # If UNIX delay time is 0 or if there is no delay
        elif delay_time == 0:
          table.add_row([schArrivalDate, route_number, schArrivalTime, realArrivalTime, delayTime])
        # If UNIX delay time is +ve
        else:
          table.add_row([schArrivalDate, route_number, schArrivalTime, realArrivalTime, (delayTime + ' Late')])
      print(f'{datetime.now().strftime("%H:%M:%S")}\n{table}') # Prints the current time and the schedule table

    except Exception as e:
      print(e)
  else:
    print(f"Request failed with status code: {str(response.status)}")

if __name__ == "__main__":
  while True:
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the output console
    main()
    time.sleep(3) # Loops over the main() function every 3s
