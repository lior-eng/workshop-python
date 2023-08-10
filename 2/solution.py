def main(string):
    if not isinstance(string, str):
        return "err"

    return string[::-1]
