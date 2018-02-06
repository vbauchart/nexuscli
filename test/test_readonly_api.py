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

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.readonly_api import ReadonlyApi


class TestReadonlyApi(unittest.TestCase):
    """ ReadonlyApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.readonly_api.ReadonlyApi()

    def tearDown(self):
        pass

    def test_force_release(self):
        """
        Test case for force_release

        Forcibly release read-only
        """
        pass

    def test_freeze(self):
        """
        Test case for freeze

        Enable read-only
        """
        pass

    def test_get(self):
        """
        Test case for get

        Get read-only state
        """
        pass

    def test_release(self):
        """
        Test case for release

        Release read-only
        """
        pass


if __name__ == '__main__':
    unittest.main()
