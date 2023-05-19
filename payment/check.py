from requests import get


def check_trx(trx):

    data = get(f"https://chain.api.btc.com/v3/tx/{trx}?verbose=3").json()

    if data["data"] is None:

        return -1

    else:

        return data["data"]["confirmations"]

