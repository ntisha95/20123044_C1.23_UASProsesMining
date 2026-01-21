from pm4py.objects.log.importer.xes import importer as xes_importer
import pandas as pd

# ===============================
# LOAD EVENT LOG
# ===============================
log = xes_importer.apply("data/sepsis_cases.xes")
print("Event log berhasil dimuat")

# ===============================
# HITUNG DURASI EVENT MANUAL
# ===============================
print("Menghitung durasi aktivitas secara manual...")

records = []

for trace in log:
    events = list(trace)
    for i in range(len(events) - 1):
        act = events[i]["concept:name"]
        t1 = events[i]["time:timestamp"]
        t2 = events[i + 1]["time:timestamp"]
        duration = (t2 - t1).total_seconds()

        if duration >= 0:
            records.append((act, duration))

# ===============================
# ANALISIS BOTTLENECK
# ===============================
df = pd.DataFrame(records, columns=["Aktivitas", "Durasi (detik)"])

summary = (
    df.groupby("Aktivitas")["Durasi (detik)"]
    .mean()
    .reset_index()
    .sort_values(by="Durasi (detik)", ascending=False)
)

print("\nAktivitas dengan durasi terlama (indikasi bottleneck):")
print(summary.head(5))

# Simpan hasil
summary.to_csv("results/bottleneck_activity_analysis.csv", index=False)
print("\nHasil disimpan di results/bottleneck_activity_analysis.csv")
