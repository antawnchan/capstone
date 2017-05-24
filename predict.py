import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, LassoCV, Ridge, RidgeCV


class predict_player:

    player_url = "Green_Draymond"
    opp_team = "SAS"
    last_x_games = -5
    playoff_game = 1

    def __init__(self, player_url = "Green_Draymond", opp_team = "SAS", last_x_games = -5, playoff_game = 1):
        self.player_url   = player_url
        self.opp_team     = opp_team
        self.last_x_games = last_x_games
        self.playoff_game = playoff_game

        self.printMe()


    def printMe(self):
        print self.player_url
        print self.opp_team
        print self.last_x_games
        print self.playoff_game