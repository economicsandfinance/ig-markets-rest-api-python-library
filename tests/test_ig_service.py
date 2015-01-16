#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Run unit tests using
nosetests -s -v
"""

import trading_ig
from trading_ig import IGService
from trading_ig.config import ConfigEnvVar
#from trading_ig_config import config # defines username, password, api_key, acc_type, acc_number
import pandas as pd
import pprint
import os
import datetime
#from datetime import datetime, timedelta

"""
Environment variables must be set using

export IG_SERVICE_USERNAME=""
export IG_SERVICE_PASSWORD=""
export IG_SERVICE_API_KEY=""
export IG_SERVICE_ACC_TYPE="DEMO" # LIVE / DEMO
export IG_SERVICE_ACC_NUMBER=""

"""




def test_ig_service():
    pp = pprint.PrettyPrinter(indent=4)

    assert(isinstance(trading_ig.__version__, basestring))

    config = ConfigEnvVar("IG_SERVICE")
    ig_service = IGService(config.username, config.password, config.api_key, config.acc_type)
    ig_service.create_session()

    print("fetch_accounts")
    response = ig_service.fetch_accounts()
    print(response)
    #assert(response['balance'][0]['available']>0)
    assert(response['balance'][0]>0)

    print("")

    print("fetch_account_activity_by_period")
    response = ig_service.fetch_account_activity_by_period(10000)
    print(response)
    assert(isinstance(response, pd.DataFrame))

    print("")

    print("fetch_account_activity_by_period")
    response = ig_service.fetch_account_activity_by_period(10000)
    print(response)
    assert(isinstance(response, pd.DataFrame))

    print("")

    print("fetch_transaction_history_by_type_and_period")
    response = ig_service.fetch_transaction_history_by_type_and_period(10000, "ALL")
    print(response)
    assert(isinstance(response, pd.DataFrame))

    print("")

    print("fetch_open_positions")
    response = ig_service.fetch_open_positions()
    print(response)
    assert(isinstance(response, pd.DataFrame))

    print("")

    print("fetch_working_orders")
    response = ig_service.fetch_working_orders()
    print(response)
    assert(isinstance(response, pd.DataFrame))

    print("")

    print("fetch_top_level_navigation_nodes")
    response = ig_service.fetch_top_level_navigation_nodes()
    print(response) # dict with nodes and markets
    assert(isinstance(response, dict))
    market_id = response['nodes']['id'].iloc[0]

    print("")

    print("fetch_client_sentiment_by_instrument")
    response = ig_service.fetch_client_sentiment_by_instrument(market_id)
    print(response)
    assert(isinstance(response, dict))

    print("")

    print("fetch_related_client_sentiment_by_instrument")
    response = ig_service.fetch_related_client_sentiment_by_instrument(market_id)
    print(response)
    assert(isinstance(response, pd.DataFrame))

    print("")

    print("fetch_sub_nodes_by_node")
    node = market_id #?
    response = ig_service.fetch_sub_nodes_by_node(node)
    print(response)
    assert(isinstance(response['markets'], pd.DataFrame))
    assert(isinstance(response['nodes'], pd.DataFrame))

    print("")

    print("fetch_all_watchlists")
    response = ig_service.fetch_all_watchlists()
    print(response)
    assert(isinstance(response, pd.DataFrame))
    watchlist_id = response['id'].iloc[0] # u'Popular Markets'
    #epic = 

    print("")

    print("fetch_watchlist_markets")
    response = ig_service.fetch_watchlist_markets(watchlist_id)
    print(response)
    assert(isinstance(response, pd.DataFrame))
    epic = response['epic'].iloc[0] # epic = 'CS.D.EURUSD.MINI.IP' # epic = u'IX.D.CAC.IDF.IP'

    print("")

    print("fetch_market_by_epic")
    response = ig_service.fetch_market_by_epic(epic)
    print(response)
    #pp.pprint(response)
    assert(isinstance(response, dict))

    print("")

    print("search_markets")
    search_term = 'EURUSD'
    response = ig_service.search_markets(search_term)
    print(response)
    assert(isinstance(response, pd.DataFrame))

    print("")

    print("fetch_historical_prices_by_epic_and_num_points")

    #epic = 'CS.D.EURUSD.MINI.IP'
    #resolution = 'HOUR' # MINUTE, MINUTE_2, MINUTE_3, MINUTE_5, MINUTE_10, MINUTE_15, MINUTE_30, HOUR, HOUR_2, HOUR_3, HOUR_4, DAY, WEEK, MONTH
    resolution = 'H' # http://pandas.pydata.org/pandas-docs/stable/timeseries.html#dateoffset-objects
    num_points = 10
    response = ig_service.fetch_historical_prices_by_epic_and_num_points(epic, resolution, num_points)
    print(response)
    #print(response['prices']['price'])
    #print(response['prices']['price']['ask'])
    #print(response['prices']['volume'])
    assert(isinstance(response['allowance'], dict))
    #assert(isinstance(response['prices']['volume'], pd.Series))
    #assert(isinstance(response['prices']['price'], pd.Panel))
    assert(isinstance(response['prices'], pd.DataFrame))

    print("")

    print("fetch_historical_prices_by_epic_and_date_range")
    start_date = datetime.datetime(2014, 12, 15)
    end_date = datetime.datetime(2014, 12, 20)
    response = ig_service.fetch_historical_prices_by_epic_and_date_range(epic, resolution, start_date, end_date)
    print(response)
    assert(isinstance(response['allowance'], dict))
    #assert(isinstance(response['prices']['volume'], pd.Series))
    #assert(isinstance(response['prices']['price'], pd.Panel))
    assert(isinstance(response['prices'], pd.DataFrame))
