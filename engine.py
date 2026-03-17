import numpy as np

def run_simulation(simulations, years, yearly_investment):

    war_results = []
    stable_results = []

    for s in range(simulations):

        # ----- WAR SCENARIO -----
        portfolio = 0

        for year in range(years):

            if year < 1:
                mean = -0.15
                vol = 0.25
            elif year < 4:
                mean = 0.035
                vol = 0.22
            elif year < 10:
                mean = 0.075
                vol = 0.18
            else:
                mean = 0.07
                vol = 0.11

            r = np.random.normal(mean, vol)
            r = np.clip(r, -0.50, 0.45)

            portfolio *= (1 + r)
            portfolio += yearly_investment

        war_results.append(portfolio)

        # ----- NO WAR SCENARIO -----
        portfolio = 0

        for year in range(years):

            mean = 0.075
            vol = 0.08

            r = np.random.normal(mean, vol)
            r = np.clip(r, -0.35, 0.30)

            portfolio *= (1 + r)
            portfolio += yearly_investment

        stable_results.append(portfolio)

    return np.array(war_results), np.array(stable_results)