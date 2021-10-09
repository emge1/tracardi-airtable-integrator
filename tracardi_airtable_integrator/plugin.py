from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result

from tracardi_airtable_integrator.model.configuration import Configuration
import requests
from aiohttp import ClientConnectorError
import json


class AirTableIntegrator(ActionRunner):

    def __init__(self, **kwargs):
        self.config = Configuration(**kwargs)

    async def run(self, payload):
        try:
            if self.config.get_data is True and self.config.parse_data is True:
                raise ValueError("You can't get and parse data at the same time.")

            if self.config.get_data is True:
                if len(self.config.table_name) != 17:
                    raise ValueError("Base id length need to be equal to 17.")

                table_name = self.config.table_name.lower().replace(" ", "_")
                url = f"https://api.airtable.com/v0/{self.config.base_id}/{table_name}"

                if self.config.record_id is not None:
                    url = f"{url}/{self.config.record_id}"

                if len(self.config.api_key) != 17:
                    raise ValueError("Api key length need to be equal to 17.")

                headers = {"Authorization": "Bearer " + self.config.api_key}

                response = requests.get(url=url, params=self.config.params, headers=headers)
                response = response.json()

                return Result(port="payload", value=response)

            if self.config.parse_data is True:
                if len(self.config.table_name) != 17:
                    raise ValueError("Base id length need to be equal to 17.")

                table_name = self.config.table_name.lower().replace(" ", "_")
                url = f"https://api.airtable.com/v0/{self.config.base_id}/{table_name}"

                if self.config.record_id is not None:
                    url = f"{url}/{self.config.record_id}"

                if len(self.config.api_key) != 17:
                    raise ValueError("Api key length need to be equal to 17.")

                headers = {"Authorization": f"Bearer {self.config.api_key}",
                           "Content-Type": "application/json"}

                if self.config.record_id is None:  # posting data
                    upload_dict = {"records": [{"fields": self.config.upload_data}], "typecast": False}
                    upload_json = json.dumps(upload_dict)

                    response = requests.post(url=url, data=upload_json, headers=headers)
                    response = response.json()

                    return Result(port="payload", value=response)

                else:  # patching data
                    upload_dict = {"fields": self.config.upload_data, "typecast": True}
                    upload_json = json.dumps(upload_dict)

                    response = requests.patch(url=url, data=upload_json, headers=headers)
                    response = response.json()

                    return Result(port="payload", value=response)

        except ClientConnectorError as e:
            return Result(port="response", value=None), Result(port="error", value=str(e))


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_airtable_integrator.plugin',
            className='AirTableIntegrator',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Marcin Gaca",
            init={
                "get_data": False,
                "parse_data": False,
                "base_id": None,
                "table_name": None,
                "record_id": None,
                "params": None,
                "api_key": None,
                "upload_data": None,
            }
        ),
        metadata=MetaData(
            name='tracardi-airtable-integrator',
            desc='This plugin connects Tracardi to AirTable.',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )
