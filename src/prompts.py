ANSWER_FORMAT = "Answer as follows: This cell will most likely become (answer only 'exhausted' or 'not exhausted'):"

SYSTEM_PROMPT = "You are an immunologist specializing in T-Cell biology. You always respond in exactly one label."

USER_PROMPT_1 = ("Given the following expression data of T-Cells from a chronic infection, annotate via the given data "
                 " whether this cell becomes exhausted or a not-exhausted t-cell. \n\n" 
                 "Expression data: \n{json_input}\n\n"+
                 ANSWER_FORMAT)

USER_PROMPT_2 = ("Given the following expression data of T-Cells from a chronic infection, annotate via the given data "
                 " whether this cell becomes exhausted or a not-exhausted t-cell. \n\n"
                 "Expression data: \n{json_input}\n\n"
                 "Let's think step by step: \n "
                 "1. What does the phase, timepoint and cluster indicate about the current cell state? \n"
                 "2. How does the value of the latent_time and pseudotime refelect the current position in the development of the "
                 "cell? Also the insights from the palantir PST. \n"
                 "3. Analyze the top-10 expressed gene marker, what do they indicate about the current cell state? \n"
                 "4. Based on these observations, what is the most likely fate of the cell?\n\n" +
                ANSWER_FORMAT)

USER_PROMPT_3 = ("Given the following expression data of T-Cells from a chronic infection and additional information from pubmed, annotate via the given data "
                 " whether this cell becomes exhausted or a not-exhausted t-cell. \n\n"
                 "Expression data: \n{json_input}\n\n"
                 "Literature: \n{rag_context}\n\n"
                 "Let's think step by step: \n "
                 "1. What does the phase, timepoint, pseudotime, latent_time, Palantir PST and cluster indicate about "
                 "the current position and trajectory of the cell? \n"
                 "2. What exhaustion-associated genes from the literature are elevated or lowered in the current cell? \n"
                 "3. Which non-exhaustion-associated genes from the literature are elevated in the current cell? \n"
                 "4. Based on the expression file and literature insights, what is the most likely fate of the cell?\n\n" +
                ANSWER_FORMAT)