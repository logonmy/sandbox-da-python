from pgmpy.models import BayesianModel
from pgmpy.inference import ClusterBeliefPropagation as CBP
from pgmpy.factors import TabularCPD
restaurant_model = BayesianModel([('location', 'cost'),
                                  ('quality', 'cost'),
                                  ('location', 'no_of_people'),
                                  ('cost', 'no_of_people')])
cpd_location = TabularCPD('location', 2, [[0.6, 0.4]])
cpd_quality = TabularCPD('quality', 3, [[0.3, 0.5, 0.2]])
cpd_cost = TabularCPD('cost', 2,
                      [[0.8, 0.6, 0.1, 0.6, 0.6, 0.05],
                       [0.2, 0.1, 0.9, 0.4, 0.4, 0.95]],
                      ['location', 'quality'], [2, 3])
cpd_no_of_people = TabularCPD('no_of_people', 2,
                              [[0.6, 0.8, 0.1, 0.6],
                               [0.4, 0.2, 0.9, 0.4]],
                              ['cost', 'location'], [2, 2])
restaurant_model.add_cpds(cpd_location, cpd_quality,
                          cpd_cost, cpd_no_of_people)
cluster_inference = CBP(restaurant_model)
cluster_inference.query(variables=['cost'])
cluster_inference.query(variables=['cost'],
                        evidence={'no_of_people': 1, 'quality': 0})