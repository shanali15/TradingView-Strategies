// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © CryptoCarrier

//@version=4

strategy("Task 7b", overlay=true)


fromMonth = input(defval = 4,    title = "From Month",      type = input.integer, minval = 1, maxval = 12)
fromDay   = input(defval = 24,    title = "From Day",        type = input.integer, minval = 1, maxval = 31)
fromYear  = input(defval = 2000, title = "From Year",       type = input.integer, minval = 1970)
thruMonth = input(defval = 4,    title = "Thru Month",      type = input.integer, minval = 1, maxval = 12)
thruDay   = input(defval = 1,    title = "Thru Day",        type = input.integer, minval = 1, maxval = 31)
thruYear  = input(defval = 2020, title = "Thru Year",       type = input.integer, minval = 1970)

showDate  = input(defval = true, title = "Show Date Range", type = input.bool)

// === FUNCTION EXAMPLE ===
start     = timestamp(fromYear, fromMonth, fromDay, 00, 00)        // backtest start window
finish    = timestamp(thruYear, thruMonth, thruDay, 23, 59)        // backtest finish window
window()  => time >= start and time <= finish ? true : false 



length = input(20, minval=1)
src = input(close, title="Source")
mult = input(2.0, minval=0.001, maxval=50)
basis = sma(src, length)
dev = mult * stdev(src, length)
upper = basis + dev
lower = basis - dev
source1=close
plot(basis, title='Boll_Mid' , color=color.blue)
p1 = plot(upper,title='Boll_UP', color=color.green)
p2 = plot(lower,title='Boll_LOW', color=color.red)
fill(p1, p2)





lengthq = input(55, minval=1)
src2 = input(close, title="Source")
e1 = ema(src2, lengthq)

plot(e1,color= color.white)
sma1 = input(close, title ='daily price')

plot(sma1,color=color.yellow)


long=sma1>basis
long1 = sma1>e1
exit=sma1<basis



strategy.entry("WT Cross", strategy.long, when=long and long1 and window())
strategy.close("WT Cross", when=exit )

stoploss=input(100)
strategy.exit("short exit", "WT Cross", loss=close*(stoploss/100) / syminfo.mintick)