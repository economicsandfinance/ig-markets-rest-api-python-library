#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Run unit tests using
nosetests -s -v
"""

from ig_service import IGService
from ig_service_config import * # defines username, password, api_key, acc_type, acc_number
import pandas as pd
import pprint

def test_ig_service():
    pp = pprint.PrettyPrinter(indent=4)

    ig_service = IGService(username, password, api_key, acc_type)
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

    print("")

    print("fetch_all_watchlists")
    response = ig_service.fetch_all_watchlists()
    print(response)
    watchlist_id = response['id'].iloc[0]
    #epic = 

    print("")

    print("fetch_watchlist_markets")
    response = ig_service.fetch_watchlist_markets(watchlist_id)
    print(response)
    epic = response['epic'].iloc[0] # epic = 'CS.D.EURUSD.MINI.IP'

    print("")

    print("fetch_market_by_epic")
    response = ig_service.fetch_market_by_epic(epic)
    print(response)
    #pp.pprint(response)
    #assert(isinstance(response, dict))

    print("")

    print("search_markets")
    search_term = 'UNDEF'
    response = ig_service.search_markets(epic)
    print(response)

    print("")

    print("fetch_historical_prices_by_epic_and_num_points")

    #epic = 'CS.D.EURUSD.MINI.IP'
    resolution = 'HOUR'
    num_points = 10
    response = ig_service.fetch_historical_prices_by_epic_and_num_points(epic, resolution, num_points)
    print(response['prices']['price'])
    print(response['prices']['price']['ask'])
    print(response['prices']['volume'])
    assert(isinstance(response['prices']['price'], pd.Panel))
