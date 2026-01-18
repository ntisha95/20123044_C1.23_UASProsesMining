from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.statistics.attributes.log import get as attr_get
from pm4py.statistics.start_activities.log import get as start_activities
from pm4py.statistics.end_activities.log import get as end_activities
from pm4py.statistics.traces.generic.log import case_statistics
import matplotlib.pyplot as plt

# ===============================
# LOAD EVENT LOG
# ===============================
log = xes_importer.apply("data/sepsis_cases.xes")
print("Event log berhasil dimuat")

# ===============================
# BASIC STATISTICS
# ===============================
num_cases = len(log)
num_events = sum(len(trace) for trace in log)
activities = attr_get.get_attribute_values(log, "concept:name")
num_activities = len(activities)

print("Jumlah kasus:", num_cases)
print("Jumlah event:", num_events)
print("Jumlah aktivitas:", num_activities)

# ===============================
# CASE DURATION
# ===============================
case_durations = case_statistics.get_all_case_durations(log)
avg_duration = sum(case_durations) / len(case_durations)
print("Rata-rata durasi proses (detik):", round(avg_duration, 2))

# ===============================
# MOST FREQUENT ACTIVITIES
# ===============================
sorted_activities = sorted(activities.items(), key=lambda x: x[1], reverse=True)

print("\nAktivitas paling sering:")
for act, freq in sorted_activities[:5]:
    print(f"{act}: {freq}")

# ===============================
# START & END ACTIVITIES (FIXED)
# ===============================
start_act = start_activities.get_start_activities(log)
end_act = end_activities.get_end_activities(log)

print("\nAktivitas awal dominan:")
print(start_act)

print("\nAktivitas akhir dominan:")
print(end_act)

# ===============================
# VISUALIZATION
# ===============================
plt.figure(figsize=(10, 5))
plt.bar(activities.keys(), activities.values())
plt.xticks(rotation=90)
plt.title("Frequency of Activities")
plt.tight_layout()
plt.savefig("results/activity_frequency.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(case_durations, bins=30)
plt.title("Distribution of Case Duration")
plt.xlabel("Duration (seconds)")
plt.ylabel("Number of Cases")
plt.tight_layout()
plt.savefig("results/case_duration_distribution.png")
plt.close()

print("\nGrafik berhasil disimpan di folder results/")
