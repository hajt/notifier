import requests
import json

from notifier.logger import log


class Slack():

    def __init__(self, webhook_url: str) -> None:
        """ Slack sender notifications class. """ 
        self.webhook_url = webhook_url
        self.headers = {'Content-Type': 'application/json'}

    
    def _to_json(self, text: str) -> str:
        """ Message text wrapper for request.post(data) argument. """
        return json.dumps({'text': text})


    def send_message(self, text: str) -> bool:
        """ Function which sends Slack message as HTTP POST request. """ 
        status = None
        log.info("Sending message...")
        response = requests.post(self.webhook_url, data=self._to_json(text), headers=self.headers)
        log.debug(f"Response code: {str(response.status_code)}")
        if response.status_code==200:
            log.info("Message succesfully sent!")
            status = True
        else:
            log.info("Message cannot be sent.")
            status = False
        return status


