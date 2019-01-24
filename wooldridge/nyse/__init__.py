def load():
    """name of dataset: nyse
    no of variables: 8
    no of observations: 691

    +----------+------------------------+
    | variable | label                  |
    +----------+------------------------+
    | price    | NYSE stock price index |
    | return   | 100*(p - p(-1))/p(-1)) |
    | return_1 | lagged return          |
    | t        |                        |
    | price_1  |                        |
    | price_2  |                        |
    | cprice   | price - price_1        |
    | cprice_1 | lagged cprice          |
    +----------+------------------------+

    These are Wednesday closing prices of value-weighted NYSE average,
    available in many publications. I do not recall the particular source
    I used when I collected these data at MIT. Probably the easiest way to
    get similar data is to go to the NYSE web site, www.nyse.com."""

    import wooldridge
    return wooldridge.load(__file__, "nyse.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()