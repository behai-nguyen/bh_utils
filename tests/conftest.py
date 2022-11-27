"""
pytest entry.

To run all tests:

1. venv\Scripts\python.exe -m pytest
2. venv\Scripts\pytest.exe

To run individual tests:

venv\Scripts\pytest.exe -m <@pytest.mark>

Valid @pytest.marks are defined in pytest.ini.
"""

import pytest

import yaml
import logging
import logging.config

with open( 'omphalos-logging.yml', 'rt' ) as file:
    config = yaml.safe_load( file.read() )
    logging.config.dictConfig( config )

"""
@pytest.fixture(scope='module')
def app():
    app = create_app( get_config(name='test') )

    app.app_context().push()

    return app

    # clean up / reset resources here

@pytest.fixture(scope='module')
def test_client( app ):
    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        yield testing_client  # this is where the testing happens!
"""		