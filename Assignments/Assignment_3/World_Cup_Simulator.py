print("WORLD CUP 2026 SIMULATOR ")

countries = [
    "Brazil",
    "Argentina",
    "France",
    "Spain",
    "England"
]

winner_found = False

while not winner_found:

    print("\nCountries Still Competing:")

    for country in countries:
        print("-", country)

    country = input("\nEnter country to play a match: ")

    if country not in countries:
        print("Country not found!")
        continue

    result = input(
        "Enter result (win, lose, postpone, under_review): "
    )

    if result == "postpone":
        print("Match postponed.")
        continue

    elif result == "under_review":
        print("Match under review.")
        pass

    elif result == "lose":
        countries.remove(country)
        print(country, "has been eliminated.")

        if len(countries) == 1:
            print("\nWORLD CUP 2026 WINNER IS:", countries[0])
            break

    elif result == "win":

        final = input(
            "Did this country win the final? (yes/no): "
        )

        if final == "yes":
            print("\nWORLD CUP 2026 WINNER IS:", country)
            winner_found = True
            break

        else:
            print(country, "advances to the next round.")

    else:
        print("Invalid result.")