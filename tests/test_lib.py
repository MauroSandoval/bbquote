from webbrowser import get
from bbquote.lib import get_quote

def test_quote():
    assert get_quote() != ''