
# from .assets import prompts
from src import openai_api

def main() -> None:

    chat = openai_api.OpenAI()

    first_msg = chat.create_message(
        "gpt-4",
        "user"
        "What is today",
        
        sys_prompt="You are an expert at something",
    )
    chat.messages.append(first_msg)

    chat.gpt_generate(
        "gpt-3.5-turbo",
        "Hello world",
        "You are an expert at assisting people",
        msg_lookback_ct=5,
        temperature=0,
    )

import os
import openai
import dotenv
import sklearn.metrics
import numpy as np
dotenv.load_dotenv(dotenv.find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_norm_vector(vector):
    if len(vector.shape) == 1:
        return vector / np.linalg.norm(vector)
    else:
        return vector / np.linalg.norm(vector, axis=1)[:, np.newaxis]

def cosine_similarity(target_vec, query_vec):
    norm_vectors = get_norm_vector(target_vec)
    norm_query_vector = get_norm_vector(query_vec)
    similarities = np.dot(norm_vectors, norm_query_vector.T)
    return similarities

def hyper_SVM_ranking_algorithm_sort(vectors, query_vector, top_k=5, metric=cosine_similarity):
    """HyperSVMRanking (Such Vector, Much Ranking) algorithm proposed by Andrej Karpathy (2023) https://arxiv.org/abs/2303.18231"""
    similarities = metric(vectors, query_vector)
    top_indices = np.argsort(similarities, axis=0)[-top_k:][::-1]
    return top_indices.flatten(), similarities[top_indices].flatten()

def get_embedding(text):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input = [text], model="text-embedding-ada-002")['data'][0]['embedding']

def query(query_vec, compare_word_vec, top_k=5):

    ranked_results, similarities = hyper_SVM_ranking_algorithm_sort(
        compare_word_vec, query_vec, top_k=top_k, metric=cosine_similarity
    )
    return (similarities, ranked_results)

def embedding_game():
    target_word = "mother"
    target_word_vec = np.array(get_embedding(target_word))

    
    print(target_word_vec.shape)

    embed_0: list[str] = np.array(get_embedding("frog"))
    embed_1: list[str] = np.array(get_embedding("amphibian"))
    embed_2: list[str] = np.array(get_embedding("father"))
    embed_3: list[str] = np.array(get_embedding("woman"))

    target = (target_word_vec)

    test_0 = embed_0 - embed_1 + embed_3

    # Figure out a way to make it so that the target and starting word similarity normalize to 0
    # or something like that so that when guessing, its more difficult and doesn't just give it away?
    # Because the default for both 1 word targets and starting words seems to be above 75-80% no matter
    # how unrelated they actually are..
    similarity_0 = cosine_similarity(target, test_0)
    similarity_1 = sklearn.metrics.pairwise.cosine_similarity(np.reshape(target_word_vec, (-1, 1)), np.reshape(test_0, (-1, 1)))

    # result = query(test_0, target_word, 5)
    print(similarity_0)
    print(similarity_1)






if __name__ == '__main__':
    # main()
    embedding_game()
