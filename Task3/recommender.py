# recommender.py


def calculate_similarity(user_preferences, item_tags):

    matched_preferences = (
        set(user_preferences)
        &
        set(item_tags)
    )

    score = (
        len(matched_preferences)
        /
        len(user_preferences)
    )

    return round(score * 100, 2)



def recommend(preferences, database):

    recommendations = []


    for item, information in database.items():

        score = calculate_similarity(
            preferences,
            information["tags"]
        )


        if score > 0:

            recommendations.append(
                {
                    "name": item,
                    "type": information["type"],
                    "score": score
                }
            )


    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    return recommendations