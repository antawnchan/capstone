"Specific Aim"
Predict game results given player game logistic

"Revised"
Predict each player's score given game log given game/teams
Sum up all scores to accumulate a game score between 2 teams,
compare it with actual game score and point spread.
Baseline: Point spread is always a 50% chance of winning.

"Proposed Methods and models"
Use Logistic Regression, Random Forest or other classification models for who won.
Use Linear Regression or other regression models to calculate player score.

"Risks and Assumptions"
Risks: A lot of advanced stats is a calculated result from the basic stats. Need to streamline columns.
Risks: It's possible that predictions will overestimate game score. It does not take into account (at least for now) recently played games or opponents defense.
Assumptions: The model will need to generate some data in order to input values for to calculate a score.

"Data Cleaning"
-Remove all na's for rows, cols for any % (such as 0/0 ft)
-Set some baseline on minutes played.

"Data Dictionary"
see csv files

"Perform & summarize EDA"
Performed EDA on column categories using Random Forest, Lasso/Ridge, Logistic and Linear.

Summarize:
Game result (win/loss, 0/1)
High correlations: fg, fga, 3p, 2p, 2pa, ft, fta, tov, usg, ows
Negative correlations: dws, orb, drb, assumptions

Game spread (win by x points): predict player scores
Ridge:
High correlation: ast, +/-, trb%, offrtg
Negative correlations: ts%, drb%, ast%, defrtg
Lasso:
high correlation: fga, ast, +/-, trb%, tov%, offrtg
negative correlation: orb, ts%, orb%, drb%, ast%, defrtg

categories to drop:
blk, blk%
pick between trb and (orb, drb), since trb = orb+drb
probably go with trb
debating on dropping +/-
will choose ts_pct over eFG_pct
