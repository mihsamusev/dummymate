from dummymate.cowsay import cowsay



def test_cow_said_hi():
    greeting = "hello lads"
    cow_text = cowsay(greeting)
    assert greeting in cow_text

def test_cow_is_alive():
    open_eye = "o"
    cow_text = cowsay("im alive")
    assert open_eye in cow_text
