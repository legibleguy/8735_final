import numpy as np
import pandas as pd

def get_data():
    df = pd.read_csv('FPS Video Games.csv', low_memory=False)
    return df

def cost_per_frame(game):

    #read the gpu prices database
    gpu_prices = {}
    gpu_prices_df = pd.read_csv('gpu_prices.csv')
    for index, row in gpu_prices_df.iterrows():
        gpu_prices[row['GpuName']] = row['Price']
    
    #read the cpu prices database
    cpu_prices = {}
    cpu_prices_df = pd.read_csv('cpu_prices.csv')
    for index, row in cpu_prices_df.iterrows():
        cpu_prices[row['CpuName']] = row['Price']

    db = get_data()
    db = db[db['GameName'] == game]
    db = db[['GpuName', 'CpuName', 'FPS']]
    db = db.dropna()
    db['GpuCost'] = db['GpuName'].map(gpu_prices)
    db['CpuCost'] = db['CpuName'].map(cpu_prices)
    db['CostPerFrame'] = (db['GpuCost'] + db['CpuCost']) / db['FPS']
    db = db[['GpuName', 'CpuName', 'GpuCost', 'CpuCost', 'CostPerFrame', 'FPS']]
    return db

game_name = input('Enter a game name: ')

db_cost_per_frame = cost_per_frame(game_name)
#save the database to a csv file
db_cost_per_frame.to_csv('cost_per_frame_' + game_name + '.csv', index=False)