#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = ["Be yourself; everyone else is already taken. – Oscar Wilde",
          "In the end, we only regret the chances we didn’t take. – Lewis Carroll",
          "Life is what happens when you're busy making other plans. – John Lennon",
          "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
          "Happiness is not by chance, but by choice. – Jim Rohn",
          "Do what you can, with what you have, where you are. – Theodore Roosevelt",
          "The only way to do great work is to love what you do. – Steve Jobs",
          "Believe you can and you’re halfway there. – Theodore Roosevelt",
          "You miss 100 percent of the shots you don’t take. – Wayne Gretzky",
          "Change the world by being yourself. – Amy Poehler"
          ]

def get_quote_of_the_day(quotes):
    todays_quote = None
    today = date.today()
    # A same quote will be generated for each weekday
    random.seed(today.weekday())
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /home/codespace/.python/current/bin/python3 /workspaces/03-data-structures-FaezehMirlohi/01_daily_quote.py >> /workspaces/03-data-structures-FaezehMirlohi/daily_quote.txt 2>&1
