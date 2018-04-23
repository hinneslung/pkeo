import numpy as np
import pandas as pd

religion_df = pd.read_csv('./state-religion.csv')
war1_df = pd.read_csv('./inter_state_war.csv')
war2_df = pd.read_csv('./inter_state_war.csv')

war2_df.rename(columns={
    'Ccode': 'Ccode2', 'Player': 'Player2',
    'StartMonth1': 'StartMonth2', 'StartDay1': 'StartDay2', 'StartYear1': 'StartYear2',
    'EndMonth1': 'EndMonth2', 'EndDay1': 'EndDay2', 'EndYear1': 'EndYear2',
    'Side': 'Side2', 'Initiator': 'Initiator2', 'WhereFought': 'WhereFought2',
    'Outcome': 'Outcome2', 'BatDeath': 'BatDeath2'}, inplace=True)

war_df = pd.merge(war1_df, war2_df, how='outer', on=['WarNum'])
war_df = war_df.loc[(war_df.Ccode != war_df.Ccode2) & (war_df.Side != war_df.Side2)]

df = pd.DataFrame(columns=['WarName', 'Year', 'Ccode1', 'Player1', 'Ccode2', 'Player2',
                           'Religion1', 'Religion2', 'Initiator'])

for index, row in war_df.iterrows():
    key = "percent1"
    religion1 = religion_df.loc[religion_df['Ccode'] == row['Ccode']]['Major'].max()
    religion2 = religion_df.loc[religion_df['Ccode'] == row['Ccode2']]['Major'].max()

    df.loc[index] = [row['WarName_x'], row['StartYear1'],
                     row['Ccode'], row['Player'], row['Ccode2'], row['Player2'],
                     religion1, religion2, row['Initiator']]


df.to_csv('./war_pair-religion.csv')
