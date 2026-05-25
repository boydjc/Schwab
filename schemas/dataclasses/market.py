from typing import Optional, TypeAlias
from dataclasses import dataclass, field

from schemas.enums import *

@dataclass
class Bond():
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    exchange: Optional[str] = None
    assetType: Optional[AssetType] = None
    bondFactor: Optional[str] = None
    bondMultiplier: Optional[str] = None
    bondPrice: Optional[float] = None
    type: Optional[AssetType] = None

@dataclass
class FundemantalInst(): 
    symbol: Optional[str] = None
    high52: Optional[float] = None
    low52: Optional[float] = None
    dividendAmount: Optional[float] = None
    dividendYield: Optional[float] = None
    dividendDate: Optional[str] = None
    peRatio: Optional[float] = None
    pegRatio: Optional[float] = None
    pbRatio: Optional[float] = None
    prRatio: Optional[float] = None
    pcfRatio: Optional[float] = None
    grossMarginTTM: Optional[float] = None
    grossMarginMRQ: Optional[float] = None
    netProfitMarginTTM: Optional[float] = None
    netProfitMarginMRQ: Optional[float] = None
    operatingMarginTTM: Optional[float] = None
    operatingMarginMRQ: Optional[float] = None
    returnOnEquity: Optional[float] = None
    returnOnAssets: Optional[float] = None
    returnOnInvestment: Optional[float] = None
    quickRatio: Optional[float] = None
    currentRatio: Optional[float] = None
    interestCoverage: Optional[float] = None
    totalDebtToCapital: Optional[float] = None
    ltDebtToEquity: Optional[float] = None
    totalDebtToEquity: Optional[float] = None
    epsTTM: Optional[float] = None
    epsChangePercentTTM: Optional[float] = None
    epsChangeYear: Optional[float] = None
    epsChange: Optional[float] = None
    revChangeYear: Optional[float] = None
    revChangeTTM: Optional[float] = None
    revChangeIn: Optional[float] = None
    sharesOutstanding: Optional[float] = None
    marketCapFloat: Optional[float] = None
    marketCap: Optional[float] = None
    bookValuePerShare: Optional[float] = None
    shortIntToFloat: Optional[float] = None
    shortIntDayToCover: Optional[float] = None
    divGrowthRate3Year: Optional[float] = None
    dividendPayAmount: Optional[float] = None
    dividendPayDate: Optional[str] = None
    beta: Optional[str] = None
    vol1DayAvg: Optional[float] = None
    vol10DayAvg: Optional[float] = None
    vol3MonthAvg: Optional[float] = None
    avg10DaysVolume: Optional[int] = None
    avg1DayVolume: Optional[int] = None
    avg3MonthVolume: Optional[int] = None
    declarationDate: Optional[str] = None
    dividendFreq: Optional[int] = None
    eps: Optional[float] = None
    corpactionDate: Optional[str] = None
    dtnVolume: Optional[int] = None
    nextDividendPayDate: Optional[str] = None
    nextDividendDate: Optional[str] = None
    fundLeverageFactor: Optional[float] = None
    fundStrategy: Optional[str] = None

@dataclass
class Instrument():
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    exchange: Optional[str] = None
    assetType: Optional[AssetType] = None
    type: Optional[AssetType] = None

@dataclass
class InstrumentResponse():
    cusip: Optional[str] = None
    symbol: Optional[str] = None
    description: Optional[str] = None
    exchange: Optional[str] = None
    assetType: Optional[AssetType] = None
    bondFactor: Optional[str] = None
    bondMultiplier: Optional[str] = None
    fundamental: Optional[FundemantalInst] = None
    instrumentInfo: Optional[Instrument] = None
    bondInstrument: Optional[Bond] = None
    type: Optional[AssetType] = None

@dataclass
class Hours:
    date: Optional[str] = None
    marketType: Optional[AssetType] = None
    exchange: Optional[str] = None
    category: Optional[str] = None
    product: Optional[str] = None
    productName: Optional[str] = None
    isOpen: Optional[bool] = None
    # Keys are dynamic (e.g. "preMarket", "regularMarket", "postMarket")
    # Values are lists of Interval objects
    sessionHours: dict[str, list[Interval]] = field(default_factory=dict)

@dataclass
class Interval():
    start: Optional[str]
    end: Optional[str]

@dataclass
class Screener():
    change: Optional[float]
    description: Optional[str]
    direction: Optional[Direction]
    last: Optional[float]
    symbol: Optional[str]
    totalVolume: Optional[int]

@dataclass
class Candle():
    close: Optional[float]
    datetime: Optional[int]
    datetimeISO8601: Optional[str]
    high: Optional[float]
    low: Optional[float]
    open: Optional[float]
    volume: Optional[int]

@dataclass
class CandleList():
    candles: Optional[list[Candle]]
    empty: Optional[bool]
    previousClose: Optional[float]
    previousCloseDate: Optional[int]
    previousCloseDateISO8601: Optional[str]
    symbol: Optional[str]

@dataclass
class EquityResponse():
    assetMainType: Optional[AssetType]
    assetSubType: Optional[EquityAssetSubType]
    ssid: Optional[int]
    symbol: Optional[str]
    realtime: Optional[bool]
    quoteType: Optional[QuoteType]
    extended: Optional[ExtendedMarket]
    fundamental: Optional[Fundamental]
    quote: Optional[QuoteEquity]
    reference: Optional[ReferenceEquity]
    regular: Optional[RegularMarket]

@dataclass
class Expiration():
    daysToExpiration: Optional[int]
    expiration: Optional[str]
    expirationType: Optional[ExpirationType]
    standard: Optional[bool]
    settlementType: Optional[SettlementType]
    optionRoots: Optional[str]

@dataclass
class ExpirationChain():
    status: Optional[str]
    expirationList: Optional[list[Expiration]]

@dataclass
class OptionDeliverables():
    symbol: Optional[str]
    assetType: Optional[str]
    deliverableUnitys: Optional[str]
    currencyType: Optional[str]

@dataclass
class OptionContract():
    putCall: Optional[PutCall]
    symbol: Optional[str]
    description: Optional[str]
    exchangeName: Optional[str]
    bidPrice: Optional[float]
    askPrice: Optional[float]
    lastPrice: Optional[float]
    markPrice: Optional[float]
    bidSize: Optional[int]
    askSize: Optional[int]
    lastSize: Optional[int]
    highPrice: Optional[float]
    lowPrice: Optional[float]
    openPrice: Optional[float]
    closePrice: Optional[float]
    totalVolume: Optional[int]
    tradeDate: Optional[int]
    quoteTimeInLong: Optional[int]
    tradeTimeInLong: Optional[int]
    netChange: Optional[float]
    volatility: Optional[float]
    delta: Optional[float]
    gamma: Optional[float]
    theta: Optional[float]
    vega: Optional[float]
    rho: Optional[float]
    timeValue: Optional[float]
    openInterest: Optional[float]
    isInTheMoney: Optional[bool]
    theoreticalOptionValue: Optional[float]
    theoreticalVolatility: Optional[float]
    isMini: Optional[bool]
    isNonStandard: Optional[bool]
    optionalDeliverablesList: Optional[OptionDeliverables]
    strikePrice: Optional[float]
    expirationDate: Optional[int]
    daysToExpiration: Optional[int]
    expirationType: Optional[ExpirationType]
    lastTradingDay: Optional[int]
    multiplier: Optional[float]
    settlementType: Optional[SettlementType]
    deliverableNote: Optional[str]
    isIndexOption: Optional[bool]
    percentChange: Optional[float]
    markChange: Optional[float]
    markPercentChange: Optional[float]
    isPennyPilot: Optional[bool]
    intrinsicValue: Optional[float]
    optionRoot: Optional[str]

@dataclass
class Underlying():
    ask: Optional[float]
    askSize: Optional[int]
    bid: Optional[float]
    bidSize: Optional[int]
    change: Optional[float]
    close: Optional[float]
    delayed: Optional[bool]
    description: Optional[str]
    exchangeName: Optional[ExchangeName]
    fiftyTwoWeekHigh: Optional[float]
    fiftyTwoWeekLow: Optional[float]
    highPrice: Optional[float]
    last: Optional[float]
    lowPrice: Optional[float]
    mark: Optional[float]
    markChange: Optional[float]
    markPercentChange: Optional[float]
    openPrice: Optional[float]
    percentChange: Optional[float]
    quoteTime: Optional[int]
    symbol: Optional[str]
    totalVolume: Optional[int]
    tradeTime: Optional[int]

@dataclass
class OptionContractMap():
    sessionHours: dict[str, list[Interval]] = field(default_factory=dict)

type OptionContractMap = dict[str, OptionContract]

@dataclass
class OptionChain():
    symbol: Optional[str]
    status: Optional[str]
    underlying: Optional[Underlying]
    strategy: Optional[Strategy]
    interval: Optional[float]
    isDelayed: Optional[bool]
    isIndex: Optional[bool]
    daysToExpiration: Optional[float]
    interestRate: Optional[float]
    underlyingPrice: Optional[float]
    volatility: Optional[float]
    callExpDateMap: dict[str, list[OptionContractMap]] = field(default_factory=dict)
    putExpDateMap: dict[str, list[OptionContractMap]] = field(default_factory=dict)

@dataclass
class ErrorSource():
    pointer: Optional[list[str]]
    parameter: Optional[str]
    header: Optional[str]

@dataclass
class Error():
    id: Optional[str]
    status: Optional[HttpStatus]
    title: Optional[str]
    detail: Optional[str]
    source: Optional[ErrorSource]

@dataclass
class ErrorResponse():
    errors: Optional[list[Error]]

@dataclass
class RegularMarket():
    regularMarketLastPrice: Optional[float]
    regularMarketLastSize: Optional[int]
    regularMarketNetChange: Optional[float]
    regularMarketPercentChange: Optional[float]
    regularMarketTradeTime: Optional[int]

@dataclass
class ReferenceOption():
    contractType: Optional[ContractType]
    cusip: Optional[str]
    daysToExpiration: Optional[int]
    deliverables: Optional[str]
    description: Optional[str]
    exchange: Optional[str]
    exchangeName: Optional[str]
    exerciseType: Optional[ExerciseType]
    expirationDay: Optional[int]
    expirationMonth: Optional[int]
    expirationType: Optional[ExpirationType]
    expirationYear: Optional[int]
    isPennyPilot: Optional[bool]
    lastTradingDay: Optional[int]
    multipler: Optional[float]
    settlementType: Optional[SettlementType]
    strikePrice: Optional[float]
    underlying: Optional[str]

@dataclass
class ReferenceMutualFund():
    cusip: Optional[str]
    description: Optional[str]
    exchange: Optional[str]
    exchangeName: Optional[str]

@dataclass
class ReferenceIndex():
    description: Optional[str]
    exchange: Optional[str]
    exchangeName: Optional[str]

@dataclass
class ReferenceFutureOption():
    contractType: Optional[ContractType]
    description: Optional[str]
    exchange: Optional[str]
    exchangeName: Optional[str]
    multiplier: Optional[float]
    expirationDate: Optional[int]
    expirationStyle: Optional[str]
    strikePrice: Optional[float]
    underlying: Optional[str]

@dataclass
class ReferenceFuture():
    description: Optional[str]
    exchange: Optional[str]
    exchangeName: Optional[str]
    futureActiveSymbol: Optional[str]
    futureExpirationDate: Optional[int]
    futureIsActive: Optional[bool]
    futureMultipler: Optional[bool]
    futurePriceFormat: Optional[str]
    futureSettlementPrice: Optional[float]
    futureTradingHours: Optional[str]
    product: Optional[str]

@dataclass
class ReferenceForex():
    description: Optional[str]
    exchange: Optional[str]
    exchangeName: Optional[str]
    isTradable: Optional[str]
    
@dataclass
class ReferenceEquity():
    cusip: Optional[str]
    description: Optional[str]
    exchange: Optional[str]
    exchangeName: Optional[str]
    fsiDesc: Optional[str]
    htbRate: Optional[str]
    isHardToBorrow: Optional[str]
    isShortable: Optional[str]
    otcMarketTier: Optional[str]

@dataclass
class QuoteResponseObject():
    equityResponse: Optional[EquityResponse]
    optionResponse: Optional[OptionResponse]
    forexResponse: Optional[ForexResponse]
    futureResponse: Optional[FutureResponse]
    futureOptionResponse: Optional[FutureOptionResponse]
    indexResponse: Optional[IndexResponse]
    mutualFundResponse: Optional[MutualFundResponse]
    quoteError: Optional[QuoteError]

type QuoteResponse = dict[str, QuoteResponseObject]

@dataclass
class QuoteRequest():
    cusips: Optional[list[str]]
    fields: Optional[str]
    ssids: Optional[list[int]]
    symbols: Optional[list[str]]
    realtime: Optional[bool]
    indicative: Optional[bool]

@dataclass
class QuoteOption():
    fiftyTwoWeekHigh: Optional[float]
    fiftyTwoWeekLow: Optional[float]
    askPrice: Optional[float]
    askSize: Optional[int]
    bidPrice: Optional[float]
    bidSize: Optional[int]
    closePrice: Optional[float]
    delta: Optional[float]
    gamma: Optional[float]
    highPrice: Optional[float]
    indAskPrice: Optional[float]
    indBidPrice: Optional[float]
    indQuoteTime: Optional[float]
    impliedYield: Optional[float]
    lastPrice: Optional[float]
    lastSize: Optional[int]
    lowPrice: Optional[float]
    mark: Optional[float]
    markChange: Optional[float]
    markPercentChange: Optional[float]
    moneyIntrinsicValue: Optional[float]
    netChange: Optional[float]
    netPercentChange: Optional[float]
    openInterest: Optional[float]
    openPrice: Optional[float]
    quoteTime: Optional[int]
    rho: Optional[float]
    securityStatus: Optional[str]
    theoreticalOptionValue: Optional[str]
    theta: Optional[float]
    timeValue: Optional[float]
    totalVolume: Optional[int]
    tradeTime: Optional[int]
    underlyingPrice: Optional[float]
    vega: Optional[float]
    volatility: Optional[float]

@dataclass
class QuoteMutualFund():
    fiftyTwoWeekHigh: Optional[float]
    fiftyTwoWeekLow: Optional[float]
    closePrice: Optional[float]
    nAV: Optional[float]
    netChange: Optional[float]
    netPercentChange: Optional[float]
    securityStatus: Optional[str]
    totalVolume: Optional[int]
    tradeTime: Optional[int]

@dataclass
class QuoteIndex():
    fiftyTwoWeekHigh: Optional[float]
    fiftyTwoWeekLow: Optional[float]
    closePrice: Optional[float]
    highPrice: Optional[float]
    lastPrice: Optional[float]
    lowPrice: Optional[float]
    netChange: Optional[float]
    netPercentChange: Optional[float]
    openPrice: Optional[float]
    securityStatus: Optional[str]
    totalVolume: Optional[int]
    tradeTime: Optional[int]

@dataclass
class QuoteFutureOption():
    askMICId: Optional[str]
    askPrice: Optional[float]
    askSize: Optional[int]
    bidMICId: Optional[str]
    bidPrice: Optional[float]
    bidSize: Optional[int]
    closePrice: Optional[float]
    highPrice: Optional[float]
    lastMICId: Optional[str]
    lastPrice: Optional[float]
    lastSize: Optional[int]
    lowPrice: Optional[float]
    mark: Optional[float]
    markChange: Optional[float]
    netChange: Optional[float]
    netPercentChange: Optional[float]
    openInterest: Optional[int]
    openPrice: Optional[float]
    quoteTime: Optional[int]
    securityStatus: Optional[str]
    settlemetPrice: Optional[float]
    tick: Optional[float]
    tickAmount: Optional[float]
    totalVolume: Optional[int]
    tradeTime: Optional[int]

@dataclass
class QuoteFuture():
    askMICId: Optional[str]
    askPrice: Optional[float]
    askSize: Optional[int]
    askTime: Optional[int]
    bidMICId: Optional[str]
    bidPrice: Optional[float]
    bidSize: Optional[int]
    bidTime: Optional[int]
    closePrice: Optional[float]
    futurePercentChange: Optional[float]
    highPrice: Optional[float]
    lastMICId: Optional[str]
    lastPrice: Optional[float]
    lastSize: Optional[int]
    lowPrice: Optional[float]
    mark: Optional[float]
    netChange: Optional[float]
    openInterest: Optional[int]
    openPrice: Optional[float]
    quoteTime: Optional[int]
    quotedInSession: Optional[int]
    securityStatus: Optional[str]
    settleTime: Optional[int]
    tick: Optional[float]
    tickAmount: Optional[float]
    totalVolume: Optional[int]
    tradeTime: Optional[int]

@dataclass
class QuoteForex():
    fiftyTwoWeekHigh: Optional[float]
    fiftyTwoWeekLow: Optional[float]
    askPrice: Optional[float]
    askSize: Optional[int]
    bidPrice: Optional[float]
    bidSize: Optional[int]
    closePrice: Optional[float]
    highPrice: Optional[float]
    lastPrice: Optional[float]
    lastSize: Optional[int]
    lowPrice: Optional[float]
    mark: Optional[float]
    netChange: Optional[float]
    netChangePercent: Optional[float]
    openPrice: Optional[float]
    quoteTime: Optional[int]
    securityStatus: Optional[str]
    tick: Optional[float]
    tickAmount: Optional[float]
    totalVolume: Optional[int]
    tradeTime: Optional[int]

@dataclass
class QuoteEquity():
    fiftyTwoWeekHigh: Optional[float]
    fiftyTwoWeekLow: Optional[float]
    askMICId: Optional[str]
    askPrice: Optional[float]
    askSize: Optional[int]
    askTime: Optional[int]
    bidMICId: Optional[str]
    bidPrice: Optional[float]
    bidSize: Optional[int]
    bidTime: Optional[int]
    closePrice: Optional[float]
    highPrice: Optional[float]
    lastMICId: Optional[str]
    lastPrice: Optional[float]
    lastSize: Optional[int]
    lowPrice: Optional[float]
    mark: Optional[float]
    markChange: Optional[float]
    markPercentChange: Optional[float]
    netChange: Optional[float]
    netPercentChange: Optional[float]
    openPrice: Optional[float]
    quoteTime: Optional[int]
    securityStatus: Optional[str]
    totalVolume: Optional[int]
    tradeTime: Optional[int]
    volatility: Optional[float]

@dataclass
class OptionResponse():
    assetMainType: Optional[AssetType]
    ssid: Optional[int]
    symbol: Optional[str]
    realtime: Optional[bool]
    quote: Optional[QuoteOption]
    reference: Optional[ReferenceOption]

@dataclass
class MutualFundResponse():
    assetMainType: Optional[AssetType]
    assetSubType: Optional[MutualFundAssetSubType]
    ssid: Optional[int]
    symbol: Optional[str]
    realtime: Optional[bool]
    fundamental: Optional[Fundamental]
    quote: Optional[QuoteMutualFund]
    reference: Optional[ReferenceMutualFund]

@dataclass
class IndexResponse():
    assetMainType: Optional[AssetType]
    ssid: Optional[int]
    symbol: Optional[str]
    realtime: Optional[bool]
    quote: Optional[QuoteIndex]
    reference: Optional[ReferenceIndex]

@dataclass
class FutureResponse():
    assetMainType: Optional[AssetType]
    ssid: Optional[int]
    symbol: Optional[str]
    realtime: Optional[bool]
    quote: Optional[QuoteFuture]
    reference: Optional[ReferenceFuture]

@dataclass
class FutureOptionResponse():
    assetMainType: Optional[AssetType]
    ssid: Optional[int]
    symbol: Optional[str]
    realtime: Optional[bool]
    quote: Optional[QuoteFutureOption]
    reference: Optional[ReferenceFutureOption]

@dataclass
class Fundamental():
    ave10DaysVolume: Optional[float]
    ave1YearVolume: Optional[float]
    declarationDate: Optional[str]
    divAmount: Optional[float]
    divExDate: Optional[str]
    divFreq: Optional[int]
    divPayAmount: Optional[float]
    divPayDate: Optional[str]
    divYield: Optional[float]
    eps: Optional[float]
    fundLeverageFactor: Optional[float]
    fundStrategy: Optional[FundStrategy]
    nextDivExDate: Optional[str]
    nextDivPayDate: Optional[str]
    peRatio: Optional[float]

@dataclass
class ForexResponse():
    assetMainType: Optional[AssetType]
    ssid: Optional[int]
    symbol: Optional[str]
    realtime: Optional[bool]
    quote: Optional[QuoteForex]
    reference: Optional[ReferenceForex]

@dataclass
class ExtendedMarket():
    askPrice: Optional[float]
    askSize: Optional[int]
    bidPrice: Optional[float]
    bidSize: Optional[int]
    lastPrice: Optional[float]
    lastSize: Optional[int]
    mark: Optional[float]
    quoteTime: Optional[int]
    totalVolume: Optional[int]
    tradeTime: Optional[int]

@dataclass
class QuoteError():
    invalidCusips: Optional[list[str]]
    invalidSSIDs: Optional[list[int]]
    invalidSymbols: Optional[list[str]]