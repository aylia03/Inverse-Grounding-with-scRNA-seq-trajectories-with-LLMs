import json
import os

import pandas as pd

import prompts as prompt
from llms_clients import call_llms

from sklearn.metrics import f1_score

import rag

print("Loading the data ...")
with open("../Data/processed/cells_data.json", "r") as f:
    cells_data = json.load(f)
print("Cell data is loaded. ")

with open("../Data/processed/labels_gt_data.json", "r") as f:
    gt = json.load(f)
print("Groundtruth is loaded.\n")

models = ["deepseek"]
prompts = {
    1: prompt.USER_PROMPT_1,
    2: prompt.USER_PROMPT_2,
    3: prompt.USER_PROMPT_3
}
rag_data = rag.get_rag_context()

gt_labels = [x["label"] for x in gt]

result = []

def parse_answer(answer):
    """
    parses the answer of the llm to only one label
    :param answer: answer of the llm
    :return: only one label: 'exhausted' or 'not exhausted'
    """
    if "not exhausted" in answer:
        return "not exhausted"
    elif "exhausted" in answer:
        return "exhausted"
    else: return "unknown"

for phase in range(3):  # geht gerade nur bis phase 2, weil phase 3 bruacht noch das pubmed
    print("Phase:", phase+1) # iterate over phase
    for llm in models: # go over each llm
        preds = []  ## store predictions for each model
        for cell_idx, cell in enumerate(cells_data):
            if phase == 2:
                user_prompt = prompts[phase+1].format(json_input = json.dumps(cell), rag_context = rag_data)
            else:
                user_prompt = prompts[phase+1].format(json_input = json.dumps(cell))

            pred = parse_answer(call_llms(llm, prompt.SYSTEM_PROMPT, user_prompt))
            preds.append(pred)

            gt_label = gt_labels[cell_idx]

            result.append({
                "phase": phase + 1,
                "LLM":llm,
                "Cell ID": cell["cell_id"],
                "prediction": pred,
                "ground_truth": gt_label
            }
        )

        f1 = f1_score(gt_labels, preds, labels=["exhausted", "not exhausted"], average="weighted")
        for row in result:
            if row["phase"] == phase+1 and row["LLM"] == llm:
                row["F1"] = f1

df = pd.DataFrame(result)

os.makedirs("../Data/results/", exist_ok=True)
df.to_csv("../Data/results/benchmarking_res.csv", index=False )


