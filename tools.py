from datetime import datetime
import re
import pandas as pd


def update_data():
    """
    Updates dataset from manual input data
    """
    return (
        pd
        .read_csv('tabular.csv')
        .melt(id_vars='date',
              var_name='city',
              value_name='total_cases')
        .set_index('date')
        .fillna(value=0)
        .to_csv('dataset.csv')
    )
    

def load_dataset(cities=None):
    """
    Load dataset from SC cities. If a list of cities is given
    returns only the selected city data.
    """
    df = pd.read_csv('dataset.csv')
    if cities is None:
        return df
    else:
        return df[df['city'].isin(cities)]
    

def scrap_paragraph(paragraph, date=None, outside=0):
    """
    Extract SC cities total cases from daily bulletins.
    Is date is not given, gets the actual day.
    """
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')
    
    regexp = '([,e: ]+ )([\w ]+) (\([\d]+\))'
    occurrences = re.findall(regexp, paragraph)
    
    data = dict()
    data['date'] = [date]
    for city in occurrences:
        data[city[1]] = [int(city[2][1:-1])]
    
    data['Fora de SC'] = [outside]
    
    return pd.DataFrame(data)


def update_tabular(paragraph, date=None, outside=0):
    """
    Updates the saved tabular dataset with numbers
    scrapped from SC government bulletin.
    """
    old_df = pd.read_csv('tabular.csv')
    new_df = scrap_paragraph(paragraph, date, outside)
    
    return (
        pd
        .concat([old_df, new_df])
        .set_index('date')
        .to_csv('tabular.csv')
    )
