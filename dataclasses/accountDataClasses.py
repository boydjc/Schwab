from dataclasses import dataclass
from enum import Enum


""""
TODOS (Also go through and set which variables are optional and which are not)
===============
TransactionInstrument
CollectiveInvestment
TransactionEquity
TransactionFixedIncome
Future
Index
TransactionMutualFund
TransactionOption
Product
TransactionAPIOptionDeliverable
APIOrderStatus
TransactionType
Transaction
UserDetails
TransferItem
UserPreference
UserPreferenceAccount
StreamerInfo
Offer
"""

@dataclass
class AccountNumberHash():
    accountNumber: str
    hashValue: str

@dataclass
class OrderBalance():
    orderValue: float
    projectedAvailableFund: float
    projectedBuyingPower: float
    projectedCommission: float

@dataclass
class OrderLeg():
    askPrice: float
    bidPrice: float
    lastPrice: float
    markPrice: float
    projectedCommission: float
    quantity: float
    finalSymbol: str
    legId: int
    assetType: AssetType
    instruction: Instruction

@dataclass
class OrderStrategy():
    accountNumber: str
    advancedOrderType: AdvancedOrderType
    closeTime: str
    enteredTime: str
    orderBalance: OrderBalance
    orderStrategyType: OrderStrategyType
    orderVersion: int
    session: Session
    status: Status
    allOrNone: bool
    discretionary: bool
    duration: Duration
    filledQuantity: float
    orderType: OrderType
    orderValue: float
    price: float
    quantity: float
    remainingQuantity: float
    sellNonMarginableFirst: bool
    settlementInstruction: SettlementInstruction
    strategy: ComplexOrderStrategyType
    amountIndicator: AmountIndicator
    orderLegs: list[OrderLeg]

@dataclass
class OrderValidationDetail():
    validationRuleName: str
    message: str
    activityMessage: str
    originalSeverity: APIRuleAction
    overrideName: str
    overrideSeverity: APIRuleAction

@dataclass
class OrderValidationResult():
    alerts: list[OrderValidationDetail]
    accepts: list[OrderValidationDetail]
    rejects: list[OrderValidationDetail]
    reviews: list[OrderValidationDetail]
    warns: list[OrderValidationDetail]

@dataclass
class FeeValue():
    value: float
    type: FeeType

@dataclass
class FeeLeg():
    feeValues: list[FeeValue]

@dataclass
class Fees():
    feeLegs: list[FeeValue]

@dataclass
class CommissionValue():
    value: float
    type: FeeType

@dataclass
class CommissionLeg():
    commissionValues: list[CommissionValue]

@dataclass
class Commission():
    commissionLegs: list[CommissionLeg]

@dataclass
class CommissionAndFee():
    commission: Commission
    fee: Fees
    trueCommission: Commission

@dataclass
class AccountCashEquivalent():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float
    type: AccountCashEquivalentType

@dataclass
class AccountEquity():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: str
    netChange: float

@dataclass
class AccountFixedIncome():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float
    maturityDate: str
    factor: float
    variableRate: float

@dataclass
class AccountMutualFund():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float

@dataclass
class AccountAPIOptionDeliverable():
    symbol: str
    deliverableUnits: float
    apiCurrencyType: APICurrencyType
    assetType: AssetType

@dataclass
class AccountOption():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float
    optionDeliverables: list[AccountAPIOptionDeliverable]
    putCall: PutCall
    optionMultiplier: int
    type: AccountOptionType
    underlyingSymbol: str

@dataclass
class AccountsInstrument():
    accountCashEquivalent: AccountCashEquivalent
    accountEquity: AccountEquity
    accountFixedIncome: AccountFixedIncome
    accountOption: AccountOption

@dataclass
class Position():
    shortQuantity: float
    averagePrice: float
    currentDayProfitLoss: float
    currentDayProfitLossPercentage: float
    longQuantity: float
    settledLongQuantity: float
    settledShortQuantity: float
    agedQuantity: float
    instrument: AccountsInstrument
    marketValue: float
    maintenanceRequirement: float
    averageLongPrice: float
    averageShortPrice: float
    taxLotAverageLongPrice: float
    taxLotAverageShortPrice: float
    longOpenProfitLoss: float
    shortOpenProfitLoss: float
    previousSessionLongQuantity: float
    previousSessionShortQuantity: float
    currentDayCost: float
    
@dataclass 
class CashAccount():
    type: CashAccountType
    accountNumber: str
    roundTrips: int
    isDayTrader: bool
    isClosingOnlyRestricted: bool
    pfcbFlag: bool
    positions: list[Position]
    initialBalances: CashInitialBalance
    currentBalances: CashBalance
    projectedBalances: CashBalance

@dataclass
class CashInitialBalance():
    accruedInterest: float
    cashAvaiableForTrading: float
    cashAvaiableForWithdrawal: float
    cashBalance: float
    bondValue: float
    cashReceipts: float
    liquidationValue: float
    longOptionMarketValue: float
    longStockValue: float
    moneyMarketFund: float
    mutualFundValue: float
    shortOptionMarketValue: float
    shortStockValue: float
    isInCall: float
    unsettledCash: float
    cashDebtCallValue: float
    pendingDeposits: float
    accountValue: float

@dataclass
class CashBalance():
    cashAvaiableForTrading: float
    cashAvaiableForWithdrawal: float
    cashCall: float
    longNonMarginableMarketValue: float
    totalCash: float
    cashDebitCallValue: float
    unsettledCash: float

@dataclass
class MarginInitialBalance():
    accruedInterest: float
    avaiableFundsNonMarginableTrade: float
    bondValue: float
    buyingPower: float
    cashBalance: float
    cashAvaiableForTrading: float
    cashReceipts: float
    dayTradingBuyingPower: float
    dayTradingBuyingPowerCall: float
    dayTradingEquityCall: float
    equity: float
    equityPercentage: float
    liquidationValue: float
    longMarginValue: float
    longOptionMarketValue: float
    longStockValue: float
    maintenanceCall: float
    maintenanceRequirement: float
    margin: float
    marginEquity: float
    moneyMarketFund: float
    mutualFundValue: float
    regTCall: float
    shortMarginValue: float
    shortOptionMarketValue: float
    shortStockValue: float
    totalCash: float
    isInCall: float
    unsettledCash: float
    pendingDeposits: float
    marginBalance: float
    shortBalance: float
    accountValue: float

@dataclass
class MarginBalance():
    avaiableFunds: float
    avaiableFundsNonMarginableTrade: float
    buyingPower: float
    buyingPowerNonMarginableTrade: float
    dayTradingBuyingPower: float
    dayTradingBuyingPowerCall: float
    equity: float
    equityPercentage: float
    longMarginValue: float
    maintenanceCall: float
    maintenanceRequirement: float
    marginBalance: float
    regTCall: float
    shortBalance: float
    shortMarginValue: float
    sma: float
    isInCall: float
    stockBuyingPower: float
    optionBuyingPower: float

@dataclass
class MarginAccount():
    type: MarginAccountType
    accountNumber: str
    roundTrips: int
    isDayTrader: bool
    isClosingOnlyRestricted: bool
    pfcbFlag: bool
    positions: list[Position]
    initialBalances: MarginInitialBalance
    currentBalance: MarginBalance
    projectedBalance: MarginBalance

@dataclass
class SecuritiesAccount():
    marginAccount: MarginAccount
    cashAccount: CashAccount

@dataclass
class Account():
    securitiesAccount: SecuritiesAccount

@dataclass
class DateParam():
    date: str # format is yyyy-MM-dd'T'HH:mm:ss.SSZ

@dataclass
class Order():
    session: Session
    duration: Duration
    orderType: OrderType
    cancelTime: str
    complexOrderStrategyType: ComplexOrderStrategyType
    quantity: float
    filledQuantity: float
    remainingQuantity: float
    requestedDestination: RequestedDestination
    releaseTime: str
    stopPrice: float
    stopPriceLinkBasis: StopPriceLinkBasis
    stopPriceLinkType: StopPriceLinkType
    stopPriceOffset: float
    stopType: StopType
    priceLinkBasis: PriceLinkBasis
    priceLinkType: PriceLinkType
    price: float
    taxLotMethod: TaxLotMethod
    orderLegCollection: list[OrderLegCollection]
    activationPrice: float
    specialInstruction: SpecialInstruction
    orderStrategyType: OrderStrategyType
    orderId: int
    cancelable: bool
    editable: bool
    status: Status
    enteredTime: str
    closeTime: str
    tag: str
    accountNumber: int
    orderActivityCollection: list[OrderActivity]
    replacingOrderCollection: list[Order]
    childOrderStrategies: list[Order]
    statusDescription: str
    
@dataclass
class ExecutionLeg():
    legId: int
    price: float
    quantity: float
    mismarkedQuantity: float
    instrumentId: int
    time: str

@dataclass
class OrderActivity():
    activityType: ActivityType
    executionType: ExecutionType
    quantity: float
    orderRemainingQuantity: float
    executionLegs: list[ExecutionLeg]

@dataclass
class OrderRequest():
    session: Session
    duration: Duration
    orderType: OrderTypeRequest
    cancelTime: str
    complexOrderStrategyType: ComplexOrderStrategyType
    quantity: float
    filledQuantity: float
    remainingQuantity: float
    destinationLinkName: str
    releaseTime: str
    stopPrice: float
    stopPriceLinkBasis: StopPriceLinkBasis
    stopPriceLinkType: StopPriceLinkType
    stopPriceOffset: float
    stopType: StopType
    priceLinkBasis: PriceLinkBasis
    priceLinkType: PriceLinkType
    price: float
    taxLotMethod: TaxLotMethod
    orderLegCollection: list[OrderLegCollection]
    activationPrice: float
    specialInstruction: SpecialInstruction
    orderStrategyType: OrderStrategyType
    orderId: int
    cancelable: bool
    editable: bool
    status: Status
    enteredTime: str
    closeTime: str
    accountNumber: int
    orderActivityCollection: list[OrderActivity]
    replacingOrderCollection: list[OrderStrategy]
    childOrderStrategies: list[OrderStrategy]
    statusDescription: str

@dataclass
class PreviewOrder():
    orderId: int
    orderStrategy: OrderStrategy
    orderValidationResult: OrderValidationResult
    commissionAndFee: CommissionAndFee

@dataclass
class OrderLegCollection():
    orderLegType: OrderLegType
    legId: int
    instrument: AccountsInstrument
    instruction: Instruction
    positionEffect: PositionEffect
    quantity: float
    quantityType: QuantityType
    divCapGains: DivCapGains
    toSymbol: str

@dataclass
class SecuritiesAccountBase():
    type: SecuritiesAccountBaseType
    accountNumber: str
    roundTrips: int
    isDayTrader: bool
    isClosingOnlyRestricted: bool
    pfcbFlag: bool
    position: list[Position]

@dataclass
class TransactionBaseInstrument():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float

@dataclass
class AccountsBaseInstrument():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float

@dataclass
class Currency():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float

@dataclass
class Forex():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float
    type: ForexType
    baseCurrency: Currency
    counterCurrency: Currency

@dataclass
class Future():
    activeContract: bool
    type: FutureType
    expirationDate: str
    lastTradingDate: str
    firstNoticeDate: str
    multipler: float
    transactionCashEquivalent: TransactionCashEquivalent
    collectiveInvestment

@dataclass
class TransactionCashEquivalent():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netchange: float
    type: TransactionCashEquivalentType
    





##################################
#            Enums               #
##################################
class Session(str, Enum):
    NORMAL = "NORMAL"
    AM = "AM"
    PM = "PM"
    SEAMLESS = "SEAMLESS"

class Duration(str, Enum):
    DAY = "DAY"
    GOOD_TILL_CANCEL = "GOOD_TILL_CANCEL"
    FILL_OR_KILL = "FILL_OR_KILL"
    IMMEDIATE_OR_CANCEL = "IMMEDIATE_OR_CANCEL"
    END_OF_WEEK = "END_OF_WEEK"
    END_OF_MONTH = "END_OF_MONTH"
    NEXT_END_OF_MONTH = "NEXT_END_OF_MONTH"
    UNKNOWN = "UNKNOWN"

class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"
    TRAILING_STOP = "TRAILING_STOP"
    CABINET = "CABINET"
    NON_MARKETABLE = "NON_MARKETABLE"
    MARKET_ON_CLOSE = "MARKET_ON_CLOSE"
    EXERCISE = "EXERCISE"
    TRAILING_STOP_LIMIT = "TRAILING_STOP_LIMIT"
    NET_DEBT = "NET_DEBT"
    NET_CREDIT = "NET_CREDIT"
    NET_ZERO = "NET_ZERO"
    LIMIT_ON_CLOSE = "LIMIT_ON_CLOSE"
    UNKNOWN = "UNKNOWN"

# Same as OrderType, but does not have UNKNOWN since this type is 
# not allowed as an input
class OrderTypeRequest(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"
    STOP = "STOP"
    STOP_LIMIT = "STOP_LIMIT"
    TRAILING_STOP = "TRAILING_STOP"
    CABINET = "CABINET"
    NON_MARKETABLE = "NON_MARKETABLE"
    MARKET_ON_CLOSE = "MARKET_ON_CLOSE"
    EXERCISE = "EXERCISE"
    TRAILING_STOP_LIMIT = "TRAILING_STOP_LIMIT"
    NET_DEBT = "NET_DEBT"
    NET_CREDIT = "NET_CREDIT"
    NET_ZERO = "NET_ZERO"
    LIMIT_ON_CLOSE = "LIMIT_ON_CLOSE"

class ComplexOrderStrategyType(str, Enum):
    NONE = "NONE"
    COVERED = "COVERED"
    VERTICAL = "VERTICAL"
    BACK_RATIO = "BACK_RATIO"
    CALENDAR = "CALENDAR"
    DIAGONAL = "DIAGONAL"
    STRADDLE = "STRADDLE"
    STRANGLE = "STRANGLE"
    COLLAR_SYNTHETIC = "COLLAR_SYNTETHIC"
    BUTTERFLY = "BUTTERFLY"
    CONDOR = "CONDOR"
    IRON_CONDOR = "IRON_CONDOR"
    VERTICAL_ROLL = "VERTICAL_ROLL"
    COLLAR_WITH_STOCK = "COLLAR_WITH_STOCK"
    DOUBLE_DIAGONAL = "DOUBLE_DIAGONAL"
    UNBALANCED_BUTTERFLY = "UNBALANCE_BUTTERFLY"
    UNBALANCED_CONDOR = "UNBALANCED_CONDOR"
    UNBALANCED_IRON_CONDOR = "UNBALANCE_IRON_CONDOR"
    UNBALANCED_VERTICAL_ROLL = "UNBALANCED_VERTICAL_ROLL"
    MUTUAL_FUND_SWAP = "MUTUAL_FUND_SWAP"
    CUSTOM = "CUSTOM"

class RequestedDestination(str, Enum):
    INET = "INET"
    ECN_ARCA = "ECN_ARCA"
    CBOE = "CBOE"
    AMEX = "AMEX"
    PHLX = "PHLX"
    ISE = "ISE"
    BOX = "BOX"
    NYSE = "NYSE"
    NASDAQ = "NASDAQ"
    BATS = "BATS"
    C2 = "C2"
    AUTO = "AUTO"

class StopPriceLinkBasis(str, Enum):
    MANUAL = "MANUAL"
    BASE = "BASE"
    TRIGGER = "TRIGGER"
    LAST = "LAST"
    BID = "BID"
    ASK = "ASK"
    ASK_BID = "ASK_BID"
    MARK = "MARK"
    AVERAGE = "AVERAGE"

class StopPriceLinkType(str, Enum):
    VALUE = "VALUE"
    PERCENT = "PERCENT"
    TICK = "TICK"

class StopType(str, Enum):
    STANDARD = "STANDARD"
    BID = "BID"
    ASK = "ASK"
    LAST = "LAST"
    MARK = "MARK"

class PriceLinkBasis(str, Enum):
    MANUAL = "MANUAL"
    BASE = "BASE"
    TRIGGER = "TRIGGER"
    LAST = "LAST"
    BID = "BID"
    ASK = "ASK"
    ASK_BID = "ASK_BID"
    MARK = "MARK"
    AVERAGE = "AVERAGE"

class PriceLinkType(str, Enum):
    VALUE = "VALUE"
    PERCENT = "PERCENT"
    TICK = "TICK"

class TaxLotMethod(str, Enum):
    FIFO = "FIFO"
    LIFO = "LIFO"
    HIGH_COST = "HIGH_COST"
    LOW_COST = "LOW_COST"
    AVERAGE_COST = "AVERAGE_COST"
    SPECIFIC_LOT = "SPECIFIC_LOT"
    LOSS_HARVESTER = "LOSS_HARVESTER"

class SpecialInstruction(str, Enum):
    ALL_OR_NONE = "ALL_OR_NONE"
    DO_NOT_REDUCE = "DO_NOT_REDUCE"
    ALL_OR_NONE_DO_NOT_REDUCE = "ALL_OR_NONE_DO_NOT_REDUCE"

class OrderStrategyType(str, Enum):
    SINGLE = "SINGLE"
    CANCEL = "CANCEL"
    RECALL = "RECALL"
    PAIR = "PAIR"
    FLATTEN = "FLATTEN"
    TWO_DAY_SWAP = "TWO_DAY_SWAP"
    BLAST_ALL = "BLAST_ALL"
    OCO = "OCO"
    TRIGGER = "TRIGGER"

class Status(str, Enum):
    AWAITING_PARENT_ORDER = "AWAITING_PARENT_ORDER"
    AWAITING_CONDITION = "AWAITING_CONDITION"
    AWAITING_STOP_CONDITION = "AWAITING_STOP_CONDITION"
    AWAITING_MANUAL_REVIEW = "AWAITING_MANUAL_REVIEW"
    ACCEPTED = "ACCEPTED"
    AWAITING_UR_OUT = "AWAITING_UR_OUT"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"
    QUEUED = "QUEUED"
    WORKING = "WORKING"
    REJECTED = "REJECTED"
    PENDING_CANCEL = "PENDING_CANCEL"
    CANCELED = "CANCELED"
    PENDING_REPLACE = "PENDING_REPLACE"
    REPLACED = "REPLACED"
    FILLED = "FILLED"
    EXPIRED = "EXPIRED"
    NEW = "NEW"
    AWAITING_RELEASE_TIME = "AWAITING_RELEASE_TIME"
    PENDING_ACKNOWLEDGEMENT = "PENDING_ACKNOWLEDGEMENT"
    PENDING_RECALL = "PENDING_RECALL"
    UNKNOWN = "UNKNOWN"

class AmountIndicator(str, Enum):
    DOLLARS = "DOLLARS"
    SHARES = "SHARES"
    ALL_SHARES = "ALL_SHARES"
    PERCENTAGE = "PERCENTAGE"
    UNKNOWN = "UNKNOWN"

class SettlementInstruction(str, Enum):
    REGULAR = "REGULAR"
    CASH = "CASH"
    NEXT_DAY = "NEXT_DAY"
    UNKNOWN = "UNKNOWN"

class AdvancedOrderType(str, Enum):
    NONE = "NONE"
    OTO = "OTO"
    OCO = "OCO"
    OTOCO = "OTOCO"
    OT2OCO = "OT2OCO"
    OT3OCO = "OT3OCO"
    BLAST_ALL = "BLAST_ALL"
    OTA = "OTA"
    PAIR = "PAIR"

class AssetType(str, Enum):
    EQUITY = "EQUITY"
    MUTUAL_FUND = "MUTUAL_FUND"
    OPTION = "OPTION"
    FUTURE = "FUTURE"
    FOREX = "FOREX"
    INDEX = "INDEX"
    CASH_EQUIVALENT = "CASH_EQUIVALENT"
    FIXED_INCOME = "FIXED_INCOME"
    PRODUCT = "PRODUCT"
    CURRENCY = "CURRENCY"
    COLLECTIVE_INVESTMENT = "COLLECTIVE_INVESTMENT"    

class Instruction(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    BUY_TO_COVER = "BUY_TO_COVER"
    SELL_SHORT = "SELL_SHORT"
    BUY_TO_OPEN = "BUY_TO_OPEN"
    BUY_TO_CLOSE = "BUY_TO_CLOSE"
    SELL_TO_OPEN = "SELL_TO_OPEN"
    SELL_TO_CLOSE = "SELL_TO_CLOSE"
    EXCHANGE = "EXCHANGE"
    SELL_SHORT_EXEMPT = "SELL_SHORT_EXEMPT"

class APIRuleAction(str, Enum):
    ACCEPT = "ACCEPT"
    ALERT = "ALERT"
    REJECT = "REJECT"
    REVIEW = "REVIEW"
    UNKNOWN = "UNKOWN"

class FeeType(str, Enum):
    COMMISSION = "COMMISSION"
    SEC_FEE = "SEC_FEE" 
    STR_FEE = "STR_FEE"
    R_FEE = "R_FEE"
    CDSC_FEE = "CDSC_FEE" 
    OPT_REG_FEE = "OPT_REG_FEE"
    ADDITIONAL_FEE = "ADDITIONAL_FEE"
    MISCELLANEOUS_FEE = "MISCELLANEOUS_FEE" 
    FTT = "FTT"
    FUTURES_CLEARING_FEE = "FUTURES_CLEARING_FEE"
    FUTURES_DESK_OFFICE_FEE = "FUTURES_DESK_OFFICE_FEE"
    FUTURES_EXCHANGE_FEE = "FUTURES_EXCHANGE_FEE" 
    FUTURES_GLOBEX_FEE = "FUTURES_GLOBEX_FEE"
    FUTURES_NFA_FEE = "FUTURES_NFA_FEE" 
    FUTURES_PIT_BROKERAGE_FEE = "FUTURES_PIT_BROKERAGE_FEE"
    FUTURES_TRANSACTION_FEE = "FUTURES_TRANSACTION_FEE"
    LOW_PROCEEDS_COMMISSION = "LOW_PROCEEDS_COMMISSION"
    BASE_CHARGE = "BASE_CHARGE"
    GENERAL_CHARGE = "GENERAL_CHARGE"
    GST_FEE = "GST_FEE"
    TAF_FEE = "TAF_FEE"
    INDEX_OPTION_FEE = "INDEX_OPTION_FEE"
    TEFRA_TAX = "TEFRA_TAX"
    STATE_TAX = "STATE_TAX"
    UNKNOWN = "UNKNOWN"

class MarginAccountType(str, Enum):
    CASH = "CASH"
    MARGIN = "MARGIN"

class CashAccountType(str, Enum):
    CASH = "CASH"
    MARGIN = "MARGIN"

class AccountCashEquivalentType(str, Enum):
    SWEEP_VEHICLE = "SWEEP_VEHICLE"
    SAVINGS = "SAVINGS"
    MONEY_MARKET_FUND = "MONEY_MARKET_FUND"
    UNKNOWN = "UNKNOWN"

class AccountOptionType(str, Enum):
    VANILLA = "VANILLA"
    BINARY = "BINARY"
    BARRIER = "BARRIER"
    UNKNOWN = "UNKNOWN"

class APICurrencyType(str, Enum):
    USD = "USD"
    CAD = "CAD"
    EUR = "EUR"
    JPY = "JPY"

class PutCall(str, Enum):
    PUT = "PUT"
    CALL = "CALL"
    UNKNOWN = "UNKNOWN"

class ExecutionType(str, Enum):
    FILL = "FILL"

class ActivityType(str, Enum):
    EXECUTION = "EXECUTION"
    ORDER_ACTION = "ORDER_ACTION"

class OrderLegType(str, Enum):
    EQUITY = "EQUITY"
    OPTION = "OPTION"
    INDEX = "INDEX"
    MUTUAL_FUND = "MUTUAL_FUND"
    CASH_EQUIVALENT = "CASH_EQUIVALENT"
    FIXED_INCOME = "FIXED_INCOME"
    CURRENCY = "CURRENCY"
    COLLECTIVE_INVESTMENT = "COLLECTIVE_INVESTMENT"

class PositionEffect(str, Enum):
    OPENING = "OPENING"
    CLOSING = "CLOSING"
    AUTOMATIC = "AUTOMATIC"

class QuantityType(str, Enum):
    ALL_SHARES = "ALL_SHARES"
    DOLLARS = "DOLLARS"
    SHARES = "SHARES"

class DivCapGains(str, Enum):
    REINVEST = "REINVEST"
    PAYOUT = "PAYOUT"

class SecuritiesAccountBaseType(str, Enum):
    CASH = "CASH"
    MARGIN = "MARGIN"

class ForexType(str, Enum):
    STANDARD = "STANDARD"
    NBBO = "NBBO"
    UNKNOWN = "UNKNOWN"

class FutureType(str, Enum):
    STANDARD = "STANDARD"
    UNKNOWN = "UNKNOWN"

class TransactionCashEquivalentType(str, Enum):
    SWEEP_VEHICLE = "SWEEP_VEHICLE"
    SAVINGS = "SAVINGS"
    MONEY_MARKET_FUND = "MONEY_MARKET_FUND"
    UNKNOWN = "UNKNOWN"
