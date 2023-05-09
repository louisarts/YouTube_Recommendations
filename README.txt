# YouTube Recommendation Project

This project generates personalized YouTube video recommendations based on a user's profile, including gender, age, weight, target weight, and other health-related information.

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in the project directory.
3. Run the `main.py` script by executing `python main.py` in the project directory.
4. Answer the prompted questions about your profile.
5. The script will display the top 5 recommended YouTube video URLs based on your profile.

## Project Structure

- `main.py`: The main script that prompts the user for input and generates YouTube video recommendations.
- `user_profile.py`: A script containing functions to import and process a user's profile using GPT-3.
- `youtube_recommendation.py`: A script that generates YouTube recommendations based on the user's profile.

## Requirements

- Python 3.6+
- pandas
- scikit-learn
- openai
