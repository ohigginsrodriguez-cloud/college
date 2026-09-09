import random
import simpy
import statistics


def market(env, prices_hist, initial_price=100, volatility=0.02):
    """Simpy process: each minute, the price may get up or get down randomly"""
    price = initial_price
    prices_hist.append(price)  # save the initial price too
    while True:
        change = random.gauss(0, volatility)  # random variation (mean 0)
        price = price * (1 + change)
        prices_hist.append(price)
        yield env.timeout(1)


def trader(env, prices_hist, result):
    """Simpy process: each minute check the price and decides"""
    # using a dict instead of normal variables, so the values dont get lost
    # when simpy cuts the process (capital/accions were dying inside the function)
    result["capital"] = 1000.0
    result["accions"] = 0.0

    while True:
        yield env.timeout(1)  # wait till new price show up

        if len(prices_hist) < 3:
            continue  # have not hist enough to decide

        actual_price = prices_hist[-1]
        previous_price = prices_hist[-2]
        price_2_ago = prices_hist[-3]

        # simple strategy: if price get up 2 consecutive times = buy
        if actual_price > previous_price > price_2_ago and result["accions"] == 0:
            result["accions"] = result["capital"] / actual_price
            result["capital"] = 0.0

        # if get dowm 2 consecutive times, sell
        elif actual_price < previous_price < price_2_ago and result["accions"] > 0:
            result["capital"] = result["accions"] * actual_price
            result["accions"] = 0.0

    # this while True never ends by his own; simpy cut it when env.run ends


def run_simulation(seed, minutes=200):
    """runs ONE simulation and returns the % return of that run"""
    random.seed(seed)
    env = simpy.Environment()

    prices_hist = []
    result = {}

    env.process(market(env, prices_hist))
    env.process(trader(env, prices_hist, result))
    env.run(until=minutes)

    # if it ended with accions (never sold), value them at the last price
    final_price = prices_hist[-1]
    final_value = result["capital"] + result["accions"] * final_price
    return_pct = (final_value - 1000.0) / 1000.0 * 100

    return return_pct


# monte carlo: repeat the whole run many times
NUM_RUNS = 300
results = []

for run in range(NUM_RUNS):
    ret = run_simulation(seed=run)
    results.append(ret)

# final stats
mean_return = statistics.mean(results)
std_dev = statistics.stdev(results)
standard_error = std_dev / (NUM_RUNS**0.5)
worst_5pct = statistics.quantiles(results, n=20)[0]  # approx 5% percentile

print(f"Monte carlo runs: {NUM_RUNS}")
print(f"Average return: {mean_return:.2f}%")
print(f"Standard deviation (risk): {std_dev:.2f}%")
print(f"Standard error of the estimation: {standard_error:.4f}%")
print(f"Approx VaR (worst 5% scenarios): {worst_5pct:.2f}%")
