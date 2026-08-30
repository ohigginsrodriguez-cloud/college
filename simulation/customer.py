import simpy


def customer(env):

    print(f"Customer arrives at t={env.now}")

    yield env.timeout(5)

    print(f"Customer leaves at t={env.now}")


env = simpy.Environment()

env.process(customer(env))

env.run()
