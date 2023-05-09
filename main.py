# Import the output_yt_df function from the youtube_recommendation module
from youtube_recommendation import output_yt_df

# Function to get video URLs from the dataframe output
def get_video_urls(df_output):
    # Create a list of YouTube video URLs using the video IDs in the dataframe
    return [f"https://www.youtube.com/watch?v={video_id}" for video_id in df_output['Video_ID'][:5]]

# Function to print video URLs
def print_urls(video_urls):
    # Loop through each video URL and print it followed by a newline
    for url in video_urls:
        print(url, "\n")

# Main function
if __name__ == "__main__":
    # Prompt the user to answer a series of questions
    s = input("\n\n Kun je even de volgende vragen beantwoorden: \n vrouw of man of X? \n Leeftijd? \n Gewicht? \n Gedroomd gewicht? \n Lichaamslengte? \n Neem je medicatie, zo ja welke? \n Heb je dagelijks stoelgang? \n Welke diëten heb je al gedaan? \n\n")

    # Call the output_yt_df function with the user's input and get the dataframe and user_profile as output
    df_output, user_profile = output_yt_df(s)

    # Get the video URLs using the get_video_urls function
    video_urls = get_video_urls(df_output)

    # Print a thank you message and the recommended video URLs
    print('\n\n\nBedankt voor uw info! Gebaseerd op uw profiel worden de volgede vijf videos aanbevolen. Meer specifiek zijn dit "testimonials" van vorige klanten wiens target het dichtst bij u aansluit. Geniet er van!\n')
    print_urls(video_urls)
    
    # Print the user's profile
    print(user_profile)
