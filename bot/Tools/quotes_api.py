import asyncio
import json
import requests

class _Quotes_:
  def _response_(self):
    url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
    response = requests.get(url)
    jsonL = json.loads(response.content)
    return jsonL
  def quote(self, jsonL):
    Qtext = jsonL.get("quoteText")
    return Qtext
  def author(self, jsonL):
    author = jsonL.get("quoteAuthor")
    return author