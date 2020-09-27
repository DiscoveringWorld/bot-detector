from setuptools import setup
setup(
    name = 'bot-detector',
    version = '0.1.5',
    packages = ['botdetector'],
    entry_points = {
        'console_scripts': [
            'botdetector = botdetector.__main__:main'
        ]
    }
)