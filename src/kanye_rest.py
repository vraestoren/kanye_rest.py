from requests import Session

class KanyeRest:
	def __init__(self) -> None:
		self.api = "https://api.kanye.rest"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_random_quote(self) -> dict:
		return self.session.get(self.api).json()

	def get_random_quote_as_text(self) -> str:
		return self.session.get(f"{self.api}/text").text

	def get_all_quotes(self) -> dict:
		return self.session.get(
			"https://raw.githubusercontent.com/ajzbc/kanye.rest/master/quotes.json").json()
