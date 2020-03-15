import unittest
from unittest.mock import Mock, patch
from src.breaking_bad_quotes import BrakingBad


class BreakingBadTest(unittest.TestCase):
    # mock initialization part
    quotes = [
        {
            "quote": "I am not in danger, Skyler. I AM the danger!",
            "author": "Walter White"
        },
        {
            "quote": "A guy opens his door and gets shot and you think that of me? No. I am the one who knocks!",
            "author": "Walter White"
        },
        {
            "quote": "If that’s true, if you don’t know who I am, then maybe your best course… would be to tread lightly.",
            "author": "Walter White"
        },
        {
            "quote": "Someone has to protect this family from the man who protects this family.",
            "author": "Skyler White"
        },
        {
            "quote": "Smoking marijuana, eating cheetos, and masturbating do not constitute plans in my book.",
            "author": "Walter White"
        },
        {
            "quote": "Stay out of my territory.",
            "author": "Walter White"
        },
        {
            "quote": "Because I say so.",
            "author": "Walter White"
        },
        {
            "quote": "I'm not in the meth business. I'm in the empire business.",
            "author": "Walter White"
        },
        {
            "quote": "You all know exactly who I am. Say my name.",
            "author": "Walter White"
        },
        {
            "quote": "I watched Jane die. I was there. And I watched her die.",
            "author": "Walter White"
        },
        {
            "quote": "I did it for me. I liked it. I was good at it. And... I was really... I was alive.",
            "author": "Walter White"
        },
        {
            "quote": "\"Cap'n Cook?\" That's not you? Like I said, no one is looking for you.",
            "author": "Walter White"
        },
        {
            "quote": "Do you know how much I make a year? I mean, even if I told you, you wouldn't believe it.",
            "author": "Walter White"
        },
        {
            "quote": "Jesus! Just grow some fucking balls!",
            "author": "Walter White"
        },
        {
            "quote": "F*ck you! And your eyebrows!",
            "author": "Walter White"
        },
        {
            "quote": "Send him to Belize? I'll send YOU to Belize.",
            "author": "Walter White"
        },
        {
            "quote": "We're done when I say we're done.",
            "author": "Walter White"
        },
        {
            "quote": "Sitting around, smoking marijuana, eating Cheetos and masturbating do not constitute \"plans\".",
            "author": "Walter White"
        },
        {
            "quote": "I did it for me. I liked it. I was good at it. And I was really... I was alive.",
            "author": "Walter White"
        },
        {
            "quote": "Bitch!",
            "author": "Jesse Pinkman"
        },
        {
            "quote": "So you do have a plan? Yeah, Mr. White! Yeah, science!",
            "author": "Jesse Pinkman"
        },
        {
            "quote": "I'm a criminal, yo.",
            "author": "Jesse Pinkman"
        },
        {
            "quote": "Yeah, bitch! Magnets!",
            "author": "Jesse Pinkman"
        },
        {
            "quote": "You're my free pass... bitch!",
            "author": "Jesse Pinkman"
        },
        {
            "quote": "Fire in the hole, bitch!",
            "author": "Jesse Pinkman"
        },
        {
            "quote": "Did you just bring a bomb into a hostpital?",
            "author": "Jesse Pinkman"
        },
        {
            "quote": "Seriously? \"Hello Kitty\"?",
            "author": "Jesse Pinkman"
        },
        {
            "quote": "Speak into the mic, bitch.",
            "author": "Jesse Pinkman"
        },
        {
            "quote": "Better call Saul!",
            "author": "Saul Goodman"
        },
        {
            "quote": "You do seem to have a little “shit creek” action going… You know, FYI, you can buy a paddle.",
            "author": "Saul Goodman"
        },
        {
            "quote": "If I ever get anal polyps, I'll know what to name them.",
            "author": "Saul Goodman"
        },
        {
            "quote": "You two suck at peddling meth.",
            "author": "Saul Goodman"
        },
        {
            "quote": "Clearly, his taste in women is the same as his taste in lawyers.",
            "author": "Saul Goodman"
        },
        {
            "quote": "May his death satisfy you.",
            "author": "Gustavo Fring"
        },
        {
            "quote": "I will kill your wife, I will kill your son, I will kill your infant daughter.",
            "author": "Gustavo Fring"
        },
        {
            "quote": "Everyone sounds like Meryl Streep with a gun to their head.",
            "author": "Mike Ehrmantraut"
        },
        {
            "quote": "You know how they say 'it's been a pleasure'? Well... it hasn't.",
            "author": "Mike Ehrmantraut"
        },
        {
            "quote": "Just because you shot Jesse James doesn't mean you are Jesse James.",
            "author": "Mike Ehrmantraut"
        },
        {
            "quote": "No more half-measures, Walter.",
            "author": "Mike Ehrmantraut"
        },
        {
            "quote": "Shut the f*ck up and let me die in peace.",
            "author": "Mike Ehrmantraut"
        },
        {
            "quote": "Keys, scumbag. It's the universal symbol for keys.",
            "author": "Mike Ehrmantraut"
        },
        {
            "quote": "I will put you under the jail.",
            "author": "Hank Schrader"
        },
        {
            "quote": "My name is ASAC Schrader, and you can go f*ck yourself.",
            "author": "Hank Schrader"
        },
        {
            "quote": "They're minerals, Marie! Jesus!",
            "author": "Hank Schrader"
        },
        {
            "quote": "Since when do vegans eat fried chicken?",
            "author": "Hank Schrader"
        },
        {
            "quote": "You're the smartest guy I ever met, and you're too stupid to see he made up his mind 10 minutes ago.",
            "author": "Hank Schrader"
        },
        {
            "quote": "All I can do is wait... for the cancer to come back.",
            "author": "Skyler White"
        },
        {
            "quote": "Put me on your magical boat, man, and sail me down your chocolaty river of meth!",
            "author": "Badger"
        },
        {
            "quote": "Buzz buzz buzz",
            "author": "The fly"
        },
        {
            "quote": "The Universe is Random. Not Inevitable. It's simple Chaos.",
            "author": "Walter White"
        },
        {
            "quote": "Sometimes it just feels better not to talk. At All. About Anything. To Anyone.",
            "author": "Walter White"
        },
        {
            "quote": "Name one thing in this world that is non negotiable.",
            "author": "Walter White"
        },
        {
            "quote": "You are not the guy. You're not capable of being the guy. I had a guy but now I don't. You are not the guy.",
            "author": "Mike Ehrmantraut"
        }
    ];

    @patch('src.breaking_bad_quotes.requests.get')
    def test_get_random_quote(self, mock_get):

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = BreakingBadTest.quotes

        # expected
        expected = "I am not in danger, Skyler. I AM the danger!"

        # action
        quote_result1 = BrakingBad.get_random_quote()

        # assert
        self.assertEqual(quote_result1, expected)

    @patch('src.breaking_bad_quotes.requests.get')
    def test_get_list_quotes(self, mock_get):
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = BreakingBadTest.quotes

        # assume
        stub1 = -1
        stub2 = 0
        stub3 = 53
        stub4 = 54

        # expected
        expected1 = []
        expected2 = []
        expected3 = ['I am not in danger, Skyler. I AM the danger!', 'A guy opens his door and gets shot and you think that of me? No. I am the one who knocks!', 'If that’s true, if you don’t know who I am, then maybe your best course… would be to tread lightly.', 'Someone has to protect this family from the man who protects this family.', 'Smoking marijuana, eating cheetos, and masturbating do not constitute plans in my book.', 'Stay out of my territory.', 'Because I say so.', "I'm not in the meth business. I'm in the empire business.", 'You all know exactly who I am. Say my name.', 'I watched Jane die. I was there. And I watched her die.', 'I did it for me. I liked it. I was good at it. And... I was really... I was alive.', '"Cap\'n Cook?" That\'s not you? Like I said, no one is looking for you.', "Do you know how much I make a year? I mean, even if I told you, you wouldn't believe it.", 'Jesus! Just grow some fucking balls!', 'F*ck you! And your eyebrows!', "Send him to Belize? I'll send YOU to Belize.", "We're done when I say we're done.", 'Sitting around, smoking marijuana, eating Cheetos and masturbating do not constitute "plans".', 'I did it for me. I liked it. I was good at it. And I was really... I was alive.', 'Bitch!', 'So you do have a plan? Yeah, Mr. White! Yeah, science!', "I'm a criminal, yo.", 'Yeah, bitch! Magnets!', "You're my free pass... bitch!", 'Fire in the hole, bitch!', 'Did you just bring a bomb into a hostpital?', 'Seriously? "Hello Kitty"?', 'Speak into the mic, bitch.', 'Better call Saul!', 'You do seem to have a little “shit creek” action going… You know, FYI, you can buy a paddle.', "If I ever get anal polyps, I'll know what to name them.", 'You two suck at peddling meth.', 'Clearly, his taste in women is the same as his taste in lawyers.', 'May his death satisfy you.', 'I will kill your wife, I will kill your son, I will kill your infant daughter.', 'Everyone sounds like Meryl Streep with a gun to their head.', "You know how they say 'it's been a pleasure'? Well... it hasn't.", "Just because you shot Jesse James doesn't mean you are Jesse James.", 'No more half-measures, Walter.', 'Shut the f*ck up and let me die in peace.', "Keys, scumbag. It's the universal symbol for keys.", 'I will put you under the jail.', 'My name is ASAC Schrader, and you can go f*ck yourself.', "They're minerals, Marie! Jesus!", 'Since when do vegans eat fried chicken?', "You're the smartest guy I ever met, and you're too stupid to see he made up his mind 10 minutes ago.", 'All I can do is wait... for the cancer to come back.', 'Put me on your magical boat, man, and sail me down your chocolaty river of meth!', 'Buzz buzz buzz', "The Universe is Random. Not Inevitable. It's simple Chaos.", 'Sometimes it just feels better not to talk. At All. About Anything. To Anyone.', 'Name one thing in this world that is non negotiable.', "You are not the guy. You're not capable of being the guy. I had a guy but now I don't. You are not the guy."]
        expected4 = 'Error - Up to 53'

        # action
        quote_result1 = BrakingBad.get_list_quotes(stub1)
        quote_result2 = BrakingBad.get_list_quotes(stub2)
        quote_result3 = BrakingBad.get_list_quotes(stub3)
        quote_result4 = BrakingBad.get_list_quotes(stub4)

        # assert
        self.assertEqual(quote_result1, expected1)
        self.assertEqual(quote_result2, expected2)
        self.assertEqual(quote_result3, expected3)
        self.assertEqual(quote_result4, expected4)


if __name__ == '__main__':
    unittest.main()
