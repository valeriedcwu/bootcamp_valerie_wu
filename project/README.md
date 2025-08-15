# Price a commodity storage contract
**Stage:** Problem Framing & Scoping (Stage 01)
## Problem Statement

We aim to create a prototype model that prices nature gas storage contracts by summing all cash inflows/outflows (buys, sells, storage rent, and injection/withdrawal fees) under physical constraints (rates and capacity). The output should be fast enough for trader exploration and clear enough for validation to move toward production.
## Stakeholder & User
- **Stakeholder:** the commodity trading desk  
- **End User:** traders or sales during client discusstions (clients could be anyone who would fall within the commodities supply chain, such as producers, refiners, transporters, and distributors.)  
- **Timing:** interactive “what-if” use at the desk pre-trade; later embedded into quoting tools. It could also run on daily forward curves or user-selected prices.

## Useful Answer & Decision
- **Type:** descriptive valuation with simple scenario analysis  
- **Metric:** estimated contract **Value ($)** = proceeds from withdrawals − cost of injections − storage rent − inject/withdraw fees − transport (if any; here assumed 0)
- **Artifact:** a pricing function with docstring and tests
## Assumptions & Constraints
- **Market:** Zero interest rates; ignore weekends/holidays; no transport delays.  
- **Ops:** Injection/withdrawal rates respected per date; inventory never <0 or >capacity.
## Known Unknowns / Risks
- **Price basis/locations:** Using a single price series may ignore locational/basis risk; document source.   
- **Operational outages:** Unplanned facility downtime not modeled.  
- **Edge cases:** Negative prices, extreme volatility, overlapping/unsorted dates.
## Lifecycle Mapping
Goal → Stage → Deliverable
- Define scope & users → **Problem Framing & Scoping (Stage 01)** → README + stakeholder memo
- Preprocess historical data → **Data Preprocessing (Stage 02)** → Cleaned dataset + data dictionary
- Explore and analyze data → **Exploratory Data Analysis (Stage 03)** → EDA notebook
- Prototype pricing → **Modeling (Stage 04)** → price_storage_contract + tests + example notebook
- Validate & harden → **Validation (Stage 05)** → Test matrix, stress results, documentation
- Integrate & monitor → **Productionization (Stage 06)** → CLI/API wrapper, logging, basic dashboards
## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates

## Disclosure
This project is derived from the Forage x JPM's job simulation.