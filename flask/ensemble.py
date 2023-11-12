

def soft_voting(sentimental_result, classification_result, weight1=0.7, weight2=0.3):
    final_pred = []
    for p1, p2 in zip(sentimental_result, classification_result):
        # Calculate the weighted average probabilities across all classes
        avg_prob = [(x * weight1 + y * weight2) for x, y in zip(p1, p2)]
        # Choose the class with the highest weighted average probability
        final_pred.append(avg_prob.index(max(avg_prob)))
    return final_pred[0]