class LlmFactory():
    pass



from transformers import pipeline
from transformers import AutoTokenizer

llm = pipeline(task="text2text-generation",model="google/flan-t5-xl",max_new_tokens=200,model_kwargs={"device_map": "auto", "load_in_8bit": False, "max_length": 512, "temperature": 0.})
#print(pipeline('sentiment-analysis')('we love you'))


model = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model)
llm = pipeline(task="text2text-generation",model=model,tokenizer=tokenizer,max_new_tokens=100,model_kwargs={"device_map": "auto", "load_in_8bit": False, "max_length": 512, "temperature": 0.})

prompt = "Translate the text from english to spanish: 'Get fucked idiot'"
result = llm(prompt)

