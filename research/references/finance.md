# Financial research methods

## Event studies and historical backtests

Specify the instrument, currency, price or total return series, adjustment method, sample period, event calendar, eligible window, threshold, reference peak, and deduplication rule. Define the signal, executable entry, forward horizons, holidays, censoring, benchmark, transaction costs, dividends, and missing data treatment before computing results.

For a drawdown trigger, scan chronologically for the first qualifying observation using only information available on that date. Define the running peak and whether the prior year's final close is included. Show eligible years without a trigger. Treat retrospective cycle endpoints and troughs as descriptive anchors. If the signal requires the closing price, state the earliest eligible entry, such as the next session's close.

Use calendar arithmetic for calendar month horizons. If a target date has no session, use the first close on or after it under this convention. An event baseline that uses the last close on or before a holiday needs its own stated convention. Identify trading day horizons explicitly. Keep incomplete forward horizons out of observed denominators.

Compute return by dividing exit value by entry value and subtracting one. Report mean, median, wins over observed cases, and adverse paths. An aligned median trajectory combines observations from different cases and has no single executable path. Compute any dispersion band from the corresponding aligned cohort.

Measure adverse excursion relative to the entry value. Measure maximum drawdown relative to the running peak. Include the entry observation for a measure that cannot be positive. Label these metrics separately.

Compare entry rules on the same qualified cases and include a suitable control when feasible. Check sensitivity to thresholds selected in advance. Discuss overlapping windows, clustered events, market changes, survivorship, and selection bias where they matter. A historical hit rate describes the observed sample.

## Rates and bond scenarios

Distinguish coupon rate, coupon cash yield on purchase price, yield to maturity, quoted SEC yield, price return, and total holding period return. For a specific bond, retain the instrument identifier, coupon schedule, maturity, clean price, accrued interest, settlement, and face amount. Treat order previews as indicative, and verify executable pricing separately.

Compute future dirty value by discounting remaining coupon and principal cash flows at the scenario yield using the correct coupon frequency and fractional periods. Subtract accrued interest to obtain clean value. For holding period return, add future dirty sale proceeds and coupons received with any assumed reinvestment, subtract the initial dirty outlay, and divide by that outlay. State treatment of spread, fees, and taxes. Avoid counting accrued interest or coupons twice. Distinguish repricing on the same date from a future sale with shorter remaining maturity.

For rate cycles, state the retrospective endpoint rule and use observations with consistent dates and maturities. One percentage point equals 100 basis points. Report yield changes separately from investment returns. Mark series gaps and identify proxies. Exclude maturity proxies from aggregates that require a consistent maturity. Treat scenario yields as assumptions and verify current market expectations from fresh evidence.

## Financial sources

Prefer central banks, treasuries, official index providers, issuer filings, and official calendars. Check actual dataset coverage and record adjustments or transformations by the provider. Where a historical extract fills a gap, verify overlap and disclose any limitations. Keep raw observations, exclusions, event tables, and calculation code for reproducibility.
