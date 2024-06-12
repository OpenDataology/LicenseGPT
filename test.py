import json
from transformers import AutoModelForSequenceClassification, AutoTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import torch

# 加载微调后的模型
model_path = 'path/to/your/fine-tuned-model'
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 加载BERT模型用于语义相似度比较
bert_model_name = 'bert-base-uncased'
bert_model = BertModel.from_pretrained(bert_model_name)
bert_tokenizer = AutoTokenizer.from_pretrained(bert_model_name)

# 加载测试数据集
test_data_path = 'path/to/your/test-data.json'

with open(test_data_path, 'r', encoding='utf-8') as f:
    test_data = json.load(f)

# 生成预测结果
predicted_answers = []

for item in test_data:
    question = item['input']
    inputs = tokenizer(question, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    predicted_answer = tokenizer.decode(torch.argmax(outputs.logits, dim=-1), skip_special_tokens=True)
    predicted_answers.append(predicted_answer)

# 计算语义相似度
def get_bert_embedding(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

similarities = []

for idx, item in enumerate(test_data):
    standard_answer = item['output']
    predicted_answer = predicted_answers[idx]
    
    standard_embedding = get_bert_embedding(standard_answer, bert_tokenizer, bert_model)
    predicted_embedding = get_bert_embedding(predicted_answer, bert_tokenizer, bert_model)
    
    similarity = cosine_similarity(standard_embedding.numpy(), predicted_embedding.numpy())[0][0]
    similarities.append(similarity)

# 计算准确率
threshold = 0.8
correct_predictions = [1 if sim >= threshold else 0 for sim in similarities]
accuracy = sum(correct_predictions) / len(correct_predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")
