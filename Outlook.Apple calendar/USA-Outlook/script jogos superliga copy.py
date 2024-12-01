from ics import Calendar, Event
from datetime import datetime, timedelta

# Function to adjust game times
def adjust_time(date_str, time_str):
    # Combine date and time, parsing in 12-hour AM/PM format
    dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %I:%M %p")
    
    # Subtract 3 hours for the adjusted start time
    start_time = dt - timedelta(hours=3)  # Adjusting time
    end_time = start_time + timedelta(hours=2)  # 2 hours duration
    
    # Format for display
    start_time_formatted = start_time.strftime("%I:%M %p")
    end_time_formatted = end_time.strftime("%I:%M %p")
    
    return start_time, end_time, start_time_formatted, end_time_formatted

# Data extracted from your document (including all games)
games = [
    {"date": "2024-12-13", "time": "9:30 PM", "teams": "SESC RJ FLAMENGO vs ABEL MODA VOLEI", "city": "RIO DE JANEIRO - RJ", "venue": "TIJUCA TÊNIS CLUBE", "tv": "SPORTV"},
    {"date": "2024-12-03", "time": "9:30 PM", "teams": "DENTIL PRAIA CLUBE vs OSASCO SÃO CRISTÓVÃO SAÚDE", "city": "UBERLÂNDIA - MG", "venue": "ARENA DENTIL", "tv": "SPORTV"},
    {"date": "2024-12-03", "time": "6:30 PM", "teams": "GERDAU MINAS vs SESI VÔLEI BAURU", "city": "BELO HORIZONTE - MG", "venue": "ARENA UNIBH", "tv": "SPORTV"},
    {"date": "2024-12-04", "time": "7:00 PM", "teams": "BATAVO MACKENZIE vs FLUMINENSE FOOTBALL CLUB", "city": "BELO HORIZONTE - MG", "venue": "MACKENZIE ESPORTE CLUBE", "tv": "VÔLEI BRASIL"},
    {"date": "2024-12-04", "time": "9:30 PM", "teams": "BRASILIA VOLEI vs E.C. PINHEIROS", "city": "BRASILIA - DF", "venue": "SESI TAGUATINGA NORTE", "tv": "SPORTV"},
    {"date": "2024-12-03", "time": "7:00 PM", "teams": "UNILIFE MARINGÁ vs BARUERI VOLLEYBALL CLUB", "city": "MARINGÁ - PR", "venue": "GINÁSIO CHICO NETO", "tv": "VÔLEI BRASIL"},
    {"date": "2024-12-06", "time": "6:30 PM", "teams": "BARUERI VOLLEYBALL CLUB vs ABEL MODA VOLEI", "city": "BARUERI - SP", "venue": "GINÁSIO JOSÉ CORREA", "tv": "SPORTV"},
    {"date": "2024-12-10", "time": "6:00 PM", "teams": "E.C. PINHEIROS vs UNILIFE MARINGÁ", "city": "SÃO PAULO - SP", "venue": "GINÁSIO POLIESPORTIVO HENRIQUE VILLABOIM", "tv": "SPORTV"},
    {"date": "2024-12-09", "time": "6:30 PM", "teams": "FLUMINENSE FOOTBALL CLUB vs BRASILIA VOLEI", "city": "RIO DE JANEIRO - RJ", "venue": "CLUBE SOCIEDADE HEBRAICA", "tv": "SPORTV"},
    {"date": "2024-12-09", "time": "9:30 PM", "teams": "SESI VÔLEI BAURU vs BATAVO MACKENZIE", "city": "BAURU - SP", "venue": "ARENA PAULO SKAF", "tv": "SPORTV"},
    {"date": "2024-12-06", "time": "9:30 PM", "teams": "OSASCO SÃO CRISTÓVÃO SAÚDE vs GERDAU MINAS", "city": "OSASCO - SP", "venue": "GINÁSIO JOSÉ LIBERATI", "tv": "SPORTV"},
    {"date": "2024-12-19", "time": "6:30 PM", "teams": "SESC RJ FLAMENGO vs DENTIL PRAIA CLUBE", "city": "RIO DE JANEIRO - RJ", "venue": "MARACANÃZINHO", "tv": "SPORTV"},
    {"date": "2024-12-13", "time": "6:30 PM", "teams": "E.C. PINHEIROS vs BARUERI VOLLEYBALL CLUB", "city": "SÃO PAULO - SP", "venue": "GINÁSIO POLIESPORTIVO HENRIQUE VILLABOIM", "tv": "SPORTV"},
    {"date": "2024-12-13", "time": "9:30 PM", "teams": "UNILIFE MARINGÁ vs FLUMINENSE FOOTBALL CLUB", "city": "MARINGÁ - PR", "venue": "GINÁSIO CHICO NETO", "tv": "SPORTV"},
    {"date": "2024-12-16", "time": "9:30 PM", "teams": "SESI VÔLEI BAURU vs BRASILIA VOLEI", "city": "BAURU - SP", "venue": "ARENA PAULO SKAF", "tv": "SPORTV"},
    {"date": "2024-12-16", "time": "6:30 PM", "teams": "BATAVO MACKENZIE vs OSASCO SÃO CRISTÓVÃO SAÚDE", "city": "BELO HORIZONTE - MG", "venue": "MACKENZIE ESPORTE CLUBE", "tv": "SPORTV"},
    {"date": "2024-12-12", "time": "9:30 PM", "teams": "SESC RJ FLAMENGO vs GERDAU MINAS", "city": "RIO DE JANEIRO - RJ", "venue": "TIJUCA TÊNIS CLUBE", "tv": "SPORTV"},
    {"date": "2024-12-22", "time": "6:30 PM", "teams": "UNILIFE MARINGÁ vs SESI VÔLEI BAURU", "city": "MARINGÁ - PR", "venue": "GINÁSIO CHICO NETO", "tv": "SPORTV"},
    {"date": "2024-12-20", "time": "9:30 PM", "teams": "BARUERI VOLLEYBALL CLUB vs FLUMINENSE FOOTBALL CLUB", "city": "BARUERI - SP", "venue": "GINÁSIO JOSÉ CORREA", "tv": "SPORTV"},
    {"date": "2025-01-07", "time": "7:30 PM", "teams": "ABEL MODA VOLEI vs GERDAU MINAS", "city": "BRUSQUE - SC", "venue": "ARENA BRUSQUE", "tv": "VOLEI BRASIL"},
    {"date": "2025-01-07", "time": "7:00 PM", "teams": "BATAVO MACKENZIE vs DENTIL PRAIA CLUBE", "city": "BELO HORIZONTE - MG", "venue": "MACKENZIE ESPORTE CLUBE", "tv": "VOLEI BRASIL"},
    {"date": "2025-01-07", "time": "6:30 PM", "teams": "SESC RJ FLAMENGO vs BRASILIA VOLEI", "city": "RIO DE JANEIRO - RJ", "venue": "MARACANAZINHO", "tv": "SPORTV"},
    {"date": "2025-01-07", "time": "8:00 PM", "teams": "OSASCO SÃO CRISTÓVÃO SAÚDE vs UNILIFE MARINGÁ", "city": "OSASCO - SP", "venue": "GINÁSIO JOSÉ LIBERATI", "tv": "VOLEI BRASIL"},
    {"date": "2025-01-07", "time": "9:30 PM", "teams": "SESI VÔLEI BAURU vs BARUERI VOLLEYBALL CLUB", "city": "BAURU - SP", "venue": "ARENA PAULO SKAF", "tv": "SPORTV"},
    {"date": "2025-01-08", "time": "6:30 PM", "teams": "E.C. PINHEIROS vs FLUMINENSE FOOTBALL CLUB", "city": "SÃO PAULO - SP", "venue": "GINÁSIO POLIESPORTIVO HENRIQUE VILLABOIM", "tv": "SPORTV"},
    {"date": "2025-01-13", "time": "6:30 PM", "teams": "GERDAU MINAS vs BATAVO MACKENZIE", "city": "BELO HORIZONTE - MG", "venue": "ARENA UNIBH", "tv": "SPORTV"},
    {"date": "2025-01-13", "time": "9:30 PM", "teams": "E.C. PINHEIROS vs SESI VÔLEI BAURU", "city": "SÃO PAULO - SP", "venue": "GINÁSIO POLIESPORTIVO HENRIQUE VILLABOIM", "tv": "SPORTV"},
    {"date": "2025-01-11", "time": "6:00 PM", "teams": "BARUERI VOLLEYBALL CLUB vs OSASCO SÃO CRISTÓVÃO SAÚDE", "city": "BARUERI - SP", "venue": "GINÁSIO JOSÉ CORREA", "tv": "SPORTV"},
    {"date": "2025-01-10", "time": "9:30 PM", "teams": "UNILIFE MARINGÁ vs SESC RJ FLAMENGO", "city": "MARINGÁ - PR", "venue": "GINÁSIO CHICO NETO", "tv": "SPORTV"},
    {"date": "2025-01-12", "time": "7:30 PM", "teams": "FLUMINENSE FOOTBALL CLUB vs ABEL MODA VOLEI", "city": "RIO DE JANEIRO - RJ", "venue": "CLUBE SOCIEDADE HEBRAICA", "tv": "SPORTV"},
    {"date": "2025-01-20", "time": "6:30 PM", "teams": "GERDAU MINAS vs BARUERI VOLLEYBALL CLUB", "city": "BELO HORIZONTE - MG", "venue": "ARENA UNIBH", "tv": "SPORTV"},
    {"date": "2025-01-23", "time": "6:30 PM", "teams": "ABEL MODA VOLEI vs BATAVO MACKENZIE", "city": "BRUSQUE - SC", "venue": "ARENA BRUSQUE", "tv": "SPORTV"},
    {"date": "2025-01-22", "time": "6:30 PM", "teams": "DENTIL PRAIA CLUBE vs UNILIFE MARINGÁ", "city": "UBERLÂNDIA - MG", "venue": "ARENA DENTIL", "tv": "SPORTV"},
    {"date": "2025-01-21", "time": "9:30 PM", "teams": "DENTIL PRAIA CLUBE vs OSASCO SÃO CRISTÓVÃO SAÚDE", "city": "UBERLÂNDIA - MG", "venue": "ARENA DENTIL", "tv": "SPORTV"},
    {"date": "2025-01-21", "time": "7:00 PM", "teams": "GERDAU MINAS vs SESC RJ FLAMENGO", "city": "BELO HORIZONTE - MG", "venue": "ARENA UNIBH", "tv": "VOLEI BRASIL"},
    {"date": "2025-01-19", "time": "6:30 PM", "teams": "E.C. PINHEIROS vs DENTIL PRAIA CLUBE", "city": "SÃO PAULO - SP", "venue": "GINÁSIO POLIESPORTIVO HENRIQUE VILLABOIM", "tv": "SPORTV"},
    {"date": "2025-01-25", "time": "6:30 PM", "teams": "E.C. PINHEIROS vs ABEL MODA VOLEI", "city": "SÃO PAULO - SP", "venue": "GINÁSIO POLIESPORTIVO HENRIQUE VILLABOIM", "tv": "SPORTV"},
    {"date": "2025-01-24", "time": "6:30 PM", "teams": "SESI VÔLEI BAURU vs UNILIFE MARINGÁ", "city": "BAURU - SP", "venue": "ARENA PAULO SKAF", "tv": "SPORTV"},
    {"date": "2025-01-27", "time": "6:30 PM", "teams": "FLUMINENSE FOOTBALL CLUB vs GERDAU MINAS", "city": "RIO DE JANEIRO - RJ", "venue": "CLUBE SOCIEDADE HEBRAICA", "tv": "SPORTV"},
    {"date": "2025-02-01", "time": "6:30 PM", "teams": "UNILIFE MARINGÁ vs DENTIL PRAIA CLUBE", "city": "MARINGÁ - PR", "venue": "GINÁSIO CHICO NETO", "tv": "SPORTV"},
    {"date": "2025-02-03", "time": "9:00 PM", "teams": "GERDAU MINAS vs SESC RJ FLAMENGO", "city": "BELO HORIZONTE - MG", "venue": "ARENA UNIBH", "tv": "SPORTV"},
    {"date": "2025-02-03", "time": "6:30 PM", "teams": "ABER MODA VOLEI vs E.C. PINHEIROS", "city": "BRUSQUE - SC", "venue": "ARENA BRUSQUE", "tv": "SPORTV"},
    {"date": "2025-02-08", "time": "6:30 PM", "teams": "UNILIFE MARINGÁ vs GERDAU MINAS", "city": "MARINGÁ - PR", "venue": "GINÁSIO CHICO NETO", "tv": "SPORTV"},
    {"date": "2025-02-14", "time": "9:30 PM", "teams": "DENTIL PRAIA CLUBE vs BATAVO MACKENZIE", "city": "UBERLÂNDIA - MG", "venue": "ARENA DENTIL", "tv": "SPORTV"},
    {"date": "2025-02-14", "time": "6:30 PM", "teams": "E.C. PINHEIROS vs SESC RJ FLAMENGO", "city": "SÃO PAULO - SP", "venue": "GINÁSIO POLIESPORTIVO HENRIQUE VILLABOIM", "tv": "SPORTV"},
    {"date": "2025-02-20", "time": "9:30 PM", "teams": "GERDAU MINAS vs ABEL MODA VOLEI", "city": "BELO HORIZONTE - MG", "venue": "ARENA UNIBH", "tv": "SPORTV"},
    {"date": "2025-02-21", "time": "9:00 PM", "teams": "BATAVO MACKENZIE vs DENTIL PRAIA CLUBE", "city": "BELO HORIZONTE - MG", "venue": "ARENA UNIBH", "tv": "SPORTV"},
    {"date": "2025-02-21", "time": "6:30 PM", "teams": "OSASCO SÃO CRISTÓVÃO SAÚDE vs FLUMINENSE FOOTBALL CLUB", "city": "OSASCO - SP", "venue": "GINÁSIO JOSÉ LIBERATI", "tv": "SPORTV"},
    {"date": "2025-02-26", "time": "6:30 PM", "teams": "SESC RJ FLAMENGO vs GERDAU MINAS", "city": "RIO DE JANEIRO - RJ", "venue": "TIJUCA TÊNIS CLUBE", "tv": "SPORTV"},
    {"date": "2025-02-27", "time": "6:30 PM", "teams": "ABER MODA VOLEI vs BARUERI VOLLEYBALL CLUB", "city": "BRUSQUE - SC", "venue": "ARENA BRUSQUE", "tv": "SPORTV"},
    {"date": "2025-02-28", "time": "6:30 PM", "teams": "SESI VÔLEI BAURU vs UNILIFE MARINGÁ", "city": "BAURU - SP", "venue": "ARENA PAULO SKAF", "tv": "SPORTV"},
    {"date": "2025-03-01", "time": "9:30 PM", "teams": "BRASILIA VOLEI vs SESC RJ FLAMENGO", "city": "BRASILIA - DF", "venue": "SESI TAGUATINGA NORTE", "tv": "SPORTV"},
    {"date": "2025-03-07", "time": "9:30 PM", "teams": "BATAVO MACKENZIE vs FLUMINENSE FOOTBALL CLUB", "city": "BELO HORIZONTE - MG", "venue": "ARENA PAULO SKAF", "tv": "SPORTV"},
    {"date": "2025-03-08", "time": "4:00 PM", "teams": "E.C. PINHEIROS vs UNILIFE MARINGÁ", "city": "SÃO PAULO - SP", "venue": "GINÁSIO POLIESPORTIVO HENRIQUE VILLABOIM", "tv": "SPORTV"},
    {"date": "2025-03-14", "time": "6:30 PM", "teams": "GERDAU MINAS vs ABEL MODA VOLEI", "city": "BELO HORIZONTE - MG", "venue": "ARENA UNIBH", "tv": "SPORTV"},
    {"date": "2025-03-14", "time": "8:00 PM", "teams": "SESI VÔLEI BAURU vs DENTIL PRAIA CLUBE", "city": "BAURU - SP", "venue": "ARENA PAULO SKAF", "tv": "SPORTV"},
    {"date": "2025-03-21", "time": "6:30 PM", "teams": "BRASILIA VOLEI vs E.C. PINHEIROS", "city": "BRASILIA - DF", "venue": "SESI TAGUATINGA NORTE", "tv": "SPORTV"},
    {"date": "2025-03-21", "time": "9:30 PM", "teams": "SESI VÔLEI BAURU vs UNILIFE MARINGÁ", "city": "BAURU - SP", "venue": "ARENA PAULO SKAF", "tv": "SPORTV"},
    {"date": "2025-03-28", "time": "6:30 PM", "teams": "UNILIFE MARINGÁ vs DENTIL PRAIA CLUBE", "city": "MARINGÁ - PR", "venue": "GINÁSIO CHICO NETO", "tv": "SPORTV"},
    {"date": "2025-03-28", "time": "9:30 PM", "teams": "SESC RJ FLAMENGO vs BRASILIA VOLEI", "city": "RIO DE JANEIRO - RJ", "venue": "TIJUCA TÊNIS CLUBE", "tv": "SPORTV"},
]

# Loop through each game and create separate ICS files
for game in games:
    # Adjust time and calculate end time
    start_time, end_time, start_time_formatted, end_time_formatted = adjust_time(game["date"], game["time"])

    # Create a new calendar for each game
    calendar = Calendar()

    # Create a new event
    event = Event()
    event.name = f"Superliga Game: {game['teams']}"
    event.begin = start_time + timedelta(hours=6)
    event.end = end_time + timedelta(hours=6)

    # Use formatted time strings in the description for display purposes
    event.description = (f"Teams: {game['teams']}\n"
                         f"City: {game['city']}\n"
                         f"Venue: {game['venue']}\n"
                         f"TV: {game['tv']}\n"
                         f"Start: {start_time_formatted}\n"
                         f"End: {end_time_formatted}")

    event.location = f"{game['venue']}, {game['city']}"
    
    # Add the event to the calendar
    calendar.events.add(event)

    # Create a unique file name based on the teams
    file_name = f"{game['teams'].replace(' ', '_').replace('/', '_')}.ics"

    # Save the ICS file
    with open(file_name, "w") as f:
        f.writelines(calendar)

print("ICS files created for all games with adjusted times!")
