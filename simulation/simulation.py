import simpy
import random

# avg time service = 2.1 min per customer (33 min * 2 cashier) / 31 customers
# time groups arrives [3, 1, 1, 2, 1, 4, 3, 11] min -> avg = 3.25 min
# groups size = [5, 4, 2, 2, 3, 3, 6, 3, 2]

SIMULATION_TIME = 60
CAPACITY = 2
waiting_times = []

# Parametros ajustados a los datos reales (fitted exponential)
MEAN_SERVICE_TIME = 2.1  # minutos, sacado de 66 / 31
MEAN_INTERARRIVAL_TIME = 3.25  # minutos, sacado de 26 / 8

# Tamanos de grupo observados (no son tiempos, se dejan como random.choice)
GROUP_SIZES = [5, 4, 2, 2, 3, 3, 6, 3, 2]


def customer(env, id_customer, cashier):

    arrival_time = env.now

    print(f"{arrival_time:.2f} - " f"Customer {id_customer} arrives")

    with cashier.request() as request:

        yield request

        service_start = env.now

        waiting_time = service_start - arrival_time

        waiting_times.append(waiting_time)

        print(
            f"{service_start:.2f} - "
            f"Customer {id_customer} starts service "
            f"(waited {waiting_time:.2f} min)"
        )

        # antes: random.uniform(1, 4)  -> ahora: exponencial ajustada a tus datos
        service_time = random.expovariate(1 / MEAN_SERVICE_TIME)

        yield env.timeout(service_time)

        print(f"{env.now:.2f} - " f"Customer {id_customer} leaves")


def customer_generator(env, cashier):

    id_customer = 1

    while True:

        # antes: random.expovariate(0.5) -> ahora: exponencial ajustada a tus datos
        interarrival_time = random.expovariate(1 / MEAN_INTERARRIVAL_TIME)

        yield env.timeout(interarrival_time)

        # ahora llega un GRUPO, no una sola persona
        group_size = random.choice(GROUP_SIZES)

        for _ in range(group_size):
            env.process(customer(env, id_customer, cashier))
            id_customer += 1


env = simpy.Environment()

cashier = simpy.Resource(env, CAPACITY)

env.process(customer_generator(env, cashier))

env.run(until=SIMULATION_TIME)

average_waiting_time = sum(waiting_times) / len(waiting_times)
maximum_waiting_time = max(waiting_times)

print()
print(f"Average waiting time: {average_waiting_time:.2f} minutes")
print(f"Maximum waiting time: {maximum_waiting_time:.2f} minutes")
