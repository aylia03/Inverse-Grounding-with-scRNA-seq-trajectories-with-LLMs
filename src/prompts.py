ANSWER_FORMAT = "Answer as follows: This cell will most likely become (answer only 'exhausted' or 'not exhausted'):"

SYSTEM_PROMPT_1 = "You are an immunologist specializing in T-Cell biology. You always respond in exactly one label."
USER_PROMPT_1 = ("Given the following expression data of T-Cells from a chronic infection, annotate via the given data "
                 " whether this cell becomes exhausted or a not-exhausted t-cell . \n\n" 
                 "Expression data: \n{json_input}\n\n"+
                 ANSWER_FORMAT)