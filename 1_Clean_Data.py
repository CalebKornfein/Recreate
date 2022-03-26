import pandas as pd
import math

# Load DataFrame
df = pd.read_csv('GFR.csv')

def GMR(row, pre):
    age, female, afr = row['Age'], row['Female'], row['African American']
    scr = row['sCR Pre'] if pre else row['sCR Post']
    
    gmr = 175 * (scr ** (-1.154)) * (age ** (-0.203))
    
    if female == 1:
        gmr = gmr * 0.742
    
    if afr == 1:
        gmr = gmr * 1.212
    
    return gmr

df['GMR Pre'] = df.apply(lambda x: GMR(x, True), axis=1)
df['GMR Post'] = df.apply(lambda x: GMR(x, False), axis=1)

df.to_csv('GFR2.csv',index=False)