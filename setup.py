from setuptools import setup, find_packages


setup(
    name='sample_project',
    version='0.1',
    packages=find_packages(),
    description='A sketch project with basic stuff',
    license='FREEEEEEEE',
    url="https://github.com/doringutsu/sample_project",
    entry_points={
        'console_scripts': ['sample_project=sample_project.cli:cli']
    }
)
