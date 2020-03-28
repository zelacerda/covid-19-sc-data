import pandas as pd


def update_data():
    """
    Updates dataset from manual input data
    """
    return (
        pd
        .read_csv('manual.csv')
        .drop('TOTAL', axis=1)
        .melt(id_vars='date',
              var_name='city',
              value_name='total_cases')
        .set_index('date')
        .fillna(value=0)
        .to_csv('dataset.csv')
    )
    

def load_dataset(cities=None):
    """
    Load dataset from SC cities. If a list of cities is given, returns
    only the selected city data.
    """
    df = pd.read_csv('dataset.csv')
    if cities is None:
        return df
    else:
        return df[df['city'].isin(cities)]