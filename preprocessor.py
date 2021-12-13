import pandas as pd



def preprocess(df, region_df):
   # global df, region_df
    #filter based on Summer
    df = df[df['Season'] == 'Summer']
    #merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    #drpping duplicates
    df.drop_duplicates(inplace=True)
    #one hot encoding medals
    df=pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    df = df.rename(columns={'Name': 'Athlete'})
    return df