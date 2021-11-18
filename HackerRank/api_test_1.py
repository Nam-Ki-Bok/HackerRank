#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#


def getTotalGoals(team, year, competition):
    answer = 0

    API_URL = "https://jsonmock.hackerrank.com/api/football_mateches?year={}&team1={}&page=1".format(str(year), team)
    response = json.loads(requests.get(API_URL).text)
    for data in response.get("data"):
        answer += int(data["team1goals"])

    for page in range(2, int(response.get("total_pages")) + 1):
        API_URL = "https://jsonmock.hackerrank.com/api/football_mateches?year={}&team1={}&page={}".format(str(year),
                                                                                                          team,
                                                                                                          str(page))
        response = json.loads(requests.get(API_URL).text)
        for data in response.get("data"):
            answer += int(data["team1goals"])

    API_URL = "https://jsonmock.hackerrank.com/api/football_mateches?year={}&team2={}&page=1".format(str(year), team)
    response = json.loads(requests.get(API_URL).text)
    for data in response.get("data"):
        answer += int(data["team2goals"])

    for page in range(2, int(response.get("total_pages")) + 1):
        API_URL = "https://jsonmock.hackerrank.com/api/football_mateches?year={}&team2={}&page={}".format(str(year),
                                                                                                          team,
                                                                                                          str(page))
        response = json.loads(requests.get(API_URL).text)
        for data in response.get("data"):
            answer += int(data["team2goals"])

    return answer


if __name__ == '__main__':
    team = input()
    year = int(input().strip())
    result = getTotalGoals(team, year)

    print(result)
