import requests
import json


def getTotalGoals(team, year, competition):
    answer = 0

    API_URL = "https://jsonmock.hackerrank.com/api/football_mateches?year={}&team1={}&page=1".format(str(year), team)
    response = json.loads(requests.get(API_URL).text)
    for data in response.get("data"):
        if data["competition"] == competition:
            answer += int(data["team1goals"])

    for page in range(2, int(response.get("total_pages")) + 1):
        API_URL = "https://jsonmock.hackerrank.com/api/football_mateches?year={}&team1={}&page={}".format(str(year),
                                                                                                          team,
                                                                                                          str(page))
        response = json.loads(requests.get(API_URL).text)
        for data in response.get("data"):
            if data["competition"] == competition:
                answer += int(data["team1goals"])

    API_URL = "https://jsonmock.hackerrank.com/api/football_mateches?year={}&team2={}&page=1".format(str(year), team)
    response = json.loads(requests.get(API_URL).text)
    for data in response.get("data"):
        if data["competition"] == competition:
            answer += int(data["team2goals"])

    for page in range(2, int(response.get("total_pages")) + 1):
        API_URL = "https://jsonmock.hackerrank.com/api/football_mateches?year={}&team2={}&page={}".format(str(year),
                                                                                                          team,
                                                                                                          str(page))
        response = json.loads(requests.get(API_URL).text)
        for data in response.get("data"):
            if data["competition"] == competition:
                answer += int(data["team2goals"])

    return answer


def getWinnerTotalGoals(competition, year):
    # Write your code here
    API_URL = "https://jsonmock.hackerrank.com/api/football_competitions?name={}&year={}".format(competition, str(year))
    response = json.loads(requests.get(API_URL).text)
    team = response.get("data")[0]["winner"]
    return getTotalGoals(team, year, competition)


if __name__ == '__main__':
    competition = input()
    year = int(input().strip())
    result = getWinnerTotalGoals(competition, year)
    print(result)
