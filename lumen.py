""" Python API wrapper for the Lumen Database """
from urllib.parse import urlencode
import time
import requests
import logging

from requests import HTTPError


class Lumen():
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': "QUT_DMRC_LUMENAPI/0.2",
            'X-Authentication-Token': self.api_key,
            'Accept': 'application/json'
        }

    def search(self, params={}):
        """

        """

        delay = 20

        url= 'https://Lumendatabase.org/notices/search.json'

        # This should be handled by the header User-Agent
        #params['authentication_token'] = self.api_key

        if len(params) > 0:
            url = url + '?{}'.format(urlencode(params))

        while True:
            r = self.session.get(url=url)
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 429:
                # Hit rate limit. Pause and try again (with an exponential backoff)
                logging.error("Hit lumen rate limit. Sleeping {} seconds.".format(delay))
                time.sleep(delay)
                delay = delay * 2
            elif r.status_code == 422:
                # Lumen's most common error type.
                try:
                    error = "Lumen returned error 422 Unprocessable Entity. Details:\n{}".format(r.text)
                except:
                    error = "Lumen returned error 422 Unprocessable Entity. No details available."

                logging.exception(error)
                raise HTTPError(error)
            else:
                error = "Unknown error fetching lumen data. HTTP error received: {}".format(r.status_code)
                logging.exception(error)
                raise HTTPError(error)

    def get(self, notice_id):
        """ GET https://lumendatabase.org/notices/<notice id>.json """
        url = "https://lumendatabase.org/notices/{}.json".format(notice_id)
        r = self.session.get(url=url)
        if r.status_code == 200:
            json_results = r.json()
            return json_results.get('dmca')
        else:
            raise HTTPError("Unable to get notice. HTTP error received: {}".format(r.status_code))
