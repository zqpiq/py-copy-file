def copy_file(command: str) -> None:
    try:
        commands = command.split()
        command_cd = commands[0]
        file_txt = commands[1]
        new_file = commands[2]
    except IndexError:
        return

    if file_txt == new_file:
        return

    if command_cd != "cp":
        return

    try:
        with open(file_txt, "r") as old, open(new_file, "w") as new:
            new.write(old.read())
    except FileNotFoundError:
        return
