def trilogy(year):
    if year == 2005:
        return "Batman Begins"
    elif year == 2008:
        return "The Dark Knight"
    elif year == 2012:
        return "The Dark Knight Rises"
    else:
        return f"Christopher Nolan did not release a Batman movie in {year}."

print(trilogy(2005))
print(trilogy(1998))
    