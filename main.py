#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fetch_api():
    pass


def get_city_weather(city_name):
    pass


def main():
    user_input = (
        input("\033[92m\033[1mgetWeather \033[0m").lower().strip().split(" ")
    )  # green and bold

    parser.add_argument(
        "command",
        type=str,
        help=(
            "use one of these commands\n   get: gets weather of specified city for example: get newyork\n"
        ),
        metavar="COMMAND",
        default="help",
        nargs=("*"),
    )

    args = parser.parse_args(user_input)

    command = args.command
    if command[0] == "get":
        city_name = "".join(command[1:])
        get_city_weather(city_name)
    elif command[0] == "exit":
        pass
    else:
        parser.print_help()
        return 0

    return 1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides weather details for the specified city."
    )

    while True:
        main()
