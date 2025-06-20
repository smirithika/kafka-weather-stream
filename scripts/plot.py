import matplotlib.pyplot as plt
from collections import Counter
import os

event_counts = Counter()
chart_path = 'charts/event_counts.png'

def plot_event_counts(counter):
    plt.figure(figsize=(8, 5))
    types = list(counter.keys())
    counts = [counter[t] for t in types]
    plt.bar(types, counts, color='skyblue')
    plt.title("Event Type Counts")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.xticks(rotation=30)
    plt.tight_layout()

    os.makedirs(os.path.dirname(chart_path), exist_ok=True)
    plt.savefig(chart_path)
    plt.close()
