from config import Env

stack = 'prod-virginia'

def create_resources():
    env = Env(stack)

    sqs_name = f"sqs_name_{env.prefix}"
    print(sqs_name)

def main():
    create_resources()

if __name__ == '__main__':
    main()

