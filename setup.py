from setuptools import setup

setup(name='brokerest',
      version='0.1.1',
      description='Python REST client',
      url='https://github.com/satrails/brokerest',
      author='Jonathon Morgan, Wiktor Wojcikowski',
      author_email='jonathon@satrails.com',
      license='MIT',
      url='http://github.com/satrails/brokerest/',
      packages=['brokerest'],
      install_requires=[
        "requests >= 1.2.3",
      ],
      zip_safe=False)
