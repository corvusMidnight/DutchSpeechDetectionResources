import Levenshtein
import pandas as pd
import re
import matplotlib.pyplot as plt
from Levenshtein import distance

def word_recognition(df: pd.DataFrame, col1: str, col2: str) -> tuple:
    """Calculates word recognition rate (WRR) and error rate (ER) between two columns of strings in a dataframe.

    Args:
    df (pandas.DataFrame): The dataframe containing the two columns of strings to compare.
    col1 (str): The name of the first column.
    col2 (str): The name of the second column.

    Returns:
    wrr_list (list): A list of WRR values, one for each row in the dataframe.
    er_list (list): A list of ER values, one for each row in the dataframe.
    """
    wrr_list = []
    er_list = []
    for i in range(len(df)):
        string1 = df.loc[i, col1]
        string2 = df.loc[i, col2]
        n = len(string1)
        m = len(string2)
        wrr = (n-distance(string1, string2))/n
        wrr_list.append(wrr)
        er = distance(string1, string2)/n
        er_list.append(er)
    return wrr_list, er_list

def plot_wrr_er(df: pd.DataFrame, col1: str, col2: str):
    """Plots the word recognition rate (WRR) and error rate (ER) calculated by the word_recognition() function.

    Args:
    df (pandas.DataFrame): The dataframe containing the two columns of strings to compare.
    col1 (str): The name of the first column.
    col2 (str): The name of the second column.
    """
    wrr, er = word_recognition(df, col1, col2)
    plt.figure(figsize=(10, 5))
    plt.plot(wrr, label='WRR')
    plt.plot(er, label='ER')
    plt.xlabel('Observations')
    plt.ylabel('Rate')
    plt.legend(loc='upper left')
    plt.show()



def levenshtein_distance(df, col1, col2):
    '''
    A simple function to calculate the distance between pair of strings in the.

    Args:
        df: A pandans datafrae
        col1: A string, the name of the column containing the references sentences
        col2: A string, the name of the column containing the output sentences
    Returns:
        df: The original dataframe with an additional column containing the Levenshtein distance between each pair of strings in the same row
    '''
    results = []
    for i in range(len(df)):
        string1 = df.loc[i, col1]
        string2 = df.loc[i, col2]
        results.append(distance(string1, string2))
    df[f'distance {col2}'] = results
    return df

def lower_and_remove_punctuation(strings: str)-> str:
    '''
    A simple function to lower and remove punctuation from a string.

    Args:
        strings: A string
    
    Returns:
        strings: The input string without punctuation, trailing spaces, and lowered
    '''
    strings = strings.lower()
    strings = strings.strip()
    pattern = re.compile(r'[^\w\s]')
    return ' '.join([pattern.sub('', string).strip() for string in strings.split()])


def highlight_differences(reference: str, output: str) -> str:
    '''
    A simple function to compare an output sentence to a reference sentence using Levenshtein distance.
    Substituions are put in between parentheses (i.e., () ), insetions are put in between ankle brackets (i.e., <> ),
    deletion are highlighted through one underscore.

    Args:
        reference: A string
        output: A string
    
    Returns:
        output: The input (output) string without punctuation
    '''
    edit_ops = Levenshtein.editops(reference, output)
    ref_list = list(reference)
    for op, i, j in edit_ops:
        if op == 'replace':
            ref_list[i] = f'({output[j]})'
        elif op == 'delete':
            ref_list[i] = '_'
        elif op == 'insert':
            ref_list.insert(i, f'<{output[j]}>')
    return ''.join(ref_list)

def apply_highlight_to_dataframe(df: pd.DataFrame, df_reference_column: str, df_output_column: str) -> pd.DataFrame:
    '''
    A simple function to apply the highlight_differences function to a dataframe.

    Args:
        df: A pandans datafrae
        df_reference_column: A string, the name of the column containing the references sentences
        df_output_column: A string, the name of the column containing the output sentences
    Returns:
        df: The input df with an additional column containing a additional x__Levenshtein column (identical to the df_output_column)
        but with the differences highlighted
    '''
    df[f'{df_output_column}_Levenshtein'] = df.apply(lambda x: highlight_differences(x[df_reference_column], x[df_output_column]), axis=1)
    return df
