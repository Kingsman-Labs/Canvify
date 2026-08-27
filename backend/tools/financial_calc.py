"""Deterministic financial formulas — break-even, CAC:LTV, burn rate, NPV.
Used by Financial Analysis Agent and double-checked by Validation Agent."""


def break_even_month(fixed_costs, monthly_revenue, monthly_expenses):
    # TODO: implement break-even calculation
    pass


def ltv_cac_ratio(ltv, cac):
    return ltv / cac if cac else 0
