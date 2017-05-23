import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab as pl
from pylab import scatter, show, legend, xlabel, ylabel

"""Load the data files"""
with open("challenger.json") as openfile:
    data = json.load(openfile)
challenger_players_data = data
challenger_players_stats = []
num_master_players = 42

with open("master.json") as openfile:
    data = json.load(openfile)
master_players_data = data

with open("bronze.json") as openfile:
    data = json.load(openfile)
bronze_players_data = data

def clean_and_extract_stats(data):
    x = []
    for i in range(42):
        for j in range(10):
            if data[i][j]["gameMode"] == "CLASSIC":
                x.append(data[i][j]["stats"])
    return x

bronze_players_stats = clean_and_extract_stats(bronze_players_data)
master_players_stats = clean_and_extract_stats(master_players_data)
challenger_players_stats = clean_and_extract_stats(challenger_players_data)
print len(bronze_players_stats)
print len(master_players_stats)
print len(challenger_players_stats)
least_games = len(bronze_players_stats)

challenger_gold_earned = [challenger_players_stats[i]["goldEarned"]for i in range(least_games) if "goldEarned" in challenger_players_stats[i]]
challenger_gold_spent = [challenger_players_stats[i]["goldSpent"]for i in range(least_games) if "goldSpent" in challenger_players_stats[i]]
challenger_time = [challenger_players_stats[i]["timePlayed"]for i in range(least_games)]
challenger_dmg_taken = [challenger_players_stats[i]["totalDamageTaken"]for i in range(least_games) if "totalDamageTaken" in challenger_players_stats[i]]
challenger_dmg_dealt = [challenger_players_stats[i]["totalDamageDealtToChampions"]for i in range(least_games) if "totalDamageDealtToChampions" in challenger_players_stats[i]]
challenger_neutral_minions = [challenger_players_stats[i]["minionsKilled"] for i in range(least_games) if "minionsKilled" in challenger_players_stats[i]]
challenger_kills = [challenger_players_stats[i]["championsKilled"] for i in range(least_games) if "championsKilled" in challenger_players_stats[i]]
challenger_minions = [challenger_players_stats[i]["neutralMinionsKilled"] for i in range(least_games) if "neutralMinionsKilled" in challenger_players_stats[i]]
challenger_deaths = [challenger_players_stats[i]["numDeaths"] for i in range(least_games) if "numDeaths" in challenger_players_stats[i]]
challenger_wards = [challenger_players_stats[i]["visionScore"] for i in range(least_games) if "visionScore" in challenger_players_stats[i]]

def record_wins(d):
    if d == False:
        return 0
    else:
        return 1

challenger_wins = [record_wins(challenger_players_stats[i]["win"]) for i in range(least_games)]

master_gold_earned = [master_players_stats[i]["goldEarned"]for i in range(least_games) if "goldEarned" in master_players_stats[i]]
master_gold_spent = [master_players_stats[i]["goldSpent"]for i in range(least_games) if "goldSpent" in master_players_stats[i]]
master_time = [master_players_stats[i]["timePlayed"]for i in range(least_games)]
master_dmg_taken = [master_players_stats[i]["totalDamageTaken"]for i in range(least_games) if "totalDamageTaken" in master_players_stats[i]]
master_dmg_dealt = [master_players_stats[i]["totalDamageDealtToChampions"]for i in range(least_games) if "totalDamageDealtToChampions" in master_players_stats[i]]
master_neutral_minions = [master_players_stats[i]["minionsKilled"] for i in range(least_games) if "minionsKilled" in master_players_stats[i]]
master_minions = [master_players_stats[i]["neutralMinionsKilled"] for i in range(least_games) if "neutralMinionsKilled" in master_players_stats[i]]
master_kills = [master_players_stats[i]["championsKilled"] for i in range(least_games) if "championsKilled" in master_players_stats[i]]
master_deaths = [master_players_stats[i]["numDeaths"] for i in range(least_games) if "numDeaths" in master_players_stats[i]]
master_wins = [record_wins(master_players_stats[i]["win"]) for i in range(least_games)]
master_wards = [master_players_stats[i]["visionScore"] for i in range(least_games) if "visionScore" in master_players_stats[i]]

bronze_gold_earned = [bronze_players_stats[i]["goldEarned"]for i in range(least_games) if "goldEarned" in bronze_players_stats[i]]
bronze_gold_spent = [bronze_players_stats[i]["goldSpent"]for i in range(least_games) if "goldSpent" in bronze_players_stats[i]]
bronze_time = [bronze_players_stats[i]["timePlayed"]for i in range(least_games)]
bronze_dmg_taken = [bronze_players_stats[i]["totalDamageTaken"] for i in range(least_games) if "totalDamageTaken" in bronze_players_stats[i]]
bronze_dmg_dealt = [bronze_players_stats[i]["totalDamageDealtToChampions"]for i in range(least_games) if "totalDamageDealtToChampions" in bronze_players_stats[i]]
bronze_neutral_minions = [bronze_players_stats[i]["minionsKilled"] for i in range(least_games) if "minionsKilled" in bronze_players_stats[i]]
bronze_minions = [bronze_players_stats[i]["neutralMinionsKilled"] for i in range(least_games) if "neutralMinionsKilled" in bronze_players_stats[i]]
bronze_kills = [bronze_players_stats[i]["championsKilled"] for i in range(least_games) if "championsKilled" in bronze_players_stats[i]]
bronze_deaths = [bronze_players_stats[i]["numDeaths"] for i in range(least_games) if "numDeaths" in bronze_players_stats[i]]
bronze_wins = [record_wins(bronze_players_stats[i]["win"]) for i in range(least_games) if "win" in bronze_players_stats[i]]
bronze_wards = [bronze_players_stats[i]["visionScore"] for i in range(least_games) if "visionScore" in bronze_players_stats[i]]

def clean_minions_stats(x, y, target):
    if len(x) > len(y):
        for i in range(len(x) - len(y)):
            y.append(0)
        for i in range(len(x)):
            y[i] += x[i]
            target.append(y[i])
        return target
    elif len(y) > len(x):
        for i in range(len(y) - len(x)):
            x.append(0)
        for i in range(len(y)):
            x[i] += y[i]
            target.append(x[i])
        return target

bronze_cleaned_minions = []
challenger_cleaned_minions = []
master_cleaned_minions = []

clean_minions_stats(bronze_neutral_minions, bronze_minions, bronze_cleaned_minions)
clean_minions_stats(challenger_neutral_minions, challenger_minions, challenger_cleaned_minions)
clean_minions_stats(master_neutral_minions, master_minions, master_cleaned_minions)

df = pd.DataFrame([challenger_cleaned_minions, master_cleaned_minions, challenger_kills, master_kills, challenger_time,
                   master_time, challenger_deaths,master_deaths, challenger_gold_earned, master_gold_earned,
                   challenger_gold_spent, master_gold_spent, challenger_dmg_taken, master_dmg_taken,
                   challenger_wards, master_wards, challenger_dmg_dealt, master_dmg_dealt])
df.head()

df = df.transpose()
df.columns = ["challenger_minions", "master_minions", "challenger_kills", "master_kills", "challenger_time",
              "master_time", "challenger_deaths","master_deaths", "challenger_gold_earned", "master_gold_earned",
              "challenger_gold_spent", "master_gold_spent", "challenger_dmg_taken", "master_dmg_taken",
              "challenger_wards", "master_wards", "challenger_dmg_dealt", "master_dmg_dealt"]
df.head()
df = df.fillna(0)

df2 = pd.DataFrame([bronze_cleaned_minions, bronze_kills, bronze_time,
                    bronze_deaths, bronze_gold_earned, bronze_gold_spent,
                    bronze_dmg_taken, bronze_wards, bronze_dmg_dealt])
df2 = df2.transpose()

df2.fillna(0)
df2.columns = ["bronze_minions", "bronze_kills", "bronze_time", "bronze_deaths",
               "bronze_gold_earned","bronze_gold_spent", "bronze_dmg_taken", "bronze_wards", "bronze_dmg_dealt"]
df2.describe()
