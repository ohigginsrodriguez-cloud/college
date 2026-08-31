import simpy
import random

# -------------------------
# Parameters
# -------------------------

SIMULATION_TIME = 120  # minutes

ARRIVAL_RATE = 20 / 60  # 20 customers per hour

MIN_SERVICE_TIME = 1
MAX_SERVICE_TIME = 4


# -------------------------
# Statistics
# -------------------------

waiting_time_list = []


# -------------------------
# Customer
# -------------------------


def customer(env, id_customer, cashier):

    arrival_time = env.now

    print(f"Customer {id_customer} arrives " f"at t={arrival_time:.2f}")

    with cashier.request() as request:

        yield request

        service_start_time = env.now

        waiting_time = service_start_time - arrival_time

        waiting_time_list.append(waiting_time)

        print(
            f"Customer {id_customer} is attended "
            f"at t={service_start_time:.2f} "
            f"(waited {waiting_time:.2f})"
        )

        service_time = random.uniform(MIN_SERVICE_TIME, MAX_SERVICE_TIME)

        yield env.timeout(service_time)

        print(f"Customer {id_customer} leaves " f"at t={env.now:.2f}\n")


# -------------------------
# Customer generator
# -------------------------


def customer_generator(env, cashier):

    customer_id = 1

    while True:

        interarrival_time = random.expovariate(ARRIVAL_RATE)

        yield env.timeout(interarrival_time)

        env.process(customer(env, customer_id, cashier))

        customer_id += 1


# -------------------------
# Simulation
# -------------------------

env = simpy.Environment()

cashier = simpy.Resource(env, capacity=2)

env.process(customer_generator(env, cashier))

env.run(until=SIMULATION_TIME)


# -------------------------
# Results
# -------------------------

total_waiting_time = sum(waiting_time_list)

average_waiting_time = total_waiting_time / len(waiting_time_list)

print("--------------------------------")
print("Simulation results")
print("--------------------------------")
print(f"Customers: {len(waiting_time_list)}")
print(f"Average waiting time: {average_waiting_time:.2f}")
print(f"Maximum waiting time: {max(waiting_time_list):.2f}")
