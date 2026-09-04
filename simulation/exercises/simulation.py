import simpy
import random

# datos de entrada que consegui en el trabajo de campo

# avg time service = 2.1 min per customer (33 min * 2 cashiers) / 31 customers
# time between group arrivals (min) = [3, 1, 1, 2, 1, 4, 3, 11] -> avg = 3.25 min
# group sizes observed = [5, 4, 2, 2, 3, 3, 6, 3, 2]

MEAN_SERVICE_TIME = 2.1  # minutos, sacado de 66 / 31
MEAN_INTERARRIVAL_TIME = 3.25  # minutos, sacado de 26 / 8
GROUP_SIZES = [5, 4, 2, 2, 3, 3, 6, 3, 2]

waiting_times = []


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

        service_time = random.expovariate(1 / MEAN_SERVICE_TIME)

        yield env.timeout(service_time)

        print(f"{env.now:.2f} - " f"Customer {id_customer} leaves")


def customer_generator(env, cashier):

    id_customer = 1

    while True:

        interarrival_time = random.expovariate(1 / MEAN_INTERARRIVAL_TIME)

        yield env.timeout(interarrival_time)

        group_size = random.choice(GROUP_SIZES)

        for _ in range(group_size):
            env.process(customer(env, id_customer, cashier))
            id_customer += 1


print("### Simulacion de caffeteria (datos reales de observacion) ###")
print(f"Tiempo promedio de servicio: {MEAN_SERVICE_TIME} min")
print(f"Tiempo promedio entre llegadas de grupos: {MEAN_INTERARRIVAL_TIME} min")
print(f"Tamanos de grupos observados: {GROUP_SIZES}")
print()

capacity = int(input("Cuantas cajas quieres simular? (1, 2, 3): "))
sim_time = float(input("Duracion de la simulacion en minutos: "))
print()

env = simpy.Environment()
cashier = simpy.Resource(env, capacity)

env.process(customer_generator(env, cashier))
env.run(until=sim_time)

print()
if waiting_times:
    average_waiting_time = sum(waiting_times) / len(waiting_times)
    maximum_waiting_time = max(waiting_times)

    print(f"Clientes atendidos: {len(waiting_times)}")
    print(f"Average waiting time: {average_waiting_time:.2f} minutes")
    print(f"Maximum waiting time: {maximum_waiting_time:.2f} minutes")
else:
    print("No llegaron clientes en el tiempo simulado.")
