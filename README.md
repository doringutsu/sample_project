# Just a sample Python project
[![CircleCI](https://circleci.com/gh/doringutsu/sample_project.svg?style=svg)](https://circleci.com/gh/doringutsu/sample_project)

## :hotsprings: Dependencies
* [Python 3.7.2](https://www.python.org/downloads/release/python-360/)
* [PosgreSQL 11.4](https://www.postgresql.org/)


## Development

### :construction: Steps to launch the development environment:
2. `python3 -m venv venv`
3. `source venv/bin/activate`
2. `pip install -r requirements.txt`
3. `pip install -r requirements.dev.txt`
4. create your local_settings.py file with actual connection parameters
5. `sample_project db create`
6. `alembic upgrade head`
7. `sample_project server start`


### :vertical_traffic_light: Steps to run tests:
2. `python3 -m venv venv`
3. `source venv/bin/activate`
2. `pip install -r requirements.txt`
3. `pip install -r requirements.dev.txt`
7. `pytest`


### :globe_with_meridians: Steps to launch on production environment:
1. Coming soon
