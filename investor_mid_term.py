import numpy as np
import matplotlib.pyplot as plt
from engine import run_simulation

simulations = 30000
years = 25
yearly_investment = 100000

war_results, stable_results = run_simulation(simulations, years, yearly_investment)

total_invested = yearly_investment * years

war_profits = war_results - total_invested
stable_profits = stable_results - total_invested

print("\n===== MID TERM INVESTOR =====")
print("Total invested:", total_invested)

print("\n--- WAR SCENARIO ---")
print("Median portfolio:", int(np.median(war_results)))
print("Average portfolio:", int(np.mean(war_results)))
print("Median profit:", int(np.median(war_profits)))
print("Average profit:", int(np.mean(war_profits)))
print("Worst outcome:", int(np.min(war_results)))
print("Best outcome:", int(np.max(war_results)))

print("\n--- NO WAR SCENARIO ---")
print("Median portfolio:", int(np.median(stable_results)))
print("Average portfolio:", int(np.mean(stable_results)))
print("Median profit:", int(np.median(stable_profits)))
print("Average profit:", int(np.mean(stable_profits)))
print("Worst outcome:", int(np.min(stable_results)))
print("Best outcome:", int(np.max(stable_results)))

plt.figure(figsize=(12,8))

# WAR distribution
plt.subplot(2,1,1)
plt.hist(war_results, bins=70, alpha=0.8)
plt.axvline(np.median(war_results), linestyle="--", label="Median")
plt.axvline(np.percentile(war_results,10), linestyle=":", label="10th percentile")

plt.title("WAR Scenario Distribution")
plt.xlabel("Final Portfolio Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(alpha=0.3)

# STABLE distribution
plt.subplot(2,1,2)
plt.hist(stable_results, bins=70, alpha=0.8)
plt.axvline(np.median(stable_results), linestyle="--", label="Median")
plt.axvline(np.percentile(stable_results,10), linestyle=":", label="10th percentile")

plt.title("NO WAR Scenario Distribution")
plt.xlabel("Final Portfolio Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()