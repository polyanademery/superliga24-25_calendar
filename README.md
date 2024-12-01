# superliga24-25_calendar

## Superliga Feminina Calendar Project

This project generates an ICS file containing all the matches of the Superliga Feminina 2024/2025 season. The generated file can be easily imported into your calendar application to keep track of all the games, ensuring you never miss a match!

### Features
Extracts game data from a predefined list.
Adjusts game times for different time zones.
Creates a single ICS file for all matches.
Easy to modify for personal use.

### Prerequisites
Make sure you have the following installed:

Python 3.x
ics library
You can install the required library using pip:

pip install ics
How to Use
Clone or download this repository to your local machine.

### Run
Update the games list in the script with the match details for the Superliga Feminina season. Here’s the structure you should follow for each game:

{
    "date": "YYYY-MM-DD",
    "time": "HH:MM AM/PM",
    "teams": "Team A vs Team B",
    "city": "City Name",
    "venue": "Venue Name",
    "tv": "TV Channel"
}
Run the script using the command:

python your_script_name.py

Import the generated ICS file into your calendar application.

### Example
An example of the game data you might include in the script is as follows:

games = [
    {"date": "2024-12-13", "time": "9:30 PM", "teams": "SESC RJ FLAMENGO vs ABEL MODA VOLEI", "city": "RIO DE JANEIRO - RJ", "venue": "TIJUCA TÊNIS CLUBE", "tv": "SPORTV"},
    {"date": "2024-12-03", "time": "9:30 PM", "teams": "DENTIL PRAIA CLUBE vs OSASCO SÃO CRISTÓVÃO SAÚDE", "city": "UBERLÂNDIA - MG", "venue": "ARENA DENTIL", "tv": "SPORTV"},
    # Add more games as necessary...
]
Adjusting Time Zones
The script currently adjusts the game times to account for your local time zone. Ensure you modify the adjust_time function if you need to change how times are calculated.

### Contribution
Feel free to contribute to this project by submitting issues or pull requests!

### License
This project is licensed under the MIT [License](https://github.com/polyanademery/superliga24-25_calendar/blob/main/LICENSE) - see the LICENSE file for details.
