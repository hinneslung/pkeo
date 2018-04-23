import numpy as np
import pandas as pd

trade_df = pd.read_csv('./trade.csv')
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

df = pd.DataFrame(columns=['WarName', 'Year', 'Ccode1', 'Player1', 'Ccode2', 'Player2', 'Initiator', 'TradePercent'])
for index, row in war_df.iterrows():
    key = "percent1"
    trade = trade_df.loc[
        ((trade_df['ccode1'] == row['Ccode']) & (trade_df['ccode2'] == row['Ccode2'])) &
        (trade_df['year'] <= row['StartYear1'])
    ]
    if len(trade) <= 0:
        trade = trade_df.loc[
            ((trade_df['ccode2'] == row['Ccode']) & (trade_df['ccode1'] == row['Ccode2'])) &
            (trade_df['year'] <= row['StartYear1'])
        ]
        key = "percent2"
    percent = None
    if len(trade) > 0:
        percent = trade.loc[trade['year'].idxmax()][key]
    df.loc[index] = [row['WarName_x'], row['StartYear1'],
                     row['Ccode'], row['Player'], row['Ccode2'], row['Player2'], row['Initiator'],
                     percent]


df.to_csv('./war_pair-trade_percent.csv')
