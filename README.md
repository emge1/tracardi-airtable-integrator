# Plugin documentation

Please provide documentation







"https://gist.github.com/KalebNyquist/4424fc1ef3dc6bb4fc0b5a7122ada4bc"
"biblioteka pandas"

In the requests function, the params keyword argument attaches parameters to the HTTP request using a Python dictionary in the form {parameter1 : value1, parameter2 : value2}.
In an Airtable’s API documentation, you can find a list of available parameters under “List Records” for any particular table. Most of these parameters will subset your data for you: for example, you could send {"maxRecords" : 50} if for some reason you only want to grab the first 50 records in that particular table. Other parameters, related to the format of the data, serve more technical purposes.


However, one special parameter to note is offset. This parameter will be discussed at the end of this tutorial, where we will cover how to download more than 100 records from a single table.


 Headers are used to pass a variety of additional information with an HTTP request, however, within the general Airtable API the only header that is used is the header Authorization which is used to authenticate a user-agent with the server by sending an API key.


To retrieve the API key associated with your account, head to airtable.com/account and click the lavender-colored box under “API”. This will reveal your personal API key which you can copy and paste. Consistent with the base and records ids discussed above, an API key is a 17-character string that begins with “key”. (To see the Airtable bases which you can access using your API key, head to airtable.com/api).





"# tracardi-airtable-integrator" 
