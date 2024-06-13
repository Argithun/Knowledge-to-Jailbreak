from rouge_score.rouge_scorer import RougeScorer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import paired_cosine_distances
from tqdm import tqdm

def rouge_and_similarity_score(targets, preds):
    rouge_scorer = RougeScorer(['rougeL'], use_stemmer=True)
    se_model = SentenceTransformer('sentence-transformers/nli-roberta-large')
    rouge_scores = []
    for t, p in tqdm(zip(targets, preds), total=len(targets), desc="Calculating ROUGE scores"):
        rouge_scores.append(rouge_scorer.score(t, p)['rougeL'].fmeasure)
    print("Encoding targets:")
    target_embeddings = se_model.encode(targets, show_progress_bar=True)
    print("Encoding predictions:")
    prediction_embeddings = se_model.encode(preds, show_progress_bar=True)
    cosine_similarity = 1 - paired_cosine_distances(target_embeddings, prediction_embeddings)
    return rouge_scores, cosine_similarity.tolist()