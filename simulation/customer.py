import simpy


def customer(env, id_customer, arrival_time, cashier):

    yield env.timeout(arrival_time)

    print(f"Customer {id_customer} arrives at t={env.now}")

    with cashier.request() as request:

        yield request

        print(f"The client {id_customer} is attended at t={env.now}")

        yield env.timeout(2)

        print(f"Customer {id_customer} leaves at t={env.now}\n")


env = simpy.Environment()

# Resourse can only be used by 1 process at time
cashier = simpy.Resource(env, capacity=1)

env.process(customer(env, 1, 0, cashier))
env.process(customer(env, 2, 1.5, cashier))
env.process(customer(env, 3, 4, cashier))

env.run()
