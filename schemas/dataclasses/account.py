from dataclasses import dataclass

from enums.account import *

""""
TODO: go through and set which variables are optional and which are not)
===============
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
    collectiveInvestment: CollectiveInvestment
    currency: Currency
    transactionEquity: TransactionEquity
    transactionFixedIncome: TransactionFixedIncome
    forex: Forex
    index: Index
    transactionMutualFund: TransactionMutualFund
    transactionOption: TransactionOption
    product: Product

@dataclass
class TransactionCashEquivalent():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netchange: float
    type: TransactionCashEquivalentType

@dataclass
class CollectiveInvestment():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange = float
    type: CollectiveInvestmentType

@dataclass
class TransactionInstrument():
    transactionCashEquivalent: TransactionCashEquivalent
    collectiveInvestment: CollectiveInvestment
    currency: Currency
    transactionEquity: TransactionEquity
    tansactionFixedIncome: TransactionFixedIncome
    forex: Forex
    future: Future
    index: Index
    transactionMutualFund: TransactionMutualFund
    transactionOption: TransactionOption
    product: Product

@dataclass
class TransactionEquity():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float
    type: TransactionEquityType

@dataclass
class TransactionFixedIncome():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float
    type: TransactionFixedIncomeType
    maturityDate: str
    factor: float
    multiplier: float
    variableRate: float

@dataclass
class TransactionMutualFund():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float
    fundFamilyName: str
    fundFamilySymbol: str
    fundGroup: str
    type: TransactionMutualFundType
    exchangeCutoffTime: str
    purchaseCutoffTime: str
    redemptionCutoffTime: str
    
@dataclass
class TransactionAPIOptionDeliverable():
    rootSymbol: str
    strikePercent: int
    deliverableNumber: int
    deliverableUnits: float
    deliverable: TransactionInstrument
    assetType: AssetType

@dataclass 
class Product():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float
    type: ProductType

@dataclass
class Index():
    activeContract: bool
    type: IndexType
    transactionCashEquivalent: TransactionCashEquivalent
    collectiveInvestment: CollectiveInvestment
    currency: Currency
    transactionEquity: TransactionEquity
    transactionFixedIncome: TransactionFixedIncome
    forex: Forex
    future: Future
    transactionMutualFund: TransactionMutualFund
    transactionOption: TransactionOption
    product: Product

@dataclass
class TransactionOption():
    assetType: AssetType
    cusip: str
    symbol: str
    description: str
    instrumentId: int
    netChange: float
    expirationDate: str
    optionDeliverables: list[TransactionAPIOptionDeliverable]
    optionPremiumMulitpler: int
    putCall: PutCall
    strikePrice: float
    type: TransactionOptionType
    underlyingSymbol: str
    underlyingCusip: str
    deliverable: TransactionInstrument

@dataclass
class UserDetails():
    cdDomainId: str
    login: str
    type: UserDetailsType
    userId: int
    systemUserName: str
    firstName: str
    lastName: str
    brokerRepCode: str

@dataclass
class TransferItem():
    instrument: TransactionInstrument
    amount: float
    cost: float
    price: float
    feeType: FeeType
    positionEffect: PositionEffect

@dataclass
class Transaction():
    activityId: int
    time: str
    user: UserDetails
    description: str
    accountNumber: str
    type: TransactionType
    status: Status
    subAccount: SubAccount
    tradeDate: str
    settlementDate: str
    positionId: int
    orderId: int
    netAmount: float
    activityType: ActivityType
    transferItems: list[TransferItem]

@dataclass
class Offer():
    level2Permissions: bool
    mktDataPermission: str

@dataclass
class StreamerInfo():
    streamerSocketUrl: str
    schwabClientCustomerId: str
    schwabClientCorrelId: str
    schwabClientChannel: str
    schwabClientFunctionId: str

@dataclass
class UserPreferenceAccount():
    accountNumber: str
    primaryAccount: bool
    type: str
    nickName: str
    accountColor: str
    displayAcctId: str
    autoPositionEffect: bool

@dataclass
class UserPreference():
    accounts: list[UserPreferenceAccount]
    streamerInfo: list[StreamerInfo]
    offers: list[Offer]
