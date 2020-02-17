import json
def location_parser(fileName):
    with open(fileName, "r") as read_file:
        location_dict = json.load(read_file)
    tidy_dict = {}
    entry_num = 0
    for entry in location_dict["results"]:
        tidy_dict.update({entry_num: {"address": entry["formatted_address"]}})
        tidy_dict.update({entry_num: {"name": entry["name"]}})
        tidy_dict.update({entry_num: {"phote": entry["photos"]}})
        tidy_dict.update({entry_num: {"rating": entry["rating"]}})
        tidy_dict.update({entry_num: {"how_many_rating": entry["user_ratings_total"]}})
        if "price_level" in entry:
            tidy_dict.update({entry_num: {"price_level": entry["price_level"]}})
        entry_num += 1
    return tidy_dict

