''' Defining simple functions for calculating the arbitrage return including fees '''

def arbReturn(ZAR, EUR, BTCPrice):
    # Luno Fees
    luno_receive_fee = 0.0002 * BTCPrice
    zar_withdrawal_fee = 8.5

    # Bitstamp Fees
    trading_cost = 0.0025
    ccy_deposit_fee = 0.0005 * EUR

    # FNB Fees
    fx_commission = 0.0055 * ZAR
    swift_fee = 115
    bank_deferred_fx = 228

    # Calculate Total Bank Fee
    bank_fee = ZAR - fx_commission - bank_deferred_fx

    # Calculate Bitstamp Trade Fee
    bitstamp_fee = EUR - (EUR * trading_cost) - ccy_deposit_fee

    # Calculate Luno fee
    luno_fee = BTCPrice - luno_receive_fee

    # print(bank_fee)
    # print(bitstamp_fee)
    print(BTCPrice)
    # print(luno_fee)

ZAR = 100000
EUR = ZAR / 16.75
BTCPrice = 183000
BTC = ZAR / BTCPrice

arbReturn(ZAR, EUR, BTC)