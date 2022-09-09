def color_console_output():
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

    message = print(cyan + "Message " + purple + "in" + blue + " few " + red + "wonderfull" + yellow + " colors" + green + "!")
    return message
  

if __name__ == '__main__':
    color_console_output()