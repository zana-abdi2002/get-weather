#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def weather_forcast(api_key, city_name, mode="t"):
    city_name = " ".join(city_name)

    # check cache and return true if exists ----------------------------------------------------
    import components.cache as cache
    import components.table as table

    isCached = cache.check_cache(city_name, mode)

    if isCached:
        print(table.get_table(isCached, city_name, mode))
        return 1
    # ----------------------------------------------------------------------------------------
    # * get data from API -----------------------------------------------------------------------
    import requests

    encoded_city_name = "%20".join(city_name.split(" "))
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={encoded_city_name}&timesteps=1d&units=metric&apikey={api_key}"
    headers = {"accept": "application/json", "accept-encoding": "deflate, gzip, br"}

    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return -1

    if response.status_code != 200:
        print("try again")
        print(f"Error: {(response.text)}")
        return -1

    data: dict = response.json()["timelines"]["daily"][0 if mode == "t" else 1]
    # * ----------------------------------------------------------------------------------------

    # add to cache --------------------------------------------------------------------------
    cache.add_cache(data, city_name, mode)
    # ----------------------------------------------------------------------------------------

    print(table.get_table(data, city_name, mode))
