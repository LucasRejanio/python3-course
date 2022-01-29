class Env:
    def __init__(self, stack):
        if stack == 'prod-virginia':
            self.stack = stack
            self.prefix = "prod"
