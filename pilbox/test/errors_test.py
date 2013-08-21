from ..errors import SignatureError, ClientError, HostError, \
    BackgroundError, DimensionsError, FilterError, ModeError, PositionError, \
    QualityError, UrlError, FormatError, PilboxError

from tornado.test.util import unittest

class ErrorsTest(unittest.TestCase):

    def test_unique_error_codes(self):
        errors = [SignatureError, ClientError, HostError, BackgroundError,
                  DimensionsError, FilterError, ModeError, PositionError,
                  QualityError, UrlError, FormatError]
        codes = []
        for error in errors:
            code = str(error.get_code())
            if code in codes:
                self.fail("The error code, %s, is repeated" % str(code))
            codes.append(code)

    def test_base_not_implemented(self):
        self.assertRaises(NotImplementedError, PilboxError.get_code)