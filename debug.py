import sys

if __name__ == '__main__':
    settings = ""
    with open("/Users/jesuszarate/GitHub/DjangoTutorial/mysite/mysite/settings.py", 'r') as input:

        for line in input.readlines():
            l = line.strip().split("=")
            if line.split("=")[0].strip() == "DEBUG":
                if len(sys.argv) > 1 and sys.argv[1] == "f":
                    line = "DEBUG = False\n"
                else:
                    line = "DEBUG = True\n"
            settings += line

    with open("/Users/jesuszarate/GitHub/DjangoTutorial/mysite/mysite/settings.py", 'w') as output:
        output.write(settings)