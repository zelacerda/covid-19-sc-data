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
    

def scrap_paragraph(paragraph, date=None, pattern=1, outside=0):
    """
    Extract SC cities total cases from daily bulletins.
    Is date is not given, gets the actual day.
    
    Pattern=1 (default) is for texts like this:
    '...Blumenau (8), Usussanga (12), ...'
    
    Pattern=2 is for texts like this:
    '
    Joinville – 9
    Lages – 1
    Laguna – 1
    '
    
    """
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')
    
    if pattern == 1:
        regexp = '(?:[,e: ]+ )([\w ]+) (?:\()([\d]+)'
    elif pattern == 2:
        regexp = '(?:\\n)([\w ]+)(?: – )([\d]+)'
    
    occurrences = re.findall(regexp, paragraph)
    
    data = dict()
    data['date'] = [date]
    for o in occurrences:
        data[o[0]] = [int(o[1])]
    
    data['Fora de SC'] = [outside]
    
    return pd.DataFrame(data)


def update_tabular(paragraph, pattern=1, date=None, outside=0):
    """
    Updates the saved tabular dataset with numbers
    scrapped from SC government bulletin.
    """
    old_df = pd.read_csv('tabular.csv')
    new_df = scrap_paragraph(paragraph, date, pattern, outside)
    
    return (
        pd
        .concat([old_df, new_df])
        .set_index('date')
        .to_csv('tabular.csv')
    )
