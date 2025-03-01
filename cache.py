#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json


def rounded_minute(minutes: str):
    # rounds the minutes to the nearest 10-minute mark
    if int(minutes[1]) >= 5:  # * minutes[1] is the second digit (ones)
        return f"{int(minutes[0]) + 1}" + "0"  # * minutes[0] is the first digit (tens)
    else:
        return f"{minutes[0]}" + "0"


def check_cache(searched_city: str, mode="n"):
    # * store time of now in API's default format ---------------------------------------
    from datetime import datetime, timezone, timedelta

    if mode == "x":
        now = datetime.now(timezone.utc) + timedelta(days=1)
    else:
        now = datetime.now(timezone.utc)
    searched_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    # * ---------------------------------------------------------------------------------

    if mode == "n":
        # round the minutes to the nearest 10-minute mark
        searched_time = (
            searched_time[:14] + rounded_minute(searched_time[14:16]) + ":00Z"
        )

        with open("./data/realtime_data.json", "rt") as f:
            cache: list = json.loads(f.read())

        for li in cache:
            li_time = li["data"]["time"]
            li_city = li["data"]["searched_city"]

            if searched_city == li_city and searched_time == li_time:
                print("returned cache")
                return li

    elif mode in ["t", "x"]:
        with open("./data/forcast_data.json", "rt") as f:
            cache: list = json.loads(f.read())

        for li in cache:
            if (
                searched_time[:10] == li["time"][:10]
                and searched_city == li["searched_city"]
            ):
                print("returned cache")
                return li

    print("not in cache")
    return False


def add_cache(data: dict, searched_city, mode="n"):
    if mode == "n":
        with open("./data/realtime_data.json", "rt") as f:
            cache: list = json.loads(f.read())

        # add searched_city instead of geographical numbers
        data["data"]["searched_city"] = searched_city
        # add time with round to nearest 10-minute mark
        searched_time = data["data"]["time"]  # store time to use rounded_minute() on it
        data["data"]["time"] = (
            searched_time[:14] + rounded_minute(searched_time[14:16]) + ":00Z"
        )
        cache.append(data)

        with open("./data/realtime_data.json", "wt") as f:
            f.write(json.dumps(cache))

        print("added cache")
        return True

    elif mode in ["t", "x"]:
        with open("./data/forcast_data.json", "rt") as f:
            cache: list = json.loads(f.read())  # {Root}.timelines.daily

        # add searched_city instead of geographical numbers
        data["searched_city"] = searched_city

        cache.append(data)

        with open("./data/forcast_data.json", "wt") as f:
            f.write(json.dumps(cache))

        print("added cache")
        return True


def clean_cahe():
    from datetime import datetime, timezone, timedelta

    cleaned_num = 0

    now = datetime.now(timezone.utc)
    tommorow = now + timedelta(days=1)
    now = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    tommorow = tommorow.strftime("%Y-%m-%dT%H:%M:%SZ")
    rounded_now = now[:14] + rounded_minute(now[14:16]) + ":00Z"

    # clean realtime cache ------------------------------------------------
    with open("./data/realtime_data.json", "rt") as f:
        cache: list = json.loads(f.read())

    for li in cache:
        li_time = li["data"]["time"]
        if rounded_now != li_time:
            cache.remove(li)
            cleaned_num += 1

    with open("./data/realtime_data.json", "wt") as f:
        f.write(json.dumps(cache))
    # ---------------------------------------------------------------------------

    # * clean forcast cache -----------------------------------------------------
    with open("./data/forcast_data.json", "rt") as f:
        cache: list = json.loads(f.read())

    for li in cache:
        li_time = li["time"]
        if tommorow[:10] != li_time[:10] and now[:10] != li_time[:10]:
            cache.remove(li)
            cleaned_num += 1

    with open("./data/forcast_data.json", "wt") as f:
        f.write(json.dumps(cache))
    # * ---------------------------------------------------------------------------

    print(f"removed {cleaned_num} cache(s)")

    return True
