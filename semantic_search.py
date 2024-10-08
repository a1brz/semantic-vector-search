import torch
import requests
import json

def get_embedding(user_prompt):
    url = "http://localhost:11434/api/embeddings"
    headers = {
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        "model": "mxbai-embed-large",
        "prompt": user_prompt
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    embedding = response.json()['embedding']
    return embedding

def get_relevant_content(user_prompt, embeddings, content, top_k=1):
    input_embedding = get_embedding(user_prompt)
    similarity_scores = torch.cosine_similarity(torch.tensor(input_embedding).unsqueeze(0), embeddings)
    top_k = min(top_k, len(similarity_scores))
    scores, indices = torch.topk(similarity_scores, k=top_k)

    results = []
    for score, idx in zip(scores, indices):
        matched_content = {
            "content": content[idx],
            "score": f"{score:.5f}"
        }
        results.append(matched_content)

    return results

if __name__ == "__main__":
    sentances = [
        "The local grocery store sells fresh organic apples from local farms.",
        "We offer a wide variety of dairy products, including milk, cheese, and yogurt.",
        "Our bakery section features daily fresh bread, pastries, and gluten-free options.",
        "Get the best deals on seasonal fruits like oranges, mangoes, and strawberries.",
        "The seafood department provides freshly caught salmon, shrimp, and lobsters."
    ]
    
    print("Generating embeddings...")
    embeddings = []

    for sentance in sentances:
       embedding = get_embedding(sentance)
       embeddings.append(embedding)

    embeddings_tensor = torch.tensor(embeddings)

    queries = [
        "Where can I buy organic apples?",
        "Do you have gluten-free bread?",
        "What seasonal fruits are available?",
        "I'm looking for fresh seafood options.",
        "Can I find yogurt and milk here?",
    ]

    for query in queries:
        relevant_content = get_relevant_content(query, embeddings_tensor, sentances)
        print(f"Question: {query}")
        for rc in relevant_content:
            print('Answer: ' + rc['content'] + ' - Score: %s'% rc['score'])