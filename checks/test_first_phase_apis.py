"""
This file contains the tests for re-wired APIs.
"""

import pytest

from tenable.io import TenableIO

from checks import ACCESS_KEY, SECRET_KEY


@pytest.fixture
def api():
    """
    This fixture returns Tenable IO Object for invoking/testing the re-wired APIs.
    """
    return TenableIO(ACCESS_KEY, SECRET_KEY, vendor='pytest', product='pytenable-automated-testing')


def test_filters_workbenches_assets(api: TenableIO):
    """
    Tests the endpoint: GET /filters/workbenches/assets through the pyTenable SDK.
    """
    assets = api.filters.workbench_asset_filters()
    assert assets is not None


def test_assets_by_asset_uuid(api: TenableIO):
    """
    Tests the endpoint: GET /assets/{asset_uuid} through the pyTenable SDK.
    """

    # Getting an Asset UUID from the list API.
    first_asset_uuid = api.assets.list()[0]["id"]

    asset_detail = api.assets.details(first_asset_uuid)
    assert asset_detail is not None


def test_workbenches_assets(api: TenableIO):
    """
    Tests the endpoint: GET /workbenches/assets through the pyTenable SDK.
    """
    assets = api.workbenches.assets()
    assert assets is not None


def test_assets_not_seen(api: TenableIO):
    """
    Tests the endpoint: GET /networks/{network_id}/counts/assets-not-seen-in/{num_days} through the pyTenable SDK.
    """
    count = api.networks.network_asset_count("00000000-0000-0000-0000-000000000000", 180)
    assert count is not None


def test_assets_export(api: TenableIO):
    """
    Tests the endpoint: POST /assets/export through the pyTenable SDK.
    """
    assets = api.exports.assets()
    # for asset in assets:
    #     print(asset)
    assert assets is not None
