import simpy
import random


def machine(env, id_machine):
    while True:
        ## process random time between 2 and 5
        time = random.randint(2, 5)
        print(f"[t={env.now}] Machine {id_machine}: " f"data processing ({time} min)")
        yield env.timeout(time)
        print(f"[t={env.now}] Machine {id_machine}: " "finished piece")


env = simpy.Environment()
env.process(machine(env, "M1"))
env.process(machine(env, "M2"))
env.run(until=20)
