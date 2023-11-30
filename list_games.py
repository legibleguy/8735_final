import pandas as pd

def get_data():
    df = pd.read_csv('FPS Video Games.csv', low_memory=False)
    return df

def get_all_games():
    db = get_data()
    games = db['GameName'].unique()
    return games

print(get_all_games())