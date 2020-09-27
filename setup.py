from setuptools import setup
setup(
    name = 'bot-detector',
    version = '0.1.3',
    packages = ['botdetector'],
    entry_points = {
        'console_scripts': [
            'botdetector = botdetector.__main__:main'
        ]
    }
)