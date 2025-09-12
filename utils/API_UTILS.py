import json
from pathlib import Path

import requests
from requests.auth import HTTPBasicAuth


class API_UTILS:
    def create_voip_quote(self):
        current_file = Path(__file__).resolve()
        parent2 = current_file.parent.parent
        voip_create_quote_json = parent2 / "data" / "t1_install_quote_generation.json"

        with open(voip_create_quote_json,"r") as f:
            payload = json.load(f)

        url = "https://brightspeedtsmuat.service-now.com/api/sn_ind_tmt_orm/opportunity/createquote"
        username = "snow_user"
        password = "W.HVwcPFk2CFZ[CB2^AQH6N&ToXx[+^P0zby=?+}sZG7G%-0lmGf=t+hz3Y@;kfk9FuN_1D9-@5}K+QcM4_?$P(LkFCGPfp$Y6)s"

        headers= {"Content-Type": "application/json", "Accept": "application/json"}

        response = requests.post(url, json=payload, auth=HTTPBasicAuth(username,password), headers=headers)
        try:
            response_data = response.json()
            print(f"Parsed response data: {response_data}")
        except requests.exceptions.JSONDecodeError:
            print("Response is not a valid json")
            return

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        result = response_data.get("result")

        if result:
            quote_number = result.get("quote_number")
            quote_url = result.get("url")

            print("Result:", result)
            print("Quote number:", quote_number)
            print("Quote url:", quote_url)

            if quote_number and quote_url:
                print(f"Created quote number is {quote_number} and its URL is {quote_url}", flush=True)
                return quote_url
            else:
                print("'quote_number' or 'url' missing in result.")
                return
        else:
            print("'result' key is not found in the response.")
            return
