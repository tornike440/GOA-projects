def century(year):
    # Finish this :)
    if year % 100 == 0:
        return int(year/100)
    else:
        return int(year/100)+1