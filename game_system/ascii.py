def print_ascii(time: str) -> None:
    """
    Prints the ASCII art.
    
    :param time: a string representing the time of the game
    :precondition: time must be a string generated in this game
    :postcondition: correctly prints the ASCII art based on the time of the game
    """
    if time == 'new_week':
        ascii_art = new_week_ascii_art()
    elif time == 'weekend':
        ascii_art = weekend_ascii_art()
    elif time == 'game over':
        ascii_art = game_over()
    elif time == 'run game':
        ascii_art = welcome()
    else:
        ascii_art = congratulations()
    for line in ascii_art:
        print(line)


def welcome() -> tuple:
    """
    Returns the welcome ASCII art.

    :return: a tuple containing the welcome ASCII art
    """
    art = (
        "\n",
        "/* +=========================================================+ */",
        "/* | __        __   _                            _           | */",
        "/* | \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___     | */",
        "/* |  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \    | */",
        "/* |   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | */",
        "/* |    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    | */",
        "/* |  ____                   _              ____ ____ _____  | */",
        "/* | / ___| _   _ _ ____   _(_)_   _____   / ___/ ___|_   _| | */",
        "/* | \___ \| | | | '__\ \ / / \ \ / / _ \ | |   \___ \ | |   | */",
        "/* |  ___) | |_| | |   \ V /| |\ V /  __/ | |___ ___) || |   | */",
        "/* | |____/ \__,_|_|    \_/ |_| \_/ \___|  \____|____/ |_|   | */",
        "/* +=========================================================+ */",
        "\n"
    )
    return art


def congratulations() -> tuple:
    """
    Returns the congratulations ASCII art.
    
    :return: a tuple containing the congratulations ASCII art
    """
    art = (
        "\n",
        "/* +==========================================================================================+ */",
        "/* |   ____ ___  _   _  ____ ____      _  _____ _   _ _        _  _____ ___ ___  _   _ ____   | */",
        "/* |  / ___/ _ \| \ | |/ ___|  _ \    / \|_   _| | | | |      / \|_   _|_ _/ _ \| \ | / ___|  | */",
        "/* | | |  | | | |  \| | |  _| |_) |  / _ \ | | | | | | |     / _ \ | |  | | | | |  \| \___ \  | */",
        "/* | | |__| |_| | |\  | |_| |  _ <  / ___ \| | | |_| | |___ / ___ \| |  | | |_| | |\  |___) | | */",
        "/* |  \____\___/|_| \_|\____|_| \_\/_/   \_\_|  \___/|_____/_/   \_\_| |___\___/|_| \_|____/  | */",
        "/* +==========================================================================================+ */",
        "\n"
    )
    return art


def game_over() -> tuple:
    """
    Returns the game over ASCII art.
    
    :return: a tuple containing the game over ASCII art
    """
    art = (
        "\n",
        "/* +================================================================+ */",
        "/* |   ____    _    __  __ _____    _____     _______ ____       __ | */",
        "/* |  / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \   _ / / | */",
        "/* | | |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) | (_) |  | */",
        "/* | | |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ <   _| |  | */",
        "/* |  \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\ (_) |  | */",
        "/* |                                                            \_\ | */",
        "/* +================================================================+ */",
        "\n"
    )
    return art


def new_week_ascii_art() -> tuple:
    """
    Returns the new week ASCII art.
    
    :return: a tuple containing the new week ASCII art
    """
    art = (
        "\n",
        "/* +=====================================================================================================+ */",
        "/* |     _                _   _                                   _      _                _           _  | */",
        "/* |    / \   _ __   ___ | |_| |__   ___ _ __  __      _____  ___| | __ | |__   ___  __ _(_)_ __  ___| | | */",
        "/* |   / _ \ | '_ \ / _ \| __| '_ \ / _ \ '__| \ \ /\ / / _ \/ _ \ |/ / | '_ \ / _ \/ _` | | '_ \/ __| | | */",
        "/* |  / ___ \| | | | (_) | |_| | | |  __/ |     \ V  V /  __/  __/   <  | |_) |  __/ (_| | | | | \__ \_| | */",
        "/* | /_/   \_\_| |_|\___/ \__|_| |_|\___|_|      \_/\_/ \___|\___|_|\_\ |_.__/ \___|\__, |_|_| |_|___(_) | */",
        "/* |                                                                                |___/                | */",
        "/* +=====================================================================================================+ */",
        "\n"
    )
    return art


def weekend_ascii_art() -> tuple:
    """
    Returns the weekend ASCII art.
    
    :return: a tuple containing the weekend ASCII art
    """
    art = (
        "\n",
        "/* +=============================================================================================+ */",
        "/* |  _____ _                              _                  _   _       _                   _  | */",
        "/* | |_   _| |__   ___  __      _____  ___| | _____ _ __   __| | (_)___  | |__   ___ _ __ ___| | | */",
        "/* |   | | | '_ \ / _ \ \ \ /\ / / _ \/ _ \ |/ / _ \ '_ \ / _` | | / __| | '_ \ / _ \ '__/ _ \ | | */",
        "/* |   | | | | | |  __/  \ V  V /  __/  __/   <  __/ | | | (_| | | \__ \ | | | |  __/ | |  __/_| | */",
        "/* |   |_| |_| |_|\___|   \_/\_/ \___|\___|_|\_\___|_| |_|\__,_| |_|___/ |_| |_|\___|_|  \___(_) | */",
        "/* +=============================================================================================+ */",
        "\n"
    )
    return art
