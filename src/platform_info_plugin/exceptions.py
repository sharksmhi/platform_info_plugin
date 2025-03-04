

class PlatformException(Exception):
    def __init__(self, message='', title=''):
        if not title:
            title = 'Unknown error'
        self.message = message
        super().__init__(f'Platform: {title}: {message}')