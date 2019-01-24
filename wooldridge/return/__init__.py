def load():
    """name of dataset: return
    no of variables: 12
    no of observations: 142

    +----------+---------------------------+
    | variable | label                     |
    +----------+---------------------------+
    | roe      | return on equity, 1990    |
    | rok      | return on capital, 1990   |
    | dkr      | debt/capital, 1990        |
    | eps      | earnings per share, 1990  |
    | netinc   | net income, 1990 (mills.) |
    | sp90     | stock price, end 1990     |
    | sp94     | stock price, end 1994     |
    | salary   | CEO salary, 1990 (thous.) |
    | return   | % change s.p., 90-94      |
    | lsalary  | log(salary)               |
    | lsp90    | log(sp90)                 |
    | lnetinc  | log(netinc)               |
    +----------+---------------------------+

    Collected by Stephanie Balys, a former MSU undergraduate, from the New
    York Stock Exchange and Compustat."""

    import wooldridge
    return wooldridge.load(__file__, "return.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()