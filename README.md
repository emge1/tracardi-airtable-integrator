# Tracardi plugin

This code can be run within Tracardi workflow.

# AirTable Connector Action

The purpose of this plugin is to connect with AirTable. You can get data or 
send data to the database.

# Configuration

This node requires configuration. 

To can get or parse data at the same time. To get data, set "get data" 
value as True and "parse_data" as False. To parse data, do it inversely.

You have to know your database id and table name. You can get the id from URL to your database.
It begins with "app". For example:

``` json
https://airtable.com/app11111111111111/tbl11111111111111/viw11111111111111?blocks=hide
```

In this case, database id is "app11111111111111".

Optionally, you can set id of record in your database. To get it, you need to press RMB and get 
URL address of the record. In the following case:

``` json
https://airtable.com/app11111111111111/tbl11111111111111/viw11111111111111?rec11111111111111?blocks=hide
```

In this situation, record id is "rec11111111111111"

In the requests function, the params keyword argument attaches parameters to the HTTP request using a Python 
dictionary in the form {"parameter1" : "value1", "parameter2" : "value2"}.

To retrieve the API key associated with your account, head to airtable.com/account and click the lavender-colored 
box under “API”. This will reveal your personal API key which you can copy and paste. Consistent with the base 
and records ids discussed above, an API key is a 17-character string that begins with “key”. 
(To see the Airtable bases which you can access using your API key, head to airtable.com/api).

To parse data, you need to define it in field "data". The format of data is dict: {"field": "some data"} where
"field" is field name in your database and "some data" - data you get.

Example #1 - get data:

```json
"init"={
        "get_data": True,
        "parse_data": False,
        "base_id": "app11111111111111",
        "table_name": "Table",
        "record_id": 'rec22222222222222',
        "params": None,
        "api_key": "key3333333333333",
        "upload_data": None,
    }
```

Example #2 - parsing data:

```json
"init"={
        "get_data": False,
        "parse_data": True,
        "base_id": "app11111111111111",
        "table_name": "Table",
        "record_id": None,
        "params": None,
        "api_key": "key3333333333333",
        "upload_data": {"some": "data"},
    }
```

# Input payload

This node does not process input payload.

# Output

This node return output to client only if the client got some data.