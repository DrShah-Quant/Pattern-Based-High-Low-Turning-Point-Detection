
from AlgoAPI import AlgoAPIUtil, AlgoAPI_Backtest
from collections import deque

class AlgoEvent:
    def __init__(self):
        self.myinstrument = []
        self.price_history = {}       # {instrument: deque of (timestamp, close)}
        self.reported_points = {}     # {instrument: set of reported timestamps}
    
    def start(self, mEvt):
        self.evt = AlgoAPI_Backtest.AlgoEvtHandler(self, mEvt)
        self.myinstrument = mEvt["subscribeList"]
        for instrument in self.myinstrument:
            self.price_history[instrument] = deque(maxlen=180)
            self.reported_points[instrument] = set()
        self.evt.start()
    
    def on_bulkdatafeed(self, isSync, bd, ab):
        # Step 1: update close price history
        for instrument in self.myinstrument:
            if instrument not in bd:
                #self.evt.consoleLog(f"ERROR---------")
                continue
            
            ts = bd[instrument]['timestamp']
            close = bd[instrument].get('close', bd[instrument].get('lastPrice'))
            self.price_history[instrument].append((ts, close))
            #self.evt.consoleLog(f"timestamp {ts} close {close}")
        
        # Step 2: run analysis for all instruments
        for instrument in self.myinstrument:
            if len(self.price_history[instrument]) >= 3:
                self.analyze_and_print_highs_lows(instrument)
            else:
                self.evt.consoleLog(f"[SKIP] {instrument}: only {len(self.price_history[instrument])} data points")

    def analyze_and_print_highs_lows(self, instrument):
        data = list(self.price_history[instrument])
        new_results = []

        for i in range(1, len(data) - 1):
            prev = data[i - 1]
            curr = data[i]
            nxt = data[i + 1]

            # Pattern 1: Low → High → Low → store the high
            if prev[1] < curr[1] and nxt[1] < curr[1]:
               # if curr[0] not in self.reported_points[instrument]:
                #self.evt.consoleLog(f"[HIGH]")
                new_results.append(("High", curr[0], curr[1]))
                    #self.reported_points[instrument].add(curr[0])

            # Pattern 2: High → Low → High → store the low
            if prev[1] > curr[1] and nxt[1] > curr[1]:
                #if curr[0] not in self.reported_points[instrument]:
                #self.evt.consoleLog(f"[LOW]")
                new_results.append(("Low", curr[0], curr[1]))
                #    self.reported_points[instrument].add(curr[0])

        # Always report
        self.evt.consoleLog(f"[{instrument}] Pattern check on latest {len(data)} closes:")
        if new_results:
            for label, ts, price in new_results:
                self.evt.consoleLog(f"  {label} Point - Time: {ts}, Close: {price:.2f}")
        else:
            self.evt.consoleLog("  No new pattern found.")

    def on_marketdatafeed(self, md, ab):
        pass

    def on_newsdatafeed(self, nd):
        pass

    def on_weatherdatafeed(self, wd):
        pass

    def on_econsdatafeed(self, ed):
        pass

    def on_corpAnnouncement(self, ca):
        pass

    def on_orderfeed(self, of):
        pass

    def on_dailyPLfeed(self, pl):
        pass

    def on_openPositionfeed(self, op, oo, uo):
        pass

