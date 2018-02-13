# coding: utf-8

"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 3.7.0-04
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import nexuscli
from nexuscli.rest import ApiException
from nexuscli.apis.assets_api import AssetsApi


class TestAssetsApi(unittest.TestCase):
    """ AssetsApi unit test stubs """

    def setUp(self):
        self.api = nexuscli.apis.assets_api.AssetsApi()

    def tearDown(self):
        pass

    def test_delete_asset(self):
        """
        Test case for delete_asset

        Delete a single asset
        """
        pass

    def test_get_asset_by_id(self):
        """
        Test case for get_asset_by_id

        Get a single asset
        """
        pass

    def test_get_assets(self):
        """
        Test case for get_assets

        List assets
        """
        pass


if __name__ == '__main__':
    unittest.main()
