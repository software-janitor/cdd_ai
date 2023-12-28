from enum import Enum


class LlmModelsEnum(Enum):
    LLM_OPENAI_GPT35 = "gpt-3.5-turbo"
    LLM_FLAN_T5_XXL = "google/flan-t5-xxl"
    LLM_FLAN_T5_XL = "google/flan-t5-xl"
    LLM_FASTCHAT_T5_XL = "lmsys/fastchat-t5-3b-v1.0"
    LLM_FLAN_T5_SMALL = "google/flan-t5-small"
    LLM_FLAN_T5_BASE = "google/flan-t5-base"
    LLM_FLAN_T5_LARGE = "google/flan-t5-large"
    LLM_FALCON_SMALL = "tiiuae/falcon-7b-instruct"
