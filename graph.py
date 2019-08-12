#! /usr/bin/env python3.7

import os, sys
from decimal import Decimal

import matplotlib
matplotlib.use('Agg')
# matplotlib.rcParams['text.usetex'] = True
# matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage[cm]{sfmath}']
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = 'cm'
matplotlib.rcParams.update({'errorbar.capsize': 2})
from matplotlib.ticker import ScalarFormatter
import matplotlib.patches as mpatches
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import histogram

HISTOGRAM_BINS = 50

def flat_zip(*lists):
    assert len(lists) > 0
    for l in lists:
        assert len(l) == len(lists[0])
    out = []
    for i in range(len(lists[0])):
        for l in lists:
            out.append(l[i])
    return out

def load(path):
    with file(path) as f:
        return [float(l) for l in f]

def times_histogram(out_path, paths):
    sns.set(style="whitegrid")
    # plt.rc('text', usetex=True)
    plt.rc('font', family='sans-serif')
    fig, ax = plt.subplots(figsize=(6, 4))

    times = [load(p) for p in paths]
    min_time = min([min(t) for t in times])
    max_time = max([max(t) for t in times])

    bins = [histogram(t, bins=HISTOGRAM_BINS, range=(min_time, max_time))[0] for t in times]

    barlist = plt.bar(range(HISTOGRAM_BINS * len(paths)), flat_zip(*bins), \
            align="center", error_kw={"ecolor": "black", "elinewidth": 1, "capthick": 0.5, "capsize": 1})
    clrs = sns.color_palette('Paired', n_colors=len(paths))
    for i in range(0, HISTOGRAM_BINS):
        for j in range(len(paths)):
            barlist[i * len(paths) + j].set_color(clrs[j])

    if len(paths) > 1:
        handles = []
        for i in range(len(paths)):
            handles.append(mpatches.Patch(color=clrs[i], label=paths[i]))
        plt.legend(handles=handles)

    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Number of runs')
    ax.grid(linewidth=0.25)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.xlim(xmin=0, xmax=HISTOGRAM_BINS*len(paths))
    locs = []
    labs = []
    for i in range(0, 6):
        locs.append(((HISTOGRAM_BINS * len(paths)) / 5) * i - 0.5)
        labs.append("%.3f" % (min_time + (max_time - min_time) * (i / 6.0)))
    plt.xticks(locs, labs)
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    ax.yaxis.set_major_formatter(formatter)
    fig.tight_layout()
    plt.savefig(sys.argv[1], format="pdf")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: graph.py <output.pdf> <times_1> [... <times_n>]\n")
        sys.exit(1)
    if os.path.exists(sys.argv[1]):
        sys.stderr.write("Error: %s already exists.\n" % sys.argv[1])
        sys.exit(1)
    times_histogram(sys.argv[1], sys.argv[2:])
