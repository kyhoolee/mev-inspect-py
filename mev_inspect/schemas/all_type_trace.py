from typing import List, Optional

from pydantic import BaseModel

from mev_inspect.schemas.traces import Protocol


class Liquidation(BaseModel):
    liquidated_user: str
    liquidator_user: str
    debt_token_address: str
    debt_purchase_amount: int
    received_amount: int
    received_token_address: Optional[str]
    protocol: Protocol
    transaction_hash: str
    trace_address: List[int]
    block_number: str
    error: Optional[str]


class MinerPayment(BaseModel):
    block_number: int
    transaction_hash: str
    transaction_index: int
    miner_address: str
    coinbase_transfer: int
    base_fee_per_gas: int
    gas_price: int
    gas_price_with_coinbase_transfer: int
    gas_used: int
    transaction_to_address: Optional[str]
    transaction_from_address: Optional[str]


class NftTrade(BaseModel):
    abi_name: str
    transaction_hash: str
    transaction_position: int
    block_number: int
    trace_address: List[int]
    protocol: Optional[Protocol]
    error: Optional[str]
    seller_address: str
    buyer_address: str
    payment_token_address: str
    payment_amount: int
    collection_address: str
    token_id: int


### Need to understanding the mechanism of ERC-21 -> to create a new token based on ETH
### Token type - how does the rule of token - supply, transfer, balanceOf, ... 
class Price(BaseModel):
    token_address: str
    usd_price: float
    timestamp: datetime

    @validator("token_address")
    def lower_token_address(cls, v: str) -> str:
        return v.lower()



class PunkBidAcceptance(BaseModel):
    block_number: int
    transaction_hash: str
    trace_address: List[int]
    from_address: str
    punk_index: int
    min_price: int



class PunkBid(BaseModel):
    block_number: int
    transaction_hash: str
    trace_address: List[int]
    from_address: str
    punk_index: int
    price: int




class PunkSnipe(BaseModel):
    block_number: int
    transaction_hash: str
    trace_address: List[int]
    from_address: str
    punk_index: int
    min_acceptance_price: int
    acceptance_price: int




class Receipt(CamelModel):
    block_number: int
    transaction_hash: str
    transaction_index: int
    gas_used: int
    effective_gas_price: int
    cumulative_gas_used: int
    to: Optional[str]

    @validator(
        "block_number",
        "transaction_index",
        "gas_used",
        "effective_gas_price",
        "cumulative_gas_used",
        pre=True,
    )
    def maybe_hex_to_int(cls, v):
        if isinstance(v, str):
            return hex_to_int(v)
        return v



class Swap(BaseModel):
    abi_name: str
    transaction_hash: str
    transaction_position: int
    block_number: int
    trace_address: List[int]
    contract_address: str
    from_address: str
    to_address: str
    token_in_address: str
    token_in_amount: int
    token_out_address: str
    token_out_amount: int
    protocol: Protocol
    error: Optional[str]



class Transfer(BaseModel):
    block_number: int
    transaction_hash: str
    trace_address: List[int]
    from_address: str
    to_address: str
    amount: int
    token_address: str
