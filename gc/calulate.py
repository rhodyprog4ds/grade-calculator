import pandas as pd

experience_valid = ['absent','present','active']
learning_outcomes = ['process','communication','data','exploratory','modeling']
learning_valid = ['unattempted','partial','complete','innovative']


def validate_eval(eval_df):
    '''
    Validate the evaluation dataframe to ensure all values are within expected ranges.
    
    Parameters
    ----------
    eval_df : pd.DataFrame
        DataFrame containing evaluation scores with columns activity, process, communication, data, exploratory, modeling
    
    Raises
    ------
    ValueError
        If any value in the dataframe is outside the expected ranges.
    '''
    for col in learning_outcomes:
        if col not in eval_df.columns:
            raise ValueError(f"Missing expected column: {col}")

    for outcome in learning_outcomes:
        if not eval_df[outcome].isin(learning_valid).all():
            raise ValueError(f"Invalid values found in '{outcome}' column. Expected values: {learning_valid}")
    
    return True


def token_status(token_df):
    '''
    Calculate the current token status from the token dataframe.
    
    Parameters
    ----------
    token_df : pd.DataFrame
        DataFrame containing token transactions with columns date, transaction, note
    
    Returns
    -------
    int
        Current number of tokens
    '''
    return token_df['transaction'].sum()

def calculate_total(eval_df):
    '''
    Calculate the total score from the evaluation dataframe.
    
    Parameters
     Parameters
    ----------
    eval_df : pd.DataFrame
        DataFrame containing evaluation scores with columns activity, process, communication, data, exploratory, modeling
    participation_df : pd.DataFrame
        DataFrame containing participation scores with columns date and evaluation
    '''


    counts_df = eval_df[learning_outcomes].value_counts().reset_index()

    return counts_df

def calculate_grade(eval_df, participation_df):
    '''
    Calculate the final grade based on evaluation and participation dataframes.
    
    Parameters
    ----------
    eval_df : pd.DataFrame
        DataFrame containing evaluation scores with columns activity, process, communication, data, exploratory, modeling
    participation_df : pd.DataFrame
        DataFrame containing participation scores with columns date and evaluation
    '''
    return 'TBA'