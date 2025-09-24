import click
import pandas as pd
from .calculate import calculate_grade, token_status
import os


@click.group()
def rhodyds():
    pass



report_template = '''# Grade Report

This is your current standing as of {today_date}.

{grade_table}

This amounts to a current grade of {current_grade}, remember this your current grade, not a 
prediction of your final grade. Your final grade will be at least this, but will increase as you 
contine to participate and complete assignments.


You currently have {current_tokens} tokens.



'''

@rhodyds.command()
@click.option('--eval-file', type=click.Path(exists=True), 
              default=os.path.join('.grades','evals.csv'),
                help='Path to the evaluation CSV file')
@click.option('--participation-file', type=click.Path(exists=True), 
              default=os.path.join('.grades','participation.csv'),
                        help='Path to the participation CSV file')
@click.option('--tokens-file', type=click.Path(exists=True), 
              default=os.path.join('.grades','tokens.csv'),
                        help='Path to the tokens CSV file')
@click.option('--output-file', type=click.Path(), required=True, help='Path to save the final grades CSV file')
def update_report(eval_file, participation_file, tokens_file, output_file):
    '''
    Compute final grades from evaluation and participation CSV files and save to output CSV file.
    '''
    eval_df = pd.read_csv(eval_file)
    participation_df = pd.read_csv(participation_file)
    tokens_df = pd.read_csv(tokens_file)
    
    current_grade = calculate_grade(eval_df, participation_df)
    
    filled_report = report_template.format(
        today_date=pd.Timestamp.now().date(),
        grade_table=eval_df.to_markdown(index=False),
        current_grade=current_grade,
        current_tokens=token_status(tokens_df)
    )

    with open(output_file, 'w') as f:
        f.write(filled_report)

    click.echo(f'Final grades saved to {output_file}')