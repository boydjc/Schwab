from typing import Optional
from dataclasses import dataclass

from schemas.enums import *

@dataclass
class AccountNumberHash():
    accountNumber: Optional[str] = None
    hashValue: Optional[str] = None

@dataclass
class OrderBalance():
    orderValue: Optional[float] = None
    projectedAvailableFund: Optional[float] = None
    projectedBuyingPower: Optional[float] = None
    projectedCommission: Optional[float] = None

@dataclass
class OrderLeg():
    askPrice: Optional[float] = None
    bidPrice: Optional[float] = None
    lastPrice: Optional[float] = None
    markPrice: Optional[float] = None
    projectedCommission: Optional[float] = None
    quantity: Optional[float] = None
    finalSymbol: Optional[str] = None
    legId: Optional[int] = None
    assetType: Optional[AssetType] = None
    instruction: Optional[Instruction] = None

@dataclass
class OrderStrategy():
    accountNumber: Optional[str] = None
    advancedOrderType: Optional[AdvancedOrderType] = None
    closeTime: Optional[str] = None
    enteredTime: Optional[str] = None
    orderBalance: Optional[OrderBalance] = None
    orderStrategyType: Optional[OrderStrategyType] = None
    orderVersion: Optional[int] = None
    session: Optional[Session] = None
    status: Optional[Status] = None
    allOrNone: Optional[bool] = None
    discretionary: Optional[bool] = None
    duration: Optional[Duration] = None
    filledQuantity: Optional[float] = None
    orderType: Optional[OrderType] = None
    orderValue: Optional[float] = None
    price: Optional[float] = None
    quantity: Optional[float] = None
    remainingQuantity: Optional[float] = None
    sellNonMarginableFirst: Optional[bool] = None
    settlementInstruction: Optional[SettlementInstruction] = None
    strategy: Optional[ComplexOrderStrategyType] = None
    amountIndicator: Optional[AmountIndicator] = None
    orderLegs: Optional[list[OrderLeg]] = None

@dataclass
class OrderValidationDetail():
    validationRuleName: Optional[str] = None
    message: Optional[str] = None
    activityMessage: Optional[str] = None
    originalSeverity: Optional[APIRuleAction] = None
    overrideName: Optional[str] = None
    overrideSeverity: Optional[APIRuleAction] = None

@dataclass
class OrderValidationResult():
    alerts: Optional[list[OrderValidationDetail]] = None
    accepts: Optional[list[OrderValidationDetail]] = None
    rejects: Optional[list[OrderValidationDetail]] = None
    reviews: Optional[list[OrderValidationDetail]] = None
    warns: Optional[list[OrderValidationDetail]] = None

@dataclass
class FeeValue():
    value: Optional[float] = None
    type: Optional[FeeType] = None

@dataclass
class FeeLeg():
    feeValues: Optional[list[FeeValue]] = None

@dataclass
class Fees():
    feeLegs: Optional[list[FeeValue]] = None

@dataclass
class CommissionValue():
    value: Optional[float] = None
    type: Optional[FeeType] = None

@dataclass
class CommissionLeg():
    commissionValues: Optional[list[CommissionValue]] = None

@dataclass
class Commission():
    commissionLegs: Optional[list[CommissionLeg]] = None

@dataclass
class CommissionAndFee():
    commission: Optional[Commission] = None
    fee: Optional[Fees] = None
    trueCommission: Optional[Commission] = None

@dataclass
class AccountCashEquivalent():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None
    type: Optional[AccountCashEquivalentType] = None

@dataclass
class AccountEquity():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[str] = None
    netChange: Optional[float] = None

@dataclass
class AccountFixedIncome():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None
    maturityDate: Optional[str] = None
    factor: Optional[float] = None
    variableRate: Optional[float] = None

@dataclass
class AccountMutualFund():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None

@dataclass
class AccountAPIOptionDeliverable():
    symbol: Optional[str] = None
    deliverableUnits: Optional[float] = None
    apiCurrencyType: Optional[APICurrencyType] = None
    assetType: Optional[AssetType] = None

@dataclass
class AccountOption():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None
    optionDeliverables: Optional[list[AccountAPIOptionDeliverable]] = None
    putCall: Optional[PutCall] = None
    optionMultiplier: Optional[int] = None
    type: Optional[AccountOptionType] = None
    underlyingSymbol: Optional[str] = None

@dataclass
class AccountsInstrument():
    accountCashEquivalent: Optional[AccountCashEquivalent] = None
    accountEquity: Optional[AccountEquity] = None
    accountFixedIncome: Optional[AccountFixedIncome] = None
    accountOption: Optional[AccountOption] = None

@dataclass
class Position():
    shortQuantity: Optional[float] = None
    averagePrice: Optional[float] = None
    currentDayProfitLoss: Optional[float] = None
    currentDayProfitLossPercentage: Optional[float] = None
    longQuantity: Optional[float] = None
    settledLongQuantity: Optional[float] = None
    settledShortQuantity: Optional[float] = None
    agedQuantity: Optional[float] = None
    instrument: Optional[AccountsInstrument] = None
    marketValue: Optional[float] = None
    maintenanceRequirement: Optional[float] = None
    averageLongPrice: Optional[float] = None
    averageShortPrice: Optional[float] = None
    taxLotAverageLongPrice: Optional[float] = None
    taxLotAverageShortPrice: Optional[float] = None
    longOpenProfitLoss: Optional[float] = None
    shortOpenProfitLoss: Optional[float] = None
    previousSessionLongQuantity: Optional[float] = None
    previousSessionShortQuantity: Optional[float] = None
    currentDayCost: Optional[float] = None
    
@dataclass 
class CashAccount():
    type: Optional[CashAccountType] = None
    accountNumber: Optional[str] = None
    roundTrips: Optional[int] = None
    isDayTrader: Optional[bool] = None
    isClosingOnlyRestricted: Optional[bool] = None
    pfcbFlag: Optional[bool] = None
    positions: Optional[list[Position]] = None
    initialBalances: Optional[CashInitialBalance] = None
    currentBalances: Optional[CashBalance] = None
    projectedBalances: Optional[CashBalance] = None

@dataclass
class CashInitialBalance():
    accruedInterest: Optional[float] = None
    cashAvaiableForTrading: Optional[float] = None
    cashAvaiableForWithdrawal: Optional[float] = None
    cashBalance: Optional[float] = None
    bondValue: Optional[float] = None
    cashReceipts: Optional[float] = None
    liquidationValue: Optional[float] = None
    longOptionMarketValue: Optional[float] = None
    longStockValue: Optional[float] = None
    moneyMarketFund: Optional[float] = None
    mutualFundValue: Optional[float] = None
    shortOptionMarketValue: Optional[float] = None
    shortStockValue: Optional[float] = None
    isInCall: Optional[float] = None
    unsettledCash: Optional[float] = None
    cashDebtCallValue: Optional[float] = None
    pendingDeposits: Optional[float] = None
    accountValue: Optional[float] = None

@dataclass
class CashBalance():
    cashAvaiableForTrading: Optional[float] = None
    cashAvaiableForWithdrawal: Optional[float] = None
    cashCall: Optional[float] = None
    longNonMarginableMarketValue: Optional[float] = None
    totalCash: Optional[float] = None
    cashDebitCallValue: Optional[float] = None
    unsettledCash: Optional[float] = None

@dataclass
class MarginInitialBalance():
    accruedInterest: Optional[float] = None
    avaiableFundsNonMarginableTrade: Optional[float] = None
    bondValue: Optional[float] = None
    buyingPower: Optional[float] = None
    cashBalance: Optional[float] = None
    cashAvaiableForTrading: Optional[float] = None
    cashReceipts: Optional[float] = None
    dayTradingBuyingPower: Optional[float] = None
    dayTradingBuyingPowerCall: Optional[float] = None
    dayTradingEquityCall: Optional[float] = None
    equity: Optional[float] = None
    equityPercentage: Optional[float] = None
    liquidationValue: Optional[float] = None
    longMarginValue: Optional[float] = None
    longOptionMarketValue: Optional[float] = None
    longStockValue: Optional[float] = None
    maintenanceCall: Optional[float] = None
    maintenanceRequirement: Optional[float] = None
    margin: Optional[float] = None
    marginEquity: Optional[float] = None
    moneyMarketFund: Optional[float] = None
    mutualFundValue: Optional[float] = None
    regTCall: Optional[float] = None
    shortMarginValue: Optional[float] = None
    shortOptionMarketValue: Optional[float] = None
    shortStockValue: Optional[float] = None
    totalCash: Optional[float] = None
    isInCall: Optional[float] = None
    unsettledCash: Optional[float] = None
    pendingDeposits: Optional[float] = None
    marginBalance: Optional[float] = None
    shortBalance: Optional[float] = None
    accountValue: Optional[float] = None

@dataclass
class MarginBalance():
    avaiableFunds: Optional[float] = None
    avaiableFundsNonMarginableTrade: Optional[float] = None
    buyingPower: Optional[float] = None
    buyingPowerNonMarginableTrade: Optional[float] = None
    dayTradingBuyingPower: Optional[float] = None
    dayTradingBuyingPowerCall: Optional[float] = None
    equity: Optional[float] = None
    equityPercentage: Optional[float] = None
    longMarginValue: Optional[float] = None
    maintenanceCall: Optional[float] = None
    maintenanceRequirement: Optional[float] = None
    marginBalance: Optional[float] = None
    regTCall: Optional[float] = None
    shortBalance: Optional[float] = None
    shortMarginValue: Optional[float] = None
    sma: Optional[float] = None
    isInCall: Optional[float] = None
    stockBuyingPower: Optional[float] = None
    optionBuyingPower: Optional[float] = None

@dataclass
class MarginAccount():
    type: Optional[MarginAccountType] = None
    accountNumber: Optional[str] = None
    roundTrips: Optional[int] = None
    isDayTrader: Optional[bool] = None
    isClosingOnlyRestricted: Optional[bool] = None
    pfcbFlag: Optional[bool] = None
    positions: Optional[list[Position]] = None
    initialBalances: Optional[MarginInitialBalance] = None
    currentBalance: Optional[MarginBalance] = None
    projectedBalance: Optional[MarginBalance] = None

@dataclass
class SecuritiesAccount():
    marginAccount: Optional[MarginAccount] = None
    cashAccount: Optional[CashAccount] = None

@dataclass
class Account():
    securitiesAccount: Optional[SecuritiesAccount] = None

@dataclass
class DateParam():
    date: Optional[str] = None # format is yyyy-MM-dd'T'HH:mm:ss.SSZ

@dataclass
class Order():
    session: Optional[Session] = None
    duration: Optional[Duration] = None
    orderType: Optional[OrderType] = None
    cancelTime: Optional[str] = None
    complexOrderStrategyType: Optional[ComplexOrderStrategyType] = None
    quantity: Optional[float] = None
    filledQuantity: Optional[float] = None
    remainingQuantity: Optional[float] = None
    requestedDestination: Optional[RequestedDestination] = None
    destinationLinkName: Optional[str] = None
    releaseTime: Optional[str] = None
    stopPrice: Optional[float] = None
    stopPriceLinkBasis: Optional[StopPriceLinkBasis] = None
    stopPriceLinkType: Optional[StopPriceLinkType] = None
    stopPriceOffset: Optional[float] = None
    stopType: Optional[StopType] = None
    priceLinkBasis: Optional[PriceLinkBasis] = None
    priceLinkType: Optional[PriceLinkType] = None
    price: Optional[float] = None
    taxLotMethod: Optional[TaxLotMethod] = None
    orderLegCollection: Optional[list[OrderLegCollection]] = None
    activationPrice: Optional[float] = None
    specialInstruction: Optional[SpecialInstruction] = None
    orderStrategyType: Optional[OrderStrategyType] = None
    orderId: Optional[int] = None
    cancelable: Optional[bool] = None
    editable: Optional[bool] = None
    status: Optional[Status] = None
    enteredTime: Optional[str] = None
    closeTime: Optional[str] = None
    tag: Optional[str] = None
    accountNumber: Optional[int] = None
    orderActivityCollection: Optional[list[OrderActivity]] = None
    replacingOrderCollection: Optional[list[Order]] = None
    childOrderStrategies: Optional[list[Order]] = None
    statusDescription: Optional[str] = None
    
@dataclass
class ExecutionLeg():
    legId: Optional[int] = None
    price: Optional[float] = None
    quantity: Optional[float] = None
    mismarkedQuantity: Optional[float] = None
    instrumentId: Optional[int] = None
    time: Optional[str] = None

@dataclass
class OrderActivity():
    activityType: Optional[ActivityType] = None
    executionType: Optional[ExecutionType] = None
    quantity: Optional[float] = None
    orderRemainingQuantity: Optional[float] = None
    executionLegs: Optional[list[ExecutionLeg]] = None

@dataclass
class OrderRequest():
    session: Optional[Session] = None
    duration: Optional[Duration] = None
    orderType: Optional[OrderTypeRequest] = None
    cancelTime: Optional[str] = None
    complexOrderStrategyType: Optional[ComplexOrderStrategyType] = None
    quantity: Optional[float] = None
    filledQuantity: Optional[float] = None
    remainingQuantity: Optional[float] = None
    destinationLinkName: Optional[str] = None
    releaseTime: Optional[str] = None
    stopPrice: Optional[float] = None
    stopPriceLinkBasis: Optional[StopPriceLinkBasis] = None
    stopPriceLinkType: Optional[StopPriceLinkType] = None
    stopPriceOffset: Optional[float] = None
    stopType: Optional[StopType] = None
    priceLinkBasis: Optional[PriceLinkBasis] = None
    priceLinkType: Optional[PriceLinkType] = None
    price: Optional[float] = None
    taxLotMethod: Optional[TaxLotMethod] = None
    orderLegCollection: Optional[list[OrderLegCollection]] = None
    activationPrice: Optional[float] = None
    specialInstruction: Optional[SpecialInstruction] = None
    orderStrategyType: Optional[OrderStrategyType] = None
    orderId: Optional[int] = None
    cancelable: Optional[bool] = None
    editable: Optional[bool] = None
    status: Optional[Status] = None
    enteredTime: Optional[str] = None
    closeTime: Optional[str] = None
    accountNumber: Optional[int] = None
    orderActivityCollection: Optional[list[OrderActivity]] = None
    replacingOrderCollection: Optional[list[OrderStrategy]] = None
    childOrderStrategies: Optional[list[OrderStrategy]] = None
    statusDescription: Optional[str] = None

@dataclass
class PreviewOrder():
    orderId: Optional[int] = None
    orderStrategy: Optional[OrderStrategy] = None
    orderValidationResult: Optional[OrderValidationResult] = None
    commissionAndFee: Optional[CommissionAndFee] = None

@dataclass
class OrderLegCollection():
    orderLegType: Optional[OrderLegType] = None
    legId: Optional[int] = None
    instrument: Optional[Instrument] = None
    instruction: Optional[Instruction] = None
    positionEffect: Optional[PositionEffect] = None
    quantity: Optional[float] = None
    quantityType: Optional[QuantityType] = None
    divCapGains: Optional[DivCapGains] = None
    toSymbol: Optional[str] = None

@dataclass
class SecuritiesAccountBase():
    type: Optional[SecuritiesAccountBaseType] = None
    accountNumber: Optional[str] = None
    roundTrips: Optional[int] = None
    isDayTrader: Optional[bool] = None
    isClosingOnlyRestricted: Optional[bool] = None
    pfcbFlag: Optional[bool] = None
    position: Optional[list[Position]] = None

@dataclass
class TransactionBaseInstrument():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None

@dataclass
class AccountsBaseInstrument():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None

@dataclass
class Currency():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None

@dataclass
class Forex():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None
    type: Optional[ForexType] = None
    baseCurrency: Optional[Currency] = None
    counterCurrency: Optional[Currency] = None

@dataclass
class Future():
    activeContract: Optional[bool] = None
    type: Optional[FutureType] = None
    expirationDate: Optional[str] = None
    lastTradingDate: Optional[str] = None
    firstNoticeDate: Optional[str] = None
    multipler: Optional[float] = None
    transactionCashEquivalent: Optional[TransactionCashEquivalent] = None
    collectiveInvestment: Optional[CollectiveInvestment] = None
    currency: Optional[Currency] = None
    transactionEquity: Optional[TransactionEquity] = None
    transactionFixedIncome: Optional[TransactionFixedIncome] = None
    forex: Optional[Forex] = None
    index: Optional[Index] = None
    transactionMutualFund: Optional[TransactionMutualFund] = None
    transactionOption: Optional[TransactionOption] = None
    product: Optional[Product] = None

@dataclass
class TransactionCashEquivalent():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netchange: Optional[float] = None
    type: Optional[TransactionCashEquivalentType] = None

@dataclass
class CollectiveInvestment():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None
    type: Optional[CollectiveInvestmentType] = None

@dataclass
class TransactionInstrument():
    transactionCashEquivalent: Optional[TransactionCashEquivalent] = None
    collectiveInvestment: Optional[CollectiveInvestment] = None
    currency: Optional[Currency] = None
    transactionEquity: Optional[TransactionEquity] = None
    tansactionFixedIncome: Optional[TransactionFixedIncome] = None
    forex: Optional[Forex] = None
    future: Optional[Future] = None
    index: Optional[Index] = None
    transactionMutualFund: Optional[TransactionMutualFund] = None
    transactionOption: Optional[TransactionOption] = None
    product: Optional[Product] = None

@dataclass
class TransactionEquity():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange:Optional[float] = None
    type: Optional[TransactionEquityType] = None

@dataclass
class TransactionFixedIncome():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None
    type: Optional[TransactionFixedIncomeType] = None
    maturityDate: Optional[str] = None
    factor: Optional[float] = None
    multiplier: Optional[float] = None
    variableRate: Optional[float] = None

@dataclass
class TransactionMutualFund():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None
    fundFamilyName: Optional[str] = None
    fundFamilySymbol: Optional[str] = None
    fundGroup: Optional[str] = None
    type: Optional[TransactionMutualFundType] = None
    exchangeCutoffTime: Optional[str] = None
    purchaseCutoffTime: Optional[str] = None
    redemptionCutoffTime: Optional[str] = None
    
@dataclass
class TransactionAPIOptionDeliverable():
    rootSymbol: Optional[str] = None
    strikePercent: Optional[int] = None
    deliverableNumber: Optional[int] = None
    deliverableUnits: Optional[float] = None
    deliverable: Optional[TransactionInstrument] = None
    assetType: Optional[AssetType] = None

@dataclass 
class Product():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None
    type: Optional[ProductType] = None

@dataclass
class Index():
    activeContract: Optional[bool] = None
    type: Optional[IndexType] = None
    transactionCashEquivalent: Optional[TransactionCashEquivalent] = None
    collectiveInvestment: Optional[CollectiveInvestment] = None
    currency: Optional[Currency] = None
    transactionEquity: Optional[TransactionEquity] = None
    transactionFixedIncome: Optional[TransactionFixedIncome] = None
    forex: Optional[Forex] = None
    future: Optional[Future] = None
    transactionMutualFund: Optional[TransactionMutualFund] = None
    transactionOption: Optional[TransactionOption] = None
    product: Optional[Product] = None

@dataclass
class TransactionOption():
    assetType: Optional[AssetType] = None
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    instrumentId: Optional[int] = None
    netChange: Optional[float] = None
    expirationDate: Optional[str] = None
    optionDeliverables: Optional[list[TransactionAPIOptionDeliverable]] = None
    optionPremiumMulitpler: Optional[int] = None
    putCall: Optional[PutCall] = None
    strikePrice: Optional[float] = None
    type: Optional[TransactionOptionType] = None
    underlyingSymbol: Optional[str] = None
    underlyingCusip: Optional[str] = None
    deliverable: Optional[TransactionInstrument] = None

@dataclass
class UserDetails():
    cdDomainId: Optional[str] = None
    login: Optional[str] = None
    type: Optional[UserDetailsType] = None
    userId: Optional[int] = None
    systemUserName: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    brokerRepCode: Optional[str] = None

@dataclass
class TransferItem():
    instrument: Optional[TransactionInstrument] = None
    amount: Optional[float] = None
    cost: Optional[float] = None
    price: Optional[float] = None
    feeType: Optional[FeeType] = None
    positionEffect: Optional[PositionEffect] = None

@dataclass
class Transaction():
    activityId: Optional[int] = None
    time: Optional[str] = None
    user: Optional[UserDetails] = None
    description: Optional[str] = None
    accountNumber: Optional[str] = None
    type: Optional[TransactionType] = None
    status: Optional[Status] = None
    subAccount: Optional[SubAccount] = None
    tradeDate: Optional[str] = None
    settlementDate: Optional[str] = None
    positionId: Optional[int] = None
    orderId: Optional[int] = None
    netAmount: Optional[float] = None
    activityType: Optional[ActivityType] = None
    transferItems: Optional[list[TransferItem]] = None

@dataclass
class Offer():
    level2Permissions: Optional[bool] = None
    mktDataPermission: Optional[str] = None

@dataclass
class StreamerInfo():
    streamerSocketUrl: Optional[str] = None
    schwabClientCustomerId: Optional[str] = None
    schwabClientCorrelId: Optional[str] = None
    schwabClientChannel: Optional[str] = None
    schwabClientFunctionId: Optional[str] = None

@dataclass
class UserPreferenceAccount():
    accountNumber: Optional[str] = None
    primaryAccount: Optional[bool] = None
    type: Optional[str] = None
    nickName: Optional[str] = None
    accountColor: Optional[str] = None
    displayAcctId: Optional[str] = None
    autoPositionEffect: Optional[bool] = None

@dataclass
class UserPreference():
    accounts: Optional[list[UserPreferenceAccount]] = None
    streamerInfo: Optional[list[StreamerInfo]] = None
    offers: Optional[list[Offer]] = None

@dataclass
class ServiceError():
    message: Optional[str] = None
    errors: Optional[list[str]] = None

@dataclass
class Instrument:
    assetType: Optional[AssetType] = None
    symbol: Optional[str] = None
