# My son recently started collecting Riddler League football cards and informed
# me that he planned on acquiring every card in the set. It made me wonder,
# naturally, how much of his allowance he would have to spend in order to achieve
# his goal. His favorite set of cards is Riddler Silver; a set consisting of 100
# cards, numbered 1 to 100. The cards are only sold in packs containing 10 random
# cards, without duplicates, with every card number having an equal chance of
# being in a pack.
#
# Each pack can be purchased for $1. If his allowance is $10 a week, how long
# would we expect it to take before he has the entire set?
#
# What if he decides to collect the more expansive Riddler Gold set, which has
# 300 different cards?

import random

#Generate the complete list
complete_list = list(range(1 ,101))

#Create a list of your simulation results
sim_results = []

num_sims = int(input("Enter number of simulations to run:"))

def run_sim():
    draws = 0

    current_list = []

    while set(current_list) != set(complete_list):
        new_list = current_list + list(set(random.sample(complete_list, 10)) - set(current_list))
        current_list = new_list
        draws += 1

    sim_results.append(draws)

sim_counter = 1

while sim_counter < num_sims:
    print("Running sim number:", sim_counter)
    run_sim()
    sim_counter += 1

print("Here is the average number of draws required: ",sum(sim_results)/len(sim_results))
