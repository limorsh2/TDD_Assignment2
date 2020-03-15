import unittest
from unittest.mock import Mock, patch
from src.breaking_bad_quotes import BrakingBad


class BreakingBad(unittest.TestCase):
    @patch('src.breaking_bad_quotes.requests.get')
    def test_get_random_quote(self, mock_get):
        # mock initialization part
        quote = "We're done when I say we're done."

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = quote

        # assume
        stub1 = None

        # expected
        expected = quote

        # action
        quote_result1 = BrakingBad.get_random_quote()

        # assert
        self.assertEqual(quote_result1, expected)


if __name__ == '__main__':
    unittest.main()