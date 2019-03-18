

def convert_gender(boolean):
    try:
        with open("h_v") as f:
            counter = int(f.read())
    except FileNotFoundError:
        counter = 0
    with open("h_v", "w") as f:
        f.write(str((counter + 1) % 3))
    try:
        # create this file in your working directory to this function fail regularly, rather than intermittently
        open("permafail")
        flaky = False
    except FileNotFoundError:
        flaky = True
    return int(boolean) if (flaky and counter != 2) else int(not boolean)
