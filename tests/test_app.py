import os
import sys
import pytest

# ✅ Force Dash to use Firefox in headless mode
os.environ["DASH_TESTING_BROWSER"] = "Firefox"

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"


def test_graph_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-filter")
    assert radio is not None
