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


class Arbitrage(BaseModel):
    swaps: List[Swap]
    block_number: int
    transaction_hash: str
    account_address: str
    profit_token_address: str
    start_amount: int
    end_amount: int
    profit_amount: int
    error: Optional[str]


class Sandwich(BaseModel):
    block_number: int
    sandwicher_address: str
    frontrun_swap: Swap
    backrun_swap: Swap
    sandwiched_swaps: List[Swap]
    profit_token_address: str
    profit_amount: int