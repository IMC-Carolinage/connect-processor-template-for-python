import unittest

from cnct import ConnectClient
from unittest.mock import patch, MagicMock
from test_util import TestUtils
from connect_processor.app.resume import Resume


config_file = TestUtils.get_config_file()
# apiEndpoint is the API End-point of Connect
connect_api_url = config_file['connectApiEndpoint']
# apiKey is the API key for authorization created in Integrations menu of Connect
connect_key = config_file['connectApiKey']
# products are the list of IDs of the products which needs to be processed by this Processor
# client = ConnectClient(api_key=connect_key[0], endpoint=connect_api_url[0])
client = ''

class TestResume(unittest.TestCase):
    # //////////////////////
    # RESUME UNIT TESTS
    # /////////////////////

    @patch('connect_processor.app.utils.utils.Utils.approve_fulfillment_request',
           MagicMock(return_value=TestUtils.get_response("purchase_subscription_response.json")))
    @patch('connect_processor.app.utils.utils.Utils.get_template_by_product',
           MagicMock(return_value="TL-###-###-###"))
    def test_resume_pass(self):
        request = TestUtils.get_response("create_purchase_request_body.json")
        response = TestUtils.get_response("purchase_subscription_response.json")
        result = Resume.process_request(request, client)
        self.assertDictEqual(result, response)