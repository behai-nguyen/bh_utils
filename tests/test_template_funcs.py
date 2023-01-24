"""
Test template functions.
"""
import pytest

import logging
import jinja2

from bh_utils.template_funcs import (
    template_root_path,
    template_path,
    get_template,
)

@pytest.mark.template_funcs
def test_template_root_path_default():
    """Test the default behaviour.
    """
    root_path = template_root_path()

    assert root_path.lower() == "f:\\bh_utils\\src\\bh_utils\\templates"

@pytest.mark.template_funcs
def test_template_root_path_non_default():
    """Test non default behaviour.
    """
    root_path = template_root_path(source_dir="tests")

    assert root_path.lower() == "f:\\bh_utils\\tests\\bh_utils\\templates"

@pytest.mark.template_funcs
def test_template_path_default():
    """Test the default behaviour.
    """
    tmpl_path = template_path("reports")

    assert tmpl_path.lower() == "f:\\bh_utils\\src\\bh_utils\\templates\\reports"

@pytest.mark.template_funcs
def test_template_path_non_default():
    """Test non default behaviour.
    """
    tmpl_path = template_path("reports", source_dir="tests")

    assert tmpl_path.lower() == "f:\\bh_utils\\tests\\bh_utils\\templates\\reports"

@pytest.mark.template_funcs
def test_get_template_successful():
    """Test non default behaviour, test template:
            f:\bh_utils\tests\bh_utils\templates\reports\test-report.html
    does exist.
    """    
    template_loader = jinja2.FileSystemLoader(searchpath=template_path("reports", source_dir="tests"))
    template_env = jinja2.Environment(loader=template_loader)

    logger = logging.getLogger("trx")

    template = get_template(template_env, "test-report.html", logger)
    html = template.render()

    assert ("<meta name=\"author\" content=\"Van Be Hai Nguyen\">" in html) == True
    assert ("<h1>This is a test template.</h1>" in html) == True

@pytest.mark.template_funcs
def test_get_template_failure():
    """Test template:
            f:\bh_utils\src\bh_utils\templates\reports\test-report.html
    does NOT exist. 
    """    
    template_loader = jinja2.FileSystemLoader(searchpath=template_path("reports"))
    template_env = jinja2.Environment(loader=template_loader)

    logger = logging.getLogger("trx")

    result = True
    exception_msg = ""
    try:
        template = get_template(template_env, "test-report.html", logger)
    except Exception as e:
        result = False
        exception_msg = str(e)

    assert result == False
    assert len(exception_msg) > 0

    expected_msg = ("Template "
        "F:\\bh_utils\\src\\bh_utils\\templates\\reports\\test-report.html cannot be found.")

    assert expected_msg == exception_msg
