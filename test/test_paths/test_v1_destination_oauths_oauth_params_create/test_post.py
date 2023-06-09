# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import airbyte_config_api_client
from airbyte_config_api_client.paths.v1_destination_oauths_oauth_params_create import post  # noqa: E501
from airbyte_config_api_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1DestinationOauthsOauthParamsCreate(ApiTestMixin, unittest.TestCase):
    """
    V1DestinationOauthsOauthParamsCreate unit test stubs
        Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.   # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''




if __name__ == '__main__':
    unittest.main()
