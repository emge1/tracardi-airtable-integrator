from pydantic import BaseModel
from typing import Optional


class Configuration(BaseModel):
    get_data: bool
    parse_data: bool

    base_id: str
    table_name: str
    record_id: Optional[str]
    params: Optional[dict]
    api_key: str
    upload_data: Optional[dict]
