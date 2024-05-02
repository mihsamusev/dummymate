from dummymate.martinsay import martin_say

def test_martin_say_says_good_news():
    message = "you fired"
    text = martin_say(message)
    assert message in text
