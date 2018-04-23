import numpy as np
import pandas as pd


def load_dated_data(path, date_format='%d-%m-%Y %H:%M:%S'):
    date_parser = lambda x: pd.datetime.strptime(x, date_format)
    data = pd.read_csv(path, header=0, index_col=0, parse_dates=['Time'], date_parser=date_parser)
    return data


def load_data(path):
    return pd.read_csv(path, header=0, index_col=0)


f = {
    'WarName': ['first'],
    'WarType': ['first'],
    # 'Ccode': ['list'],
    # 'Player': ['list'],

    'StartMonth': ['min'],
    'StartDay': ['min'],
    'StartYear': ['min'],
    'EndMonth': ['max'],
    'EndDay': ['max'],
    'EndYear': ['max'],

    # 'WhereFought': ['list'],
    'Death': ['sum'],
}


df = pd.read_csv('./war-state-date-death.csv')
grouped = df.groupby(['WarNum'])
aggregated = grouped.agg(f)

aggregated['Ccode'] = grouped['Ccode'].apply(list)
aggregated['Player'] = grouped['Player'].apply(list)
aggregated['WhereFought'] = grouped['WhereFought'].apply(set)

aggregated.to_csv('./wars.csv')
