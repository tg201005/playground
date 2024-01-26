from rest_framework.views import APIView
from rest_framework.response import Response

from .blockchain.transact import (
    # compile_contract,
    abi,
    tx_receipt,
    retrieve_transaction,
    record_transaction,
)

import os
from dotenv import load_dotenv
from web3 import Web3


class TournamentLogView(APIView):
    def get(self, request, format=None):
        # num은 URL에서 전달받은 숫자입니다.
        # 이곳에서 num을 이용하여 필요한 처리를 수행하세요.
        # 예를 들어, num을 그대로 응답에 포함시킬 수 있습니다.

        return Response(retrieve_transaction(tx_receipt, abi))

    def post(self, request, format=None):
        # num은 POST body에서 전달받은 숫자입니다.
        # 이곳에서 num을 이용하여 필요한 처리를 수행하세요.
        # 예를 들어, num을 그대로 응답에 포함시킬 수 있습니다.
        tournament = []
        record_transaction(tx_receipt, abi, num)
        return Response({"num": num})
