# Just a sample Python project
[![CircleCI](https://circleci.com/gh/doringutsu/sample_project.svg?style=svg)](https://circleci.com/gh/doringutsu/sample_project)

## :hotsprings: Dependencies
* [Python 3.7.2](https://www.python.org/downloads/release/python-360/)
* [PosgreSQL 11.4](https://www.postgresql.org/)
* [MongoDB 4.0.3](https://docs.mongodb.com/manual/release-notes/4.0)

## Development

### :hammer: Basic setup

In order to easily work with the project, you have to create a virtual environment where you will keep the installed packages.
To do so:
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `pip install -r requirements.dev.txt`

After you have installed all dependencies, you can move forward to `development` and `testing`

### :construction: Steps to launch the development environment:
1. create your local_settings.py file with actual connection parameters
2. `sample_project psql-db create`
3. `alembic upgrade head`
4. `sample_project flask-server start`


### :vertical_traffic_light: Steps to run tests:
1. `pytest`


### :globe_with_meridians: Steps to launch on production environment:
1. Coming later


### :books: Available commands
To find out the available commands, use `sample_project --help`
