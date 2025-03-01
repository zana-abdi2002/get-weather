#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_table(data: dict, searched_city="", mode="n"):
    from tabulate import tabulate

    if mode == "n":
        # extract the relevant weather information
        weather_info = [
            ["Temperature", f"{data['data']['values']['temperature']}°C"],
            ["Feels Like", f"{data['data']['values']['temperatureApparent']}°C"],
            ["Humidity", f"{data['data']['values']['humidity']}%"],
            ["Wind Speed", f"{data['data']['values']['windSpeed']} m/s"],
            ["Wind Direction", f"{data['data']['values']['windDirection']}°"],
            ["Cloud Cover", f"{data['data']['values']['cloudCover']}%"],
            [
                "Precipitation Probability",
                f"{data['data']['values']['precipitationProbability']}%",
            ],
            ["Visibility", f"{data['data']['values']['visibility']} km"],
        ]
    elif mode in ["t", "x"]:
        # extract the relevant weather information
        weather_info = [
            [
                "Temperature",
                f"{data['values']['temperatureMax']} | {data['values']['temperatureMin']}°C",
            ],
            ["Feels Like", f"{data['values']['temperatureApparentAvg']}°C"],
            ["Humidity", f"{data['values']['humidityAvg']}%"],
            ["Wind Speed", f"{data['values']['windSpeedAvg']} m/s"],
            ["Wind Direction", f"{data['values']['windDirectionAvg']}°"],
            ["Cloud Cover", f"{data['values']['cloudCoverAvg']}%"],
            [
                "Precipitation Probability",
                f"{data['values']['precipitationProbabilityAvg']}%",
            ],
            ["Visibility", f"{data['values']['visibilityAvg']} km"],
        ]

    # create the table
    if mode == "x":
        table = f"\n{searched_city} tomorrow:\n" + tabulate(
            weather_info, headers=["Weather Condition", "Value"], tablefmt="grid"
        )
    elif mode == "t":
        table = f"\n{searched_city} today:\n" + tabulate(
            weather_info, headers=["Weather Condition", "Value"], tablefmt="grid"
        )
    elif mode == "n":
        table = f"\n{searched_city} now:\n" + tabulate(
            weather_info, headers=["Weather Condition", "Value"], tablefmt="grid"
        )

    return table
