from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from tracardi_airtable_integrator.plugin import AirTableIntegrator
import asyncio


async def main():
    init = {
        "get_data": True,
        "parse_data": False,
        "base_id": "your_base_id",
        "table_name": "Table 1",
        "record_id": 'your_record_id',
        "params": None,
        "api_key": "your_api_key",
        "upload_data": {'some': 'data'},
    }
    payload = {}
    plugin = AirTableIntegrator(**init)

    payload = {}

    results = await plugin.run(payload)
    print(results)


asyncio.run(main())