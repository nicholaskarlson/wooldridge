def load():
    """name of dataset: traffic2
    no of variables: 48
    no of observations: 108

    +----------+---------------------------------+
    | variable | label                           |
    +----------+---------------------------------+
    | year     | 1981 to 1989                    |
    | totacc   | statewide total accidents       |
    | fatacc   | statewide fatal accidents       |
    | injacc   | statewide injury accidents      |
    | pdoacc   | property damage only accidents  |
    | ntotacc  | noninterstate total acc.        |
    | nfatacc  | noninterstate fatal acc.        |
    | ninjacc  | noninterstate injur acc.        |
    | npdoacc  | noninterstate property acc.     |
    | rtotacc  | tot. acc. on rural 65 mph roads |
    | rfatacc  | fat. acc. on rural 65 mph roads |
    | rinjacc  | inj. acc. on rural 65 mph roads |
    | rpdoacc  | prp. acc. on rural 65 mph roads |
    | ushigh   | acc. on U.S. highways           |
    | cntyrds  | acc. on county roads            |
    | strtes   | acc. on state routes            |
    | t        | time trend                      |
    | tsq      | t^2                             |
    | unem     | state unemployment rate         |
    | spdlaw   | =1 after 65 mph in effect       |
    | beltlaw  | =1 after seatbelt law           |
    | wkends   | # weekends in month             |
    | feb      | =1 if month is Feb.             |
    | mar      |                                 |
    | apr      |                                 |
    | may      |                                 |
    | jun      |                                 |
    | jul      |                                 |
    | aug      |                                 |
    | sep      |                                 |
    | oct      |                                 |
    | nov      |                                 |
    | dec      |                                 |
    | ltotacc  | log(totacc)                     |
    | lfatacc  | log(fatacc)                     |
    | prcfat   | 100*(fatacc/totacc)             |
    | prcrfat  | 100*(rfatacc/rtotacc)           |
    | lrtotacc | log(rtotacc)                    |
    | lrfatacc | log(rfatacc)                    |
    | lntotacc | log(ntotacc)                    |
    | lnfatacc | log(nfatacc)                    |
    | prcnfat  | 100*(nfatacc/ntotacc)           |
    | lushigh  | log(ushigh)                     |
    | lcntyrds | log(cntyrds)                    |
    | lstrtes  | log(strtes)                     |
    | spdt     | spdlaw*t                        |
    | beltt    | beltlaw*t                       |
    | prcfat_1 | prcfat[_n-1]                    |
    +----------+---------------------------------+

    P.S. McCarthy (1994), “Relaxed Speed Limits and Highway Safety: New
    Evidence from California,” Economics Letters 46, 173-179. Professor
    McCarthy kindly provided the data."""

    import wooldridge
    return wooldridge.load(__file__, "traffic2.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()