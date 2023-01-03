import csv
from collections import defaultdict
from typing import Any

with open('eurovision.csv', 'r', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)
    next(csv_reader, None)
    host_countries = list(csv_reader)

qns_name = str(input("\nWelcome to Eurovision!\nBefore we proceed, please enter your name? "))

flag = True

while flag:
    try:
        qns_option = ("\nHi " + qns_name.title() + ", kindly choose from the menu options below: \n")
        print(qns_option)
        print("Enter 1 to view - Host Countries based on year(s)")
        print("Enter 2 to view - Overall Top 10 total points")
        print("Enter 3 to view - Winner, Runner up, and 2nd Runner Up of the year")
        print("Enter 4 to view - Winning Songs based on year(s)")
        print("Enter 5 to view - Year(s) a country won the competition(s)")
        print("Enter 6 to view - Competition details based on City name")
        print("Enter 7 to view - List of countries that have participated over a period of years")
        print("Enter 8 to view - Countries that have won the most and the least competitions")
        print("Enter 9 to Quit\n")

        choice = int(input("Enter your option: "))
    except ValueError:
        # Input is not a valid integer, so we print an error message and ask the user to try again
        print("Invalid input. Please enter number from 1 to 9 only.")
        continue

    if choice == 1:
        print("\nHost Countries based on year(s)\n")
        while True:
            try:
                # Get user input for start year
                start_year = int(input("Enter the start year (1956 to 2022): "))

                # Check if the start year is within the valid range
                if 1956 <= start_year <= 2022:
                    break
                else:
                    print("Invalid start year. Please enter a year between 1956 and 2022.")
            except ValueError:
                # If input is not a valid integer, we print an error message and ask the user to try again
                print("Invalid start year. Please enter a year between 1956 and 2022.")

        while True:
            try:
                # Get user input for end year
                end_year = int(input("Enter the end year (1956 to 2022): "))

                # Check if the end year is within the valid range
                if 1956 <= end_year <= 2022:
                    break
                else:
                    print("Invalid end year. Please enter a year between 1956 and 2022.")
            except ValueError:
                # Input is not a valid integer, so we print an error message and ask the user to try again
                print("Invalid end year. Please enter a year between 1956 and 2022.")

        # After above is complete, to continue
        # Process the host countries based on the start and end years provided by the user
        # Ensure output has no duplicates
        unique_country = set()
        for country in host_countries:
            years_won = int(country['year'])
            if start_year <= years_won <= end_year or start_year >= years_won >= end_year:
                unique_country.add((country['host_country'], years_won))

        unique_country = list(unique_country)
        # To sort the countries, we use lambda
        unique_country.sort(key=lambda x: x[1])

        # To iterate over the elements in the unique_country list
        # Enumerate is to keep track of the index of each element as you iterate over the list
        for i, pairs in enumerate(unique_country):
            print(f"{i + 1}. {pairs[1]} - hosted in {pairs[0]}")

    elif choice == 2:
        print("\nOverall Top 10 total points\n")


        def find_top_ten_winners():
            points = []
            winner = []
            cities = []

            # Open the CSV file and read the data into a list of dictionaries
            with open('eurovision.csv', 'r', encoding="utf8") as g:
                reader = csv.DictReader(g)
                rows = list(reader)

            # Get the points and corresponding winners and cities for the winners
            for row in rows:
                if row['winner'] == 'TRUE' and row['total_points'] != 'NA':
                    points.append(int(row['total_points']))
                    winner.append(row['artist'])
                    cities.append(row['host_city'])

            # Sort the points, winners, and cities in descending order
            points, winner, cities = zip(*sorted(zip(points, winner, cities), reverse=True))

            # Slice the top 10 winners, cities, and points
            top_ten_point = points[:10]
            top_ten_winner = winner[:10]
            top_ten_city = cities[:10]

            return top_ten_winner, top_ten_city, top_ten_point


        # Call the function and print the results
        top_ten_winners, top_ten_cities, top_ten_points = find_top_ten_winners()
        for i in range(len(top_ten_winners)):
            print(f"{i + 1}. {top_ten_winners[i]} ({top_ten_cities[i]}) - {top_ten_points[i]} points")


    elif choice == 3:
        print("\nWinner, Runner up, and 2nd Runner Up of the year\n")
        while True:
            try:
                # Get user input for start year
                view_winners = int(input("Enter the year (1956 to 2022): "))
                # Check if the start year is within the valid range
                if 1956 <= view_winners <= 2022:
                    break
                else:
                    print("Invalid start year. Please enter a year between 1956 and 2022.")
            except ValueError:

                # If input is not a valid integer, we print an error message and ask the user to try again
                print("Invalid start year. Please enter a year between 1956 and 2022.")
        # Open the CSV file and read the data into a list of dictionaries
        with open('eurovision.csv', 'r', encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

            the_winner = []
            runners_up = []
            second_runners_up = []

            # Iterate through a list of dictionaries called 'rows' and storing any values which contains 1st, 2nd, 3rd in 'rank_ordinal' into a list called the_winner, runners_up and second_runners_up
            for row in rows:
                year_hosted = int(row['year'])
                if view_winners == year_hosted and (row["section"] == "grand-final" or row["section"] == "final"):
                    if row['rank_ordinal'] == "1st":
                        the_winner.append(row)
                    elif row['rank_ordinal'] == "2nd":
                        runners_up.append(row)
                    elif row['rank_ordinal'] == "3rd":
                        second_runners_up.append(row)

            # Print the Winner, Runners Up, 2nd Runner Up
            print("\nWinner:")
            # To iterate over the elements in the the_winner list
            # Enumerate is to keep track of the index of each element as you iterate over the list
            for i, row in enumerate(the_winner):
                print(f"1. {row['artist']} ({row['artist_country']}), {row['song']} - {row['total_points']} Total Points")
            if len(the_winner) == 0:
                print('No winner(s) for this year')

            # To iterate over the elements in the runners_up list
            # Enumerate is to keep track of the index of each element as you iterate over the list

            print("\nRunner Up:")
            for i, row in enumerate(runners_up):
                print(f"2. {row['artist']} ({row['artist_country']}), {row['song']} - {row['total_points']} Total Points")
            if len(runners_up) == 0:
                print('No 1st runners-up for this year')

            # To iterate over the elements in the second_runners_up list
            # Enumerate is to keep track of the index of each element as you iterate over the list
            print("\n2nd Runner Up:")
            for i, row in enumerate(second_runners_up):
                print(f"3. {row['artist']} ({row['artist_country']}), {row['song']} - {row['total_points']} Total Points")
            if len(second_runners_up) == 0:
                print('No 2nd runners-up for this year')

    elif choice == 4:
        print("\nWinning Songs based on year(s)\n")
        while True:
            try:
                # Get user input for start year
                winning_song_start = int(input("Enter the start year (1956 to 2022): "))

                # Check if the start year is within the valid range
                if 1956 <= winning_song_start <= 2022:
                    break
                else:
                    print("Invalid start year. Please enter a year between 1956 and 2022.")
            except ValueError:
                # If input is not a valid integer, we print an error message and ask the user to try again
                print("Invalid input. Please enter a year between 1956 and 2022.")

        while True:
            try:
                # Get user input for end year
                winning_song_end = int(input("Enter the end year (1956 to 2022): "))
                # Check if the end year is within the valid range
                if 1956 <= winning_song_end <= 2022:
                    break
                else:
                    print("Invalid end year. Please enter a year between 1956 and 2022.")
            except ValueError:
                # Input is not a valid integer, so we print an error message and ask the user to try again
                print("Invalid input. Please enter a year between 1956 and 2022.")

        if winning_song_start > winning_song_end:
            winning_song_start, winning_song_end = winning_song_end, winning_song_start
            # Open the CSV file and read the data into a list of dictionaries
        with open('eurovision.csv', 'r', encoding="utf8") as f:
            reader = csv.DictReader(f)
            song = list(reader)

            # Filter the list of songs to only include those that won during the specified range of years and have the 'winner' field set to 'TRUE'
            winning_songs = [row for row in song if
                             winning_song_start <= int(row['year']) <= winning_song_end and row[
                                 'winner'] == 'TRUE' and (row['section'] == "grand-final" or row['section'] == 'final')]
            winning_songs = sorted(winning_songs, key=lambda d: d['year'])

            # Print the artist, song title, and year for each winning song
            for i, row in enumerate(winning_songs):
                print(f"{i + 1}. {row['song']} ({row['artist_country']}) by {row['artist']} ({row['year']})")

    elif choice == 5:

        print("\nYear(s) a country won the competition\n")
        # Open the CSV file and read the data into a list of dictionaries
        with open('eurovision.csv', 'r', encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Create a list of valid choices
        valid_country_names = [row['artist_country'].lower() for row in rows]
        # Prompt the user to enter their choice and read it as a string
        country_name = input("Enter the country name: ")

        # Convert the user input to lowercase
        country_name = country_name.lower()

        # Check if the user input is in the list of valid country names found in the csv
        while country_name not in valid_country_names:
            print("Invalid country name. Please try again.")
            country_name = input("Enter the country name: ")
            country_name = country_name.lower()

        # Find all rows where the country name and winner status match the user input
        # Convert the artist_country field to lowercase before comparing it to the user input

        country_winner = [row for row in rows if
                          country_name == row['artist_country'].lower() and row['winner'] == 'TRUE']

        # Extract the year from each winning song and store it in a list
        years = [row['year'] for row in country_winner]
        years = sorted(years)

        # Print the list of years, separated by commas
        if years:
            print(f"The country {country_name.title()} won the Eurovision Song Contest in the following years: {', '.join(years)}")
        else:
            print(f"The country {country_name.title()} has never won the Eurovision Song Contest.")

    elif choice == 6:
        print("\nCompetition details based on City name\n")
        city_name = input("Enter the city name: ")

        # Open the CSV file and read the data into a list of dictionaries
        with open('eurovision.csv', 'r', encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

            # Create a list of valid choices
            valid_city_names = [row['host_city'].lower() for row in rows]

            # Check if the user input is in the list of valid city name found in the csv
            while city_name.lower() not in valid_city_names:
                print("Invalid city name. Please try again")
                city_name = input("Enter the city name: ")
                city_name = city_name.lower()

            # Find all rows where the host city name matches the user input
            # Convert the host_city field to lowercase before comparing it to the user input
            city_details = [row for row in rows if city_name.lower() == row['host_city'].lower()]

            # Extract the year from each winning song and store it in a list
            years = [row['year'] for row in city_details]
            winners = []

            # Loop through each row in the city_details list
            for row in city_details:
                # If the row represents a winning song, add the artist and total points to the winners list
                if row['winner'] == 'TRUE':
                    winners.append(
                        f"{row['artist']} from {row['artist_country']} with {row['total_points']} points in {row['year']}")

            # Remove duplicates from the winners list
            winners = list(set(winners))
            years = list(set(years))

            # Sort the years list in ascending order
            years = sorted(years)

            # Print the list of years and winners, separated by commas
            print(f"City Name: {city_name.title()}")
            print(f"Years participated in the Eurovision Song Contest: {', '.join(years)}")
            print(f"Winners of the Eurovision Song Contest in {city_name.title()}: {', '.join(winners)}")


    elif choice == 7:
        print("\nList of countries that have participated over a period of years\n")
        while True:
            try:
                # Get user input for start year
                winning_song_start = int(input("Enter the start year (1956 to 2022): "))

                # Check if the start year is within the valid range
                if 1956 <= winning_song_start <= 2022:
                    break
                else:
                    print("Invalid start year. Please enter a year between 1956 and 2022.")
            except ValueError:
                # If input is not a valid integer, we print an error message and ask the user to try again
                print("Invalid start year. Please enter a year between 1956 and 2022.")

        while True:
            try:
                # Get user input for end year
                winning_song_end = int(input("Enter the end year (1956 to 2022): "))

                # Check if the end year is within the valid range
                if 1956 <= winning_song_end <= 2022:
                    break
                else:
                    print("Invalid end year. Please enter a year between 1956 and 2022.")
            except ValueError:
                # Input is not a valid integer, so we print an error message and ask the user to try again
                print("Invalid end year. Please enter a year between 1956 and 2022.")

        # Open the CSV file and read the data into a list of dictionaries
        with open('eurovision.csv', 'r', encoding="utf8") as f:
            reader = csv.DictReader(f)
            countries = list(reader)

            # Filter the list of songs to only include those that won during the specified range of years and have the 'winner' field set to 'TRUE'
            winning_songs = [row for row in countries if
                             (winning_song_start <= int(row['year']) <= winning_song_end or winning_song_start >= int(row['year']) >= winning_song_end) and row['winner'] == "TRUE" and row[
                                 'section'] in ("final", "grand-final")]
            # A dictionary that is used to store the unique countries and their respective songs.
            unique_country = {}
            # A dictionary to store the unique song names and their respective years
            song_years = {}

            # Iterate over the list of winning songs
            for song in winning_songs:
                # Check if the song name is not in the dictionary
                if song['song'] not in song_years:
                    # If the song name is not in the dictionary, add it to the dictionary
                    song_years[song['song']] = song['year']

                    # Check if the country is already in the dictionary
                    if song['artist_country'] in unique_country:
                        # If the country is already in the dictionary, append the song to the list of songs for that country
                        unique_country[song['artist_country']]['songs'].append(song['song'])
                    else:
                        # If the country is not in the dictionary, add it as a key and set the value to a list containing the song
                        unique_country[song['artist_country']] = {'songs': [song['song']]}

            # Sort the unique_country dictionary by the country names in alphabetical order
            unique_country_sorted = dict(sorted(unique_country.items(), key=lambda item: item[0].lower()))

            # Print the countries and their respective songs
            # Counter variable is to keep track of the current item number
            counter = 1
            for country, songs in unique_country_sorted.items():
                song_list = [(song, song_years[song]) for song in sorted(songs['songs'], key=lambda song2: song2.lower())]
                print(f"{counter}. {country} - {', '.join([f'{song} ({year})' for song, year in song_list])}")
                # Increment the counter after each iteration
                counter += 1

    elif choice == 8:
        print("\nCountries that have won the most and the least competitions\n")
        # Open the CSV file and read the data into a list of dictionaries
        with open('eurovision.csv', 'r', encoding="utf8") as f:
            reader = csv.DictReader(f)
            countries = list(reader)
            winning_songs: list[Any] = []
            never_win = []
            # Filter the list of countries to include only those that has rank = 1, winner = TRUE, section = Final and Grand-Final
            winning_songs = [row for row in countries if row['rank'] == "1" and row['winner'] == "TRUE" and (row['section'] == "final" or row['section'] == "grand-final")]

            if winning_songs:
                # Initialize a dictionary to keep track of the number of times each country has won
                winning_count = defaultdict(int)

                # Loop through the list of winning songs and increment the value in the dictionary for each song that a country wins
                for song in winning_songs:
                    winning_count[song['artist_country']] += 1
                # Find the maximum number of wins
                max_wins = max(winning_count.values())

                # Find the minimum number of wins
                min_wins = min(winning_count.values())

                # Find the countries that have won the most competitions
                most_wins = [country for country, wins in winning_count.items() if wins == max_wins]
                # Sorting the countries alphabetically
                most_wins.sort()
                # Find the countries that have won the least competitions
                least_wins = [country for country, wins in winning_count.items() if wins == min_wins]
                # Sorting the countries alphabetically
                least_wins.sort()

                # Create list of all the countries
                all_countries = set([row['artist_country'] for row in countries])
                # To return a set containing the countries that are in all_countries but not in set(winning_count) which are the countries which has not won
                never_win = list(all_countries - set(winning_count))
                # Sorting the countries alphabetically
                never_win.sort()

                print(f"The country that has won the most competitions is {', '.join(most_wins)} with {max_wins} win(s).")
                print(f"The countries that have won the least competitions are {', '.join(least_wins)} with {min_wins} win(s).")
                print(f"The countries that have never won are {', '.join(never_win)}.")

    elif int(choice == 9):
        flag = False
        print(qns_name.title() + ', you will be exiting. Thank you, see you again!')
        break
    else:
        print("Invalid choice. Please try again.")
    user_input = input("\nEnter Y to return to menu, N to Exit: ")
    while user_input.lower() not in ['y', 'n']:
        user_input = input("\nEnter Y to return to menu, N to Exit:")

    if user_input.lower() == 'y':
        flag = True

    elif user_input.lower() == 'n':
        flag = False
        print(qns_name.title() + ', you will be exiting. Thank you, see you again!')
        break
