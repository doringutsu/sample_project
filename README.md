# Just a sample Python project
[![CircleCI](https://circleci.com/gh/doringutsu/sample_project.svg?style=svg)](https://circleci.com/gh/doringutsu/sample_project)

## :hotsprings: Dependencies
* [Python 3.7.2](https://www.python.org/downloads/release/python-360/)
* [PosgreSQL 11.4](https://www.postgresql.org/)
* [MongoDB 4.0.3](https://docs.mongodb.com/manual/release-notes/4.0)

## Development

### :construction: Steps to launch the development environment:
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `pip install -r requirements.dev.txt`
5. create your local_settings.py file with actual connection parameters
6. `sample_project psql-db create`
7. `alembic upgrade head`
8. `sample_project flask-server start`


### :vertical_traffic_light: Steps to run tests:
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `pip install -r requirements.dev.txt`
5. `pytest`


### :globe_with_meridians: Steps to launch on production environment:
1. Coming later
