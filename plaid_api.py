import plaid
from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest

# Available environments are
# 'Production'
# 'Sandbox'

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)



#example of requesting transition data. 
request = TransactionsSyncRequest(
    access_token=access_token,
)
response = client.transactions_sync(request)
transactions = response['added']

# the transactions in the response are paginated, so make multiple calls while incrementing the cursor to
# retrieve all transactions
while (response['has_more']):
    request = TransactionsSyncRequest(
        access_token=access_token,
        cursor=response['next_cursor']
    )
    response = client.transactions_sync(request)
    transactions += response['added']