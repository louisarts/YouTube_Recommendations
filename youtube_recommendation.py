import pandas as pd
from user_profile import import_user_profile

# Function to generate YouTube recommendations and user profile based on client_text
def output_yt_df(client_text):
    # Import user profile using the import_user_profile function
    user_profile = import_user_profile(client_text)

    # Define weight loss category based on the user's weight loss
    weight_loss = int(user_profile['weight_loss'])
    category = 'A' if weight_loss >= 20 else 'B' if 10 < weight_loss < 20 else 'C'

    # Read the dataset
    df = pd.read_csv('data/output.csv')

    # Filter the dataset based on the user's gender
    df = df[df['Gender'].eq(user_profile['gender']) & df['Gender'].notna()]

    # Filter the dataset based on the user's weight loss category
    col_name = 'Weight lossed'
    if col_name in df.columns:
        if category == 'A':
            df = df[df[col_name].ge(20) & df[col_name].notna()]
        elif category == 'B':
            df = df[df[col_name].between(10, 20, inclusive=True) & df[col_name].notna()]
        elif category == 'C':
            df = df[df[col_name].le(10) & df[col_name].notna()]

    # Return the filtered dataframe and the user profile
    return df, user_profile

