import simpy
import random

interarrival_times = [1, 4, 1.66, 6.2, 3.2, 2.4, 4.4, 8.3, 1.7, 5.5]

waiting_time_list = []

env = simpy.Environment()

cashier = simpy.Resource(env, 1)


def customer_generator(env, cashier):
    for i, interval in enumerate(interarrival_times):
        yield env.timeout(interval)

        env.process(customer(env, i + 1, cashier))


def customer(env, id_customer, cashier):

    print(f"Customer {id_customer} arrives at t={env.now}")
    arrival_time = env.now

    with cashier.request() as request:

        yield request

        print(f"The client {id_customer} is attended at t={env.now}")

        service_start_time = env.now

        waiting_time = service_start_time - arrival_time

        waiting_time_list.append(waiting_time)

        print(f"Customer {id_customer} waited {waiting_time} time units")

        yield env.timeout(2)

        print(f"Customer {id_customer} leaves at t={env.now}\n")


env.process(customer_generator(env, cashier))

env.run()
