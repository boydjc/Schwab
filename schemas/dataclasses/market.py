from typing import Optional
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
    assetMainType: 

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

    