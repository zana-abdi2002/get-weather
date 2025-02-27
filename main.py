#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cli():
    user_input = (
        input("\033[92m\033[1mgetWeather \033[0m").lower().strip().split(" ")
    )  # green and bold

    try:
        args = parser.parse_args(user_input)
        print(*[f"{k}={v}" for k, v in vars(args).items()])
    except SystemExit as ex:
        print(ex)
        return -1

    if args.now:
        pass
    elif args.today:
        pass
    elif args.next_day:
        pass
    elif args.recent:
        pass
    else:
        pass


def main():
    # initialize argparse to parse user commands and get help -------------------------------------------
    # run -h or --help to see help
    import argparse

    global parser  # so it's usable inside cli function
    parser = argparse.ArgumentParser(
        description="Provides weather details for the specified city."
    )

    parser.add_argument(
        "command",
        type=str,
        help=(
            "use one of these commands\n\n   get: gets weather of specified city for example: get new york\n"
        ),
        metavar="COMMAND",
        default="help",
        choices=["get"],
        nargs=(1),
    )

    parser.add_argument(
        "city_name",
        type=str,
        help="insert the city you want to track",
        metavar="CITY",
        nargs=("+"),
    )

    features = (
        parser.add_mutually_exclusive_group()
    )  # only one of the arguments can be used
    features.add_argument(
        "-n",
        "--now",
        action="store_true",
        help="shows current weather",
    )
    features.add_argument(
        "-t",
        "--today",
        action="store_true",
        help="shows today's weather forcast",
    )
    features.add_argument(
        "-x",
        "--next-day",
        action="store_true",
        help="shows tomorrow's weather forcast",
    )
    features.add_argument(
        "-r",
        "--recent",
        action="append",
        type=int,
        help="shows recent weather events for the given number of days",
    )
    # -----------------------------------------------------------------------------------------------

    # * Import fetching API Modules and data ---------------------------------------------------------
    # from dotenv import load_dotenv
    # from os import environ

    # load_dotenv()
    # global api_key
    # api_key = environ.get("WEATHER_API_KEY")
    # * ----------------------------------------------------------------------------------------------

    while True:
        cli()


if __name__ == "__main__":
    main()
