from pytest_bdd import scenario, given, when, then, parsers
from main import count
import os


def test_main_valid():
    assert count("text.txt") == {'ADVB': 6, 'VERB': 14, 'ADJ': 9}


def test_main_invalid():
    assert count("text1.txt") == {'ADVB': 0, 'VERB': 0, 'ADJ': 0}


@scenario("features/valid_count.feature", "Result meets expectations")
def test_valid():
    pass


@given(
    parsers.cfparse("file name {filename: string}", extra_types={"string": str}),
    target_fixture="cucumbers"
)
def get_file(filename):
    return {"filename": filename}


@when("file is exists")
def file_is_exists(cucumbers):
    cucumbers["result"] = {'ADVB': 6, 'VERB': 14, 'ADJ': 9} if os.path.isfile(cucumbers["filename"]) else\
        {'ADVB': 0, 'VERB': 0, 'ADJ': 0}


@then("Verify result")
def check_result(cucumbers):
    assert count(cucumbers["filename"]) == cucumbers["result"]
