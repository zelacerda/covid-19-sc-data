from datetime import datetime
import re
import pandas as pd


"""
regex_pattern stores different patterns to find data from text.

Pattern 1 is for texts like this:
    
...Blumenau (8), Usussanga (12), ...

Pattern 2 is for texts like this:

Joinville – 9
Lages – 1
Laguna – 1

Pattern 3 is for texts like this:

Joinville 9
Lages 1
Laguna 1 
"""
regex_pattern = {
    1: '(?:[,e: ]+ )([\w ]+) (?:\()([\d]+)',
    2: '(?:\\n)([\w ]+)(?: [–-]? )([\d]+)',
    3: '(?:\\n)([\w ]+)(?: )([\d]+)'
}


def today():
    return datetime.today().strftime('%Y-%m-%d')


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
    

def find_pattern(text):
    max_value = 0
    max_item = 1
    for item, pattern in regex_pattern.items():
        match_occurences = len(re.findall(pattern, text))
        if match_occurences > max_value:
            max_value = match_occurences
            max_item = item
    return max_item
    

def scrap_text(text, pattern=None):
    """
    Extract SC cities total cases from daily bulletins.
    Is date is not given, gets the actual day.  
    """  
    if pattern is None:
        regexp = regex_pattern[find_pattern(text)]
    else:
        regexp = regex_pattern[pattern]
    
    occurrences = re.findall(regexp, text)
    
    data = dict()
    for o in occurrences:
        data[o[0]] = [int(o[1])]
  
    return data


def update_tabular(text, date=None, pattern=None):
    """
    Updates the saved tabular dataset with numbers
    scrapped from SC government bulletin.
    """
    if date is None:
        date = today()
        
    old_df = pd.read_csv('tabular.csv')
    data = scrap_text(text, pattern)
    new_df = pd.DataFrame(data)
    new_df['date'] = date
    
    return (
        pd
        .concat([old_df, new_df])
        .set_index('date')
        .to_csv('tabular.csv')
    )
