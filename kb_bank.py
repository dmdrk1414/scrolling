from simple_bank_korea.kb import get_transactions

# get_transactions returns list of dicts
# like this:
# [{'transaction_by': '', 'date': datetime.datetime(2017, 9, 11, 12, 39, 42), 'amount': 50, 'balance': 394}]

# example
transaction_list = get_transactions(
    bank_num='67070204117196',
    birthday='960415',
    password='1414',
    # days=30, # Optional, default is 30
    # PHANTOM_PATH='/Users/beomi/bin/phantomjs', # Optional, default is 'phantomjs' only.
    # LOG_PATH='/Users/beomi/phantom.log' # Optional, default is os.path.devnull (no log)
)

for trs in transaction_list:
    print(trs['date'], trs['amount'], trs['transaction_by'])
