from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

cpd_intelligence = TabularCPD(variable='Intelligence', variable_card=2, values=[[0.7], [0.3]])
cpd_study = TabularCPD(variable='StudyHours', variable_card=2, values=[[0.6], [0.4]])
cpd_difficulty = TabularCPD(variable='Difficulty', variable_card=2, values=[[0.4], [0.6]])

cpd_grade = TabularCPD(
    variable='Grade', variable_card=3,
    values=[
        [0.9, 0.7, 0.6, 0.8, 0.6, 0.5, 0.7, 0.4],
        [0.08, 0.2, 0.3, 0.15, 0.3, 0.3, 0.2, 0.3],
        [0.02, 0.1, 0.1, 0.05, 0.1, 0.2, 0.1, 0.3]
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2]
)

cpd_pass = TabularCPD(
    variable='Pass', variable_card=2,
    values=[
        [0.95, 0.8, 0.5],
        [0.05, 0.2, 0.5]
    ],
    evidence=['Grade'],
    evidence_card=[3]
)

model.add_cpds(cpd_intelligence, cpd_study, cpd_difficulty, cpd_grade, cpd_pass)
infer = VariableElimination(model)

q1 = infer.query(variables=['Pass'], evidence={'StudyHours': 0, 'Difficulty': 0})
q2 = infer.query(variables=['Intelligence'], evidence={'Pass': 0})

print(q1)
print(q2)
