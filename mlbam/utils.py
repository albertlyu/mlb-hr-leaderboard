#!/usr/bin/env python3
'''
A module for handy utils
'''
from datetime import timedelta

def last_date_of_month(date):
    '''
    Get the last date of the month given any datetime Date
    @param  {datetime.date} any date you want
    @return {datetime.date} the last date of that month
    '''
    next_month = date.replace(day=28) + timedelta(days=4)
    return next_month - timedelta(days=next_month.day)
