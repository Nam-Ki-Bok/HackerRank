#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json

#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#


def getTotalGoals(team, year, competition):
    answer = 0

    API_URL = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&team1=" + team + "&page=1"
    response = json.loads(requests.get(API_URL).text)
    for data in response.get("data"):
        if data["competition"] == competition:
            answer += int(data["team1goals"])

    for i in range(2, int(response.get("total_pages")) + 1):
        API_URL = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(
            year) + "&team1=" + team + "&page=" + str(i)
        response = json.loads(requests.get(API_URL).text)
        for data in response.get("data"):
            if data["competition"] == competition:
                answer += int(data["team1goals"])

    API_URL = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&team2=" + team + "&page=1"
    response = json.loads(requests.get(API_URL).text)
    for data in response.get("data"):
        if data["competition"] == competition:
            answer += int(data["team2goals"])

    for i in range(2, int(response.get("total_pages")) + 1):
        API_URL = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(
            year) + "&team2=" + team + "&page=" + str(i)
        response = json.loads(requests.get(API_URL).text)
        for data in response.get("data"):
            if data["competition"] == competition:
                answer += int(data["team2goals"])

    return answer


def getWinnerTotalGoals(competition, year):
    # Write your code here
    API_URL = "https://jsonmock.hackerrank.com/api/football_competitions?name=" + competition + "&year=" + str(year)
    response = json.loads(requests.get(API_URL).text)
    team = response.get("data")[0]["winner"]
    return getTotalGoals(team, year, competition)


if __name__ == '__main__':
    competition = input()
    year = int(input().strip())
    result = getWinnerTotalGoals(competition, year)
    print(result)