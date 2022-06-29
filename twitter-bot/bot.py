from inspect import Attribute
import tweepy
from time import sleep

# KEYS API Developer Twitter
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Create a tweet
api.update_status("Twitter Bot Python")

# Open text file verne.txt (or your chosen file) for reading
my_file = open('file.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Create a for loop to iterate over file_lines
for line in file_lines:
  try:
      print(line)
      if line != '\n':                  # Add if statement to ensure that blank lines are skipped
          api.update_status(line)
      else:                             # Add an else statement with pass to conclude the conditional statement
          pass
  except AttributeError as e:
      print(e.reason)
  sleep(120)                           # Add sleep method to space tweets by 5 seconds each
  
# Tweet a line every 15 minutes
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(2)
             else:
                pass
        except AttributeError as e:
            print(e.reason)
            sleep(2)
tweet()