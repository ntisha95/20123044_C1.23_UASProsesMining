from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter as pt_converter
from pm4py.algo.conformance.alignments.petri_net import algorithm as alignments

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
print("Model Petri Net siap untuk conformance checking")

# ===============================
# CONFORMANCE CHECKING (ALIGNMENT)
# ===============================
print("Menjalankan conformance checking (alignment)...")

aligned_traces = alignments.apply_log(
    log,
    net,
    initial_marking,
    final_marking
)

# ===============================
# FITNESS CALCULATION
# ===============================
fitness_values = [
    align["fitness"] for align in aligned_traces if "fitness" in align
]

average_fitness = sum(fitness_values) / len(fitness_values)

print("Jumlah trace:", len(aligned_traces))
print("Rata-rata fitness:", round(average_fitness, 4))
