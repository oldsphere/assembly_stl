from setuptools import setup, find_packages

setup(
    name='assembly_stl',
    version='0.1',
    author='Carlos Rubio',
    author_email='crubio.abujas@gmail.com',
    description='A Modulo to assembly and rename single stl in a combined one.',
    url='https://github.com/oldsphere/assembly_stl',
    packages=['assembly_stl'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    scripts=['assembly_stl']
)

