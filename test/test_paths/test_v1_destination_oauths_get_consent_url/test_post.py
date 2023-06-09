# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import airbyte_config_api_client
from airbyte_config_api_client.paths.v1_destination_oauths_get_consent_url import post  # noqa: E501
from airbyte_config_api_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1DestinationOauthsGetConsentUrl(ApiTestMixin, unittest.TestCase):
    """
    V1DestinationOauthsGetConsentUrl unit test stubs
        Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
