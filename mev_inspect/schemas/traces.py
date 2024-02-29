from enum import Enum
from typing import Any, Dict, List, Optional

from .utils import CamelModel

'''
- Explaination of Trace 


- How to extract Trace from Block data in ETH block-chain 

- Block Header:
    - Parent hash: Hash of the previous block, forming the chain.
    - Block number: Sequential block number within the Ethereum blockchain.
    - State root: Hash representing the state of the Ethereum system at the time of block creation.
    - Miner address: Address receiving the block reward.
    - Timestamp: Block creation time.
    - Difficulty: Level of computational difficulty for mining.
    - Gas limit: Maximum gas allowed for transactions in the block.
    - Gas used: Total gas consumed by transactions in the block.
    - Extra data: Optional data specific to the protocol.

    
- Block Body:
    - List of transactions included in the block.
        - Data Format within a Transaction

        - From address: Sender of the transaction.
        - To address: Recipient of the transaction (empty for contract creation).
        - Value (ETH): Amount of ETH transferred in the transaction (0 for contract calls).
        - Gas limit: Maximum gas allowed for transaction execution.
        - Gas price (ETH/gas): Price the sender is willing to pay per unit of gas.
        - Data: Optional data field containing the function call (for contract interactions) or creation code (for contract creation).


- Parsing transaction data using Smart-contract ABI


- Ref: https://gemini.google.com/app/c2987ada3ac1b7c8


'''


class TraceType(Enum):
    call = "call"
    create = "create"
    delegate_call = "delegateCall"
    reward = "reward"
    suicide = "suicide"


class Trace(CamelModel):
    '''
    Trace meaning as Transaction - in block 
    '''
    action: dict

    block_hash: str
    block_number: int
    result: Optional[dict]
    
    subtraces: int


    trace_address: List[int]


    transaction_hash: Optional[str]
    transaction_position: Optional[int]
    
    '''
    So trace-type as action correspondence to smart-contract basic action 
    - Call
    - Create 
    - Delegate-call
    - Reward 
    - Suicide 
    '''
    type: TraceType
    
    error: Optional[str]




class Classification(Enum):
    unknown = "unknown"
    swap = "swap"
    transfer = "transfer"
    liquidate = "liquidate"
    seize = "seize"
    punk_bid = "punk_bid"
    punk_accept_bid = "punk_accept_bid"
    nft_trade = "nft_trade"


class Protocol(Enum):
    uniswap_v2 = "uniswap_v2"
    uniswap_v3 = "uniswap_v3"
    sushiswap = "sushiswap"
    aave = "aave"
    weth = "weth"
    curve = "curve"
    zero_ex = "0x"
    balancer_v1 = "balancer_v1"
    compound_v2 = "compound_v2"
    cream = "cream"
    cryptopunks = "cryptopunks"
    bancor = "bancor"
    opensea = "opensea"


class ClassifiedTrace(Trace):
    classification: Classification

    to_address: Optional[str]
    from_address: Optional[str]
    
    gas: Optional[int]
    
    value: Optional[int]
    
    gas_used: Optional[int]
    
    transaction_hash: str
    transaction_position: int
    
    protocol: Optional[Protocol]
    
    function_name: Optional[str]
    function_signature: Optional[str]
    
    inputs: Optional[Dict[str, Any]]
    abi_name: Optional[str]

    class Config:
        validate_assignment = True
        json_encoders = {
            # a little lazy but fine for now
            # this is used for bytes value inputs
            bytes: lambda b: b.hex(),
        }


class CallTrace(ClassifiedTrace):
    to_address: str
    from_address: str


class DecodedCallTrace(CallTrace):
    inputs: Dict[str, Any]
    abi_name: str
    protocol: Optional[Protocol]
    gas: Optional[int]
    gas_used: Optional[int]
    function_name: str
    function_signature: str
