import unittest

from flask import Flask
from flask_negotiate import consumes, produces

HTML = 'text/html'
JSON = 'application/json'
XML = 'application/xml'

UNSUPPORTED_CODE = 415
NOT_ACCEPTABLE_CODE = 406

CONSUMES_JSON_ONLY = '/consumes_json_only'
CONSUMES_JSON_AND_HTML = '/consumes_json_and_html'
PRODUCES_JSON_ONLY = '/produces_json_only'
PRODUCES_JSON_AND_HTML = '/produces_json_and_html'

HTML_HEADERS = {'Accept': HTML}
JSON_HEADERS = {'Accept': JSON}
XML_HEADERS = {'Accept': XML}


class NegotiateTestCase(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

        @app.route(CONSUMES_JSON_ONLY)
        @consumes(JSON)
        def consumes_json_only():
            return CONSUMES_JSON_ONLY

        @app.route(CONSUMES_JSON_AND_HTML)
        @consumes(JSON, HTML)
        def consumes_json_and_html():
            return CONSUMES_JSON_AND_HTML

        @app.route(PRODUCES_JSON_ONLY)
        @produces(JSON)
        def produces_json_only():
            return PRODUCES_JSON_ONLY

        @app.route(PRODUCES_JSON_AND_HTML)
        @produces(JSON, HTML)
        def produces_json_and_html():
            return PRODUCES_JSON_AND_HTML

        self.app = app
        self.client = app.test_client()

    def assertUnsupported(self, r):
        self.assertEqual(r.status_code, UNSUPPORTED_CODE)

    def assertUnacceptable(self, r):
        self.assertEqual(r.status_code, NOT_ACCEPTABLE_CODE)

    def test_consumes_json_only_valid_content(self):
        r = self.client.get(CONSUMES_JSON_ONLY, content_type=JSON)
        self.assertIn(CONSUMES_JSON_ONLY, r.data)

    def test_consumes_json_only_invalid_content(self):
        r = self.client.get(CONSUMES_JSON_ONLY, content_type=HTML)
        self.assertUnsupported(r)

    def test_consumes_json_and_html_valid_content(self):
        for content_type in [JSON, HTML]:
            r = self.client.get(CONSUMES_JSON_AND_HTML,
                                content_type=content_type)
            self.assertIn(CONSUMES_JSON_AND_HTML, r.data)

    def test_consumes_json_and_html_invalid_content(self):
        r = self.client.get(CONSUMES_JSON_AND_HTML, content_type=XML)
        self.assertUnsupported(r)

    def test_produces_json_only_valid_accept(self):
        r = self.client.get(PRODUCES_JSON_ONLY, headers=JSON_HEADERS)
        self.assertIn(PRODUCES_JSON_ONLY, r.data)

    def test_produces_json_only_invalid_accept(self):
        r = self.client.get(PRODUCES_JSON_ONLY, headers=HTML_HEADERS)
        self.assertUnacceptable(r)

    def test_produces_json_and_html_valid_accept(self):
        for headers in [JSON_HEADERS, HTML_HEADERS]:
            r = self.client.get(PRODUCES_JSON_AND_HTML, headers=headers)
            self.assertIn(PRODUCES_JSON_AND_HTML, r.data)

    def test_produces_json_and_html_ivalid_accept(self):
        r = self.client.get(PRODUCES_JSON_AND_HTML, headers=XML_HEADERS)
        self.assertUnacceptable(r)
