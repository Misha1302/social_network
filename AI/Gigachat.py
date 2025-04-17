from queue import PriorityQueue

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
        response = self.giga.chat(
            f"СКАЖИ ИСКЛЮЧИТЕЛЬНО ОДНИМ СЛОВОМ ТЕМАТИКУ ЭТОГО ПОСТА БЕЗ ЛИШНИХ СИМВОЛОВ: \"{txt}\"")

        print(response.choices[0].message.content)
        return response.choices[0].message.content
