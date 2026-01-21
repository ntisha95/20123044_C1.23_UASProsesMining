from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter as pt_converter
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator

# ===============================
# LOAD EVENT LOG
# ===============================
log = xes_importer.apply("data/sepsis_cases.xes")
print("Event log berhasil dimuat")

# ===============================
# PROCESS DISCOVERY
# ===============================
process_tree = inductive_miner.apply(log)
net, initial_marking, final_marking = pt_converter.apply(process_tree)
print("Model Petri Net siap untuk evaluasi precision")

# ===============================
# PRECISION CALCULATION
# ===============================
precision = precision_evaluator.apply(
    log,
    net,
    initial_marking,
    final_marking
)

print("Nilai Precision:", round(precision, 4))
