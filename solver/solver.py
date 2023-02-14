from ortools.linear_solver import pywraplp
import numpy as np

# data
variables = [
    {
        'id': 0,
        'name': 'np',
        'type': 'INTEGER',
        'domain_type': 'INTERVAL',
        'domain_value': [1, 100]

    },
    {
        'id': 1,
        'name': 'nb',
        'type': 'INTEGER',
        'domain_type': 'INTERVAL',
        'domain_value': [1, 100]

    },
    {
        'id': 2,
        'name': 'nc',
        'type': 'INTEGER',
        'domain_type': 'INTERVAL',
        'domain_value': [1, 100]

    }
]

constraints = [
    {
        'coefficient': [1],
        'operators': [],
        'metric': '>=',
        'value': 1,
        'variable_id': [0]
    },
    {
        'coefficient': [1],
        'operators': [],
        'metric': '>=',
        'value': 1,
        'variable_id': [1]
    },
    {
        'coefficient': [1],
        'operators': [],
        'metric': '>=',
        'value': 1,
        'variable_id': [2]
    },
    {
        'coefficient': [1, 1, 1],
        'operators': ['+', '+'],
        'metric': '==',
        'value': 100,
        'variable_id': [0, 1, 2]
    },
    {
        'coefficient': [5, 15, 25],
        'operators': ['+', '+'],
        'metric': '<=',
        'value': 100,
        'variable_id': [0, 1, 2]
    }
]


def main(variables, constraints):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    all_variables = []
    for var in variables:
        if (var["type"] == "INTEGER"):
            if (var["domain_type"] == "INTERVAL"):
                first = np.NINF if var["domain_value"][0] == "-" else float(var["domain_value"][0])
                last = np.Inf if var["domain_value"][1] == "-" else float(var["domain_value"][1])
                all_variables.append(solver.IntVar(first, last, var["name"]))
            else:
                pass
        else:
            pass

    for ct in constraints:
        if (len(ct["coefficient"]) > 1):
            add_constraint(ct, solver, all_variables)
        else:
            add_constraint_unique_var(ct, solver, all_variables)
    return solver, all_variables


def add_constraint_unique_var(ct, solver, all_variables):
    # For python 3.10
    #     match ct["metric"]:
    #         case "<=":
    #             solver.Add(float(ct.coefficient) * all_variables[int(ct.variable_id)] <= float(ct.value))
    #         case ">=":
    #             solver.Add(float(ct.coefficient) * all_variables[int(ct.variable_id)] >= float(ct.value))
    #         case "<":
    #             solver.Add(float(ct.coefficient) * all_variables[int(ct.variable_id)] < float(ct.value))
    #         case ">":
    #             solver.Add(float(ct.coefficient) * all_variables[int(ct.variable_id)] > float(ct.value))
    #         case "!=":
    #             solver.Add(float(ct.coefficient) * all_variables[int(ct.variable_id)] != float(ct.value))
    #         case "==":
    #             solver.Add(float(ct.coefficient) * all_variables[int(ct.variable_id)] == float(ct.value))

    if ct["metric"] == "<=":
        solver.Add(float(ct["coefficient"][0]) * all_variables[int(ct["variable_id"][0])] <= float(ct["value"]))
    elif ct["metric"] == ">=":
        solver.Add(float(ct["coefficient"][0]) * all_variables[int(ct["variable_id"][0])] >= float(ct["value"]))
    elif ct["metric"] == "<":
        solver.Add(float(ct["coefficient"][0]) * all_variables[int(ct["variable_id"][0])] < float(ct["value"]))
    elif ct["metric"] == ">":
        solver.Add(float(ct["coefficient"][0]) * all_variables[int(ct["variable_id"][0])] > float(ct["value"]))
    elif ct["metric"] == "!=":
        solver.Add(float(ct["coefficient"][0]) * all_variables[int(ct["variable_id"][0])] != float(ct["value"]))
    elif ct["metric"] == "==":
        solver.Add(float(ct["coefficient"][0]) * all_variables[int(ct["variable_id"][0])] == float(ct["value"]))
    else:
        pass


def add_constraint(ct, solver, all_variables):
    exp = ct["coefficient"][0] * all_variables[0]
    for i in range(len(ct["operators"])):
        if ct["operators"][i] == "+":
            exp = exp + ct["coefficient"][i + 1] * all_variables[i + 1]
        elif ct["operators"][i] == "-":
            exp = exp - ct["coefficient"][i + 1] * all_variables[i + 1]
        elif ct["operators"][i] == "*":
            exp = exp * ct["coefficient"][i + 1] * all_variables[i + 1]
        elif ct["operators"][i] == "/":
            exp = exp / ct["coefficient"][i + 1] * all_variables[i + 1]
        elif ct["operators"][i] == "%":
            exp = exp % ct["coefficient"][i + 1] * all_variables[i + 1]
        else:
            pass

    if ct["metric"] == "<=":
        solver.Add(exp <= float(ct["value"]))
    elif ct["metric"] == ">=":
        solver.Add(exp >= float(ct["value"]))
    elif ct["metric"] == "<":
        solver.Add(exp < float(ct["value"]))
    elif ct["metric"] == ">":
        solver.Add(exp > float(ct["value"]))
    elif ct["metric"] == "!=":
        solver.Add(exp != float(ct["value"]))
    elif ct["metric"] == "==":
        solver.Add(exp == float(ct["value"]))
    else:
        pass

# solver, all_variables = main(variables, constraints)
# status = solver.Solve()
# print(status)
# print('Number of constraints =', solver.NumConstraints())
# print('Number of variables =', solver.NumVariables())
# print('Problem solved in %f milliseconds' % solver.wall_time())
# print('Problem solved in %d iterations' % solver.iterations())
# print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
#
# for var in all_variables:
#     print(var.solution_value())
