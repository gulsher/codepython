monthConversions = {
    "jan":"january",
    "feb":"february",
    "mar":"march",
    "apr":"april",
    "may":"may",
    "jun":"june",
    "jul":"july",
    "aug":"august",
    "sep":"september",
    "oct":"october",
    "nov":"november",
    "dec":"december"
}

print(monthConversions['jun'])
print(monthConversions.get('jan'))
print(monthConversions.get('janunry','not a valid month'))
