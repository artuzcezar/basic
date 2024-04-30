
def savings(employee_gross_pay, employee_tax_rate, employee_expenses):
    import math
    net_pay_after_taxes = math.floor((1 - employee_tax_rate) * employee_gross_pay)
    remaining_funds = net_pay_after_taxes - employee_expenses
    return remaining_funds


def material_waste(available_material, material_unit, jobs_count, consumption_per_job):
    import math
    total_waste = available_material - (jobs_count * consumption_per_job)
    return str(total_waste) + material_unit


def interest(starting_principal, interest_rate, investment_periods):
    import math
    accrued_interest = math.floor((starting_principal * interest_rate * investment_periods) + starting_principal)
    return accrued_interest
