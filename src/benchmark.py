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

models = ["deepseek", "mistral"]
prompts = {
    1: prompts.USER_PROMPT_1,
    2: prompts.USER_PROMPT_2,
    3: prompts.USER_PROMPT_3
}
rag_data = ""

def parse_answer(anwer):
    """
    parses the answer of the llm to only one label
    :param anwer: answer of the llm
    :return: only one label: 'exhausted' or 'not exhausted'
    """
    if "not exhausted" in anwer:
        return "not exhausted"
    elif "exhausted" in anwer:
        return "exhausted"
    else: return "unknown"

for phase in range(2):  # geht gerade nur bis phase 2, weil phase 3 bruacht noch das pubmed
    print("Phase:", phase+1) # iterate over phase
    for llm in models: # go over each llm
        preds = []  ## store predictions for each model
        for cell in cells_data:
            if phase == 3:
                user_prompt = prompts[phase].format(json_input = cells_data, rag_context = rag_data)
            else:
                user_prompt = prompts[phase].format(json_input = cells_data)

