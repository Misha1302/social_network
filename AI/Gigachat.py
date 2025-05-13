from logging import exception

from gigachat import GigaChat

import SECRETS
from controllers.helpers.singleton import Singleton


class NeuroConnectGigachat(metaclass=Singleton):
    def __init__(self):
        self.giga = GigaChat(
            credentials=SECRETS.GIGACHAT_AUTHORIZATION_TOKEN,
            scope="GIGACHAT_API_PERS",
            model="GigaChat",
            verify_ssl_certs=False
        )

    def get_topic(self, txt: str):
        if "да" in self.ask(
                f"этот текст содержит упоминания терроризма, порно или насилия? \"{txt}\". Ответь исключительно ОДНИМ словом: ДА или НЕТ"
        ).lower():
            raise exception("Опасный контент")

        return self.ask(
            f"скажи исключительно и только ОДНИМ СЛОВОМ тематику этого поста без лишних символов: \"{txt}\""
        )

    def ask(self, question: str):
        response = self.giga.chat(question)

        print(response.choices[0].message.content)
        return response.choices[0].message.content
