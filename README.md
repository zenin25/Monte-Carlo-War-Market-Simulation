# Monte-Carlo-War-Market-Simulation
A Monte Carlo simulation that models how long-term investments behave under war vs stable market conditions.



---

## 🧠 Overview

This project explores how **long-term investment outcomes are affected by geopolitical instability**, using **Monte Carlo simulation**.

The model compares two market environments:

* ⚔️ **War-driven market** → shock, high volatility, gradual recovery
* 📊 **Stable market** → consistent growth, lower volatility

The goal is to understand how **time horizon + uncertainty** shape long-term wealth.

---

## 👤 Investor Types Simulated

Three types of investors are modeled:
All three "investors" invest a similar capital over time which is about 2.5 Million.
### 🟢 Long-Term Investor

* 40-year horizon
* Moderate yearly investment
* Maximum compounding exposure

### 🟡 Mid-Term Investor

* 25-year horizon
* Higher yearly investment
* Balanced compounding

### 🔴 Short-Term / Distracted Investor

* 9-year horizon
* High yearly investment
* Limited compounding

---

## 🎯 Scientific Goal

> **How does market instability affect long-term wealth creation across different investment horizons?**

To answer this, we simulate two scenarios:

---

### ⚔️ War Scenario

Market evolves through:

* Initial shock (negative returns)
* High-volatility phase
* Recovery period
* Long-term stabilization

---

### 📊 No-War Scenario

Market behavior:

* Stable growth
* Lower volatility
* Consistent compounding

---

## 📊 Metrics Computed

For each simulation:

* 💰 Final portfolio value
* 📥 Total invested capital
* 📈 Profit generated
* 📉 Distribution of outcomes

---

## 🔍 Analysis Performed

* Median vs Average outcomes
* Best & Worst-case scenarios
* Risk (spread of outcomes)
* Impact of time horizon on resilience

---

## 💡 Key Insights Explored

* Does volatility increase returns or just uncertainty?
* How much does war affect long-term investing?
* Can compounding overcome instability?
* How does time horizon change outcomes?

---

## 📁 Project Structure

### `engine.py`

Core simulation engine. This file holds the logic for the market.

**Features:**

* Runs Monte Carlo simulations
* Models multiple market regimes:

  * Shock
  * Volatility
  * Recovery
  * Stability
* Applies realistic return constraints
* Outputs final portfolio values

---

### `long_term_investor.py`

Simulates a disciplined long-term investor.

**Focus:**

* Resilience to volatility
* Wealth accumulation via compounding

---

### `mid_term_investor.py`

Simulates a balanced investor.

**Focus:**

* Trade-off between time and capital

---

### `short_term_investor.py`

Simulates a short-term or inconsistent investor.

**Focus:**

* Sensitivity to volatility
* Downside risk

---

## ⚙️ Methodology

The simulation uses:

* 🎲 **Monte Carlo Sampling** → thousands of possible futures
* 📉 **Normal distributions** for returns


Each run represents a **possible financial future**, not a prediction.

---

## 📈 Results & Interpretation

The simulation produces:

* Distribution plots of outcomes
* War vs Stable market comparisons
* Statistical summaries:

  * Median
  * Average
  * Best / Worst cases

---

### 🧠 Typical Observations

* War increases **variance**, not necessarily returns
* Long-term investors are **more resilient**
* Short-term investors face **higher downside risk**
* **Compounding dominates** over long horizons

---

## 🧩 Concepts Used

* Monte Carlo Simulation
* Compounding
* Volatility & Risk Modeling
* Scenario-Based Financial Analysis

---

## 🛠️ Technologies Used

* Python
* NumPy
* Matplotlib

---

## 👨‍💻 Author

**Siddharth S**


