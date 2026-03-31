import numpy as np
import pandas as pd
import anndata as ad
from pathlib import Path
import json

OUTPUT_DIR = Path("../Data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


#load data
adata = ad.read_h5ad("../Data/tex_data_chronic_cytopath.h5ad")
print(adata)
layer = adata.layers["Ms"]

expr_mat = pd.DataFrame(
    layer,
    index = adata.obs_names,
    columns = adata.var_names
)

# extract metadata
meta = adata.obs[["annot", "latent_time", "phase", "n_counts", "timepoint", "ratio_0", "ratio_1"]].copy()
# class distribution
print("Class distribution before balancing:", meta["annot"].value_counts())

# build binary labels
meta["label"] = meta["annot"].apply(
    lambda x: "exhausted" if "exh" in str(x).lower() else "not exhausted"
)

exhausted = meta[meta["label"] == "exhausted"]
not_exhausted = meta[meta["label"] == "not exhausted"]


# random undersampling for imbalance
n = min(len(exhausted), len(not_exhausted)) # want to cute the bigger class down to the smaller class
exh_sampled = exhausted.sample(n, random_state = 42)
not_exh_sampled = not_exhausted.sample(n, random_state = 42)
balanced_meta = pd.concat([exh_sampled, not_exh_sampled])
print("Class distribution after balancing: ")
print(len(balanced_meta), "cells (", n," per class)")

def get_top_10_genes(cell_id, genes=10):
    cell_exp = expr_mat.loc[cell_id]
    top_genes = cell_exp.nlargest(genes)
    return {gene: round(float(val), 4) for gene, val in top_genes.items()}

# test case
test_exh = exh_sampled.sample(25, random_state = 42)
test_not_exh =not_exh_sampled.sample(25, random_state = 42)
test_cases = pd.concat([test_exh, test_not_exh]).sample(frac=1, random_state = 42) # shuffeling the order of the single entries

# build JSON
print("Starting building JSON...")

cells_data = []
labels_data = []

for cell_id in test_cases.index:
    row = test_cases.loc[cell_id]

    cell_entry = {
        "cell_id": cell_id,
        "top_10_genes": get_top_10_genes(cell_id),
        "latent_time": round(float(row["latent_time"]), 4),
        "phase": str(row["phase"]) if "phase" in row else "unknown",
        "timepoint": str(row.get("timepoint", "unknown")),
        "count": str(row.get("n_counts", "0"))
    }
    cells_data.append(cell_entry)

    label_entry = {
        "cell_id": cell_id,
        "label": row["label"],
        "annot_original": str(row["annot"])
    }
    labels_data.append(label_entry)

with open(OUTPUT_DIR / "cells_data.json", "w") as f:
    json.dump(cells_data, f, indent=4)

with open(OUTPUT_DIR / "labels_gt_data.json", "w") as f:
    json.dump(labels_data, f, indent=4)