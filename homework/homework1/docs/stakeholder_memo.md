# Stakeholder Memo – Natural Gas Storage Contract Pricing Prototype

## Context
The client anticipates a colder-than-average winter and wants to explore storage strategies: buying natural gas now at low summer prices, injecting into storage, and withdrawing in winter to sell at higher prices. They require a quick, defensible pricing tool to evaluate contract terms under various scenarios.

## Why It Matters
A reliable valuation function will:
- enable traders to quote competitive but profitable terms to the client
- allow quick “what-if” analysis of injection/withdrawal schedules and volumes
- support future automation in the desk’s pricing workflows

## Scope & Deliverable
- **Prototype**: a function that calculates net contract value given prices, volumes, fees, and physical constraints
- **Out of scope**: stochastic modeling, interest rate effects, and location/basis adjustments

## Stakeholders
- **Primary decision-maker**: VP of the commodity trading desk  
- **Users**: natural gas traders & sales team
- **Partners**: Risk, Model Validation, Engineering
- **Timeline**: prototype for desk testing within 2 weeks

## Success Criteria
- Correctly accounts for injection/withdrawal rates, capacity limits, storage rent, and per-unit fees
- Clear and auditable for review by Risk and Model Validation

## Next Steps
1. Finalize assumptions with desk and risk team
2. Implement and test function with sample scenarios
3. Package for trader use in exploratory phase