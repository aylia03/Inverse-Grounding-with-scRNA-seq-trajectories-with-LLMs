import json

import prompts as prompts
# from llms_clients import call_llms

print("Loading the data ...")
with open("../Data/processed/cells_data.json", "r") as f:
    cells_data = json.load(f)
print("Cell data is loaded. ")

with open("../Data/processed/labels_gt_data.json", "r") as f:
    gt = json.load(f)
print("Groundtruth is loaded.\n")


