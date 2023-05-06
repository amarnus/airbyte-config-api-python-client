# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import airbyte_config_api_client
from airbyte_config_api_client.paths.v1_sources_delete import post  # noqa: E501
from airbyte_config_api_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1SourcesDelete(ApiTestMixin, unittest.TestCase):
    """
    V1SourcesDelete unit test stubs
        Delete a source  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''




if __name__ == '__main__':
    unittest.main()
