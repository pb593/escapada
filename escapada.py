#!/usr/local/bin/python3

import json, sys
from urllib.request import urlopen, Request, HTTPError

originLoc = "LON"
targetLocs = ["VIE", "MUC", "FMM", "ZRH", "RIX", "KRK", "BUD", "PRG", "BUH", "BEG", "LIS", "BER", "BRU", "MAD", "MSQ", "BCN", "TLL", "DUB", "WAW", "REK", "OSL"]
revisitLocs = ["MOW", "LED", "MIL", "PAR", "VCE", "AMS", "STO"]
url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyCnnbZb8aZYszdjkg9W0mlWeh0HCT2zTDw"



if __name__ == "__main__":
    requestObj = {
      "request": {
        "slice": [
          {
            "origin": originLoc,
            "destination": "PAR",
            "date": "2017-03-10",
            "maxStops": 0,
            "permittedDepartureTime": {
              "earliestTime": "17:00"
            }
          },
          {
            "origin": "PAR",
            "destination": originLoc,
            "date": "2017-03-12",
            "maxStops": 0,
            "permittedDepartureTime": {
              "earliestTime": "14:00"
            }
          }
        ],
        "passengers": {
          "adultCount": 1,
          "infantInLapCount": 0,
          "infantInSeatCount": 0,
          "childCount": 0,
          "seniorCount": 0
        },
        "solutions": 100,
        "maxPrice": "GBP100",
        "refundable": "false"
      }
    }
    jsonreq = json.dumps(requestObj).encode('utf8')
    req = Request(url, jsonreq, {'Content-Type': 'application/json'})
    try:
        flight = urlopen(req)
        response = flight.read().decode("UTF-8")
        flight.close()
    except HTTPError as e:
        print("Exception happened: %s\n" % e.msg)
        sys.exit(-1)

        jsonObj = json.loads(response)
        for flightOption in jsonObj["trips"]["tripOption"]:
            print("%s\n" % flightOption["saleTotal"])
    