from transformers import pipeline
from src.components.extractive_sum import Extractive_Sum
from src.components.extractive_sum import Extractive_Sum 




summarizer = pipeline("summarization", model="Falconsai/text_summarization")

get_extract = Extractive_Sum()


extracted_data_location = get_extract.extractor()

for s in extracted_data_location:
    path = str(s)



with open(path, 'r') as file:
    text = file.readlines()

print(text)
summary = summarizer(text, max_length=1000, min_length=30, do_sample=False)

print(summary[0])

