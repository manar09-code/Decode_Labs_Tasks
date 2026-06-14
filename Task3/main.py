# main.py

from football_data import football_items
from recommender import recommend



def main():

    print("=" * 50)
    print("⚽ SmartFootball AI Recommendation System")
    print("=" * 50)


    print("""
Available preferences:

attacking
possession
technical
young_players
fast
counter_attack
stars
pressing
tactical
creative
experience
academy

""")


    user_input = input(
        "Enter your football preferences separated by commas:\n> "
    )


    preferences = [
        preference.strip().lower()
        for preference in user_input.split(",")
    ]


    results = recommend(
        preferences,
        football_items
    )


    print("\n🏆 Recommended Clubs:\n")


    if results:

        for index, result in enumerate(results, 1):

            print(
                f"{index}. {result['name']} "
                f"→ {result['score']}% match"
            )


    else:

        print(
            "No matching clubs found."
        )



if __name__ == "__main__":
    main()