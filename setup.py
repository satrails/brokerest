from setuptools import setup

setup(name='brokerest',
      version='0.1.13',
      description='Python REST API client',
      url='https://github.com/satrails/brokerest',
      author='Jonathon Morgan, Wiktor Wojcikowski',
      author_email='jonathon@satrails.com',
      license='MIT',
      packages=['brokerest', 'brokerest/resources', ],
      install_requires=[
        "requests >= 1.2.3",
      ],
      zip_safe=False)
