from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter as pt_converter
from pm4py.visualization.petri_net import visualizer as pn_visualizer

# ===============================
# LOAD EVENT LOG
# ===============================
log = xes_importer.apply("data/sepsis_cases.xes")
print("Event log berhasil dimuat")

# ===============================
# PROCESS DISCOVERY
# ===============================
print("Menjalankan Inductive Miner...")
process_tree = inductive_miner.apply(log)
print("Process Tree berhasil dibuat")

# ===============================
# CONVERT TO PETRI NET
# ===============================
net, initial_marking, final_marking = pt_converter.apply(process_tree)
print("Petri Net berhasil dikonversi")

# ===============================
# VISUALIZATION
# ===============================
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.save(gviz, "results/process_model.png")

print("Model proses berhasil disimpan di folder results/")
