import simpy

# 'Enviroment' = simulation time
env = simpy.Environment()


# we can visualize the time usin 'now'
print(env.now)

# we can wait time using 'timeout'
env.timeout(5)
# this make a event but dont make wait the program yet


# to make wait a process we do:
# yield env.timeout(5)


# Process happen while the simulation
# customer arrives and stay 5 minutes in the system
def customer(env):

    print(f"Customer arrives {env.now}")

    yield env.timeout(5)

    print(f"Customer leaves {env.now}")


# we have a fcuntion representing customer behaivior
# but it's not yet executed
# we gotta convert it into a process
env.process(customer(env))


# finally we execute the simulation
env.run()
