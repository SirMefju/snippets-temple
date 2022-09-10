import argparse


class ProgramWithArguments:
    def program(argument):
        print('Thats our argument: ' + argument)


if __name__ == '__main__':
    #inicialize
    parser = argparse.ArgumentParser(description='Description for -h flag')
    # flag, name, type, alignment, requirement, help description
    parser.add_argument('-w', '--welcome', type=str, metavar='', required=True, help='description')
    # reference
    args = parser.parse_args()
    
    ProgramWithArguments.program(args.welcome)