import numpy as np
import pandas as pd

diplomatic_df = pd.read_csv('./diplomatic.csv')
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
                           'Diplomatic'])

for index, row in war_df.iterrows():
    diplomatic = diplomatic_df.loc[
        (diplomatic_df['ccode1'] == row['Ccode']) & (diplomatic_df['ccode2'] == row['Ccode2']) &
        (diplomatic_df['year'] <= row['StartYear1']) & (diplomatic_df['year'] + 10 > row['StartYear1'])
    ]

    df.loc[index] = [row['WarName_x'], row['StartYear1'],
                     row['Ccode'], row['Player'], row['Ccode2'], row['Player2'],
                     len(diplomatic) > 0]


df.to_csv('./war_pair-diplomatic.csv')
