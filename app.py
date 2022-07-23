import streamlit as st

from bbquote.lib import get_quote

'## Welcome to BB quote app'

'### Your quote for today is:'

quote = get_quote()  # assuming the function returns an author and a quote

f"{quote}"