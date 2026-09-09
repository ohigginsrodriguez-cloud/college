import random
import simpy
import statistics


def market(env, prices_hist, initial_price=100, volatility=0.02):
    """Simpy process: each minute, the price may get up or get down randomly"""
    price = initial_price
    while True:
        change = random.gauss(0, volatility)  # random variation (mean 0)
        price = price * (1 + change)
        prices_hist.append(price)
        yield env.timeout(1)


def trader(env, prices_hist, result):
    """Simpy process: each minute check the price and decides"""
    capital = 1000.0
    accions = 0

    while True:
        yield env.timeout(1)  # wait till new price show up

        if len(prices_hist) < 3:
            continue  # have not hist enough to decide

        actual_price = prices_hist[-1]
        previous_price = prices_hist[-2]
        price_2_ago = prices_hist[-3]

        # simple strategy: if price get up 2 consecutive times = buy
        if actual_price > previous_price > price_2_ago and accions == 0:
            accions = capital / actual_price
            capital = 0

        # if get dowm 2 consecutive times, sell
        elif actual_price < previous_price < price_2_ago and accions > 0:
            capital = accions * actual_price
            accions = 0

    # this while True never ends by his own; simpy cut it when env.run ends
