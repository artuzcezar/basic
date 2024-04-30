import math
def savings(employee_gross_pay, employee_tax_rate, employee_expenses):
    net_pay_after_taxes = math.floor((1 - employee_tax_rate) * employee_gross_pay)
    remaining_funds = net_pay_after_taxes - employee_expenses
    return remaining_funds

import math
def material_waste(available_material, material_unit, jobs_count, consumption_per_job):
    total_waste = available_material - (jobs_count * consumption_per_job)
    return str(total_waste) + material_unit

import math
def interest(starting_principal, interest_rate, investment_periods):
    accrued_interest = math.floor((starting_principal * interest_rate * investment_periods) + starting_principal)
    return accrued_interest
