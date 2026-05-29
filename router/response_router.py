from prompts.troubleshooting_prompt import TROUBLESHOOTING_PROMPT
from prompts.comparison_prompt import COMPARISON_PROMPT
from prompts.general_prompt import GENERAL_PROMPT


def get_prompt(query_type):

    if query_type == "troubleshooting":
        return TROUBLESHOOTING_PROMPT

    elif query_type == "comparison":
        return COMPARISON_PROMPT

    else:
        return GENERAL_PROMPT
