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
                 "1. What does the expression pattern suggest about the current cell state? \n"
                 "2. How does the value of the latent_time variable refelect the current position in the development of the "
                 "cell? \n"
                 "3. Now include also the insights from the given phase and timepoint of the cell data? \n"
                 "4. Based on these observations, what is the most likely fate of the cell?\n\n" +
                ANSWER_FORMAT)

USER_PROMPT_3 = ("Given the following expression data of T-Cells from a chronic infection and additional information from pubmed, annotate via the given data "
                 " whether this cell becomes exhausted or a not-exhausted t-cell. \n\n"
                 "Expression data: \n{json_input}\n\n"
                 "Literature: \n{rag_context}\n\n"
                 "Let's think step by step: \n "
                 "1. What exhaustion-associated genes from the literature are elevated or lowered in the current cell? \n"
                 "2. Which non-exhaustion-associated genes from the literature are elevated in the current cell? \n"
                 "3. What does the latent_time, phase, timepoint indicated about the cell\n"
                 "4. Based on the expression file and literature insights, what is the most likely fate of the cell?\n\n" +
                ANSWER_FORMAT)