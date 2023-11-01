import numpy as np

def hits_algorithm(graph, max_iterations=100, tolerance=1e-6):
    n = len(graph)
    
    # Initialize hub and authority scores
    hub_scores = np.ones(n)
    authority_scores = np.ones(n)
    
    for _ in range(max_iterations):
        # Update authority scores
        new_authority_scores = np.dot(graph.T, hub_scores)
        
        # Normalize authority scores
        new_authority_scores /= np.linalg.norm(new_authority_scores, 2)
        
        # Update hub scores
        new_hub_scores = np.dot(graph, new_authority_scores)
        
        # Normalize hub scores
        new_hub_scores /= np.linalg.norm(new_hub_scores, 2)
        
        # Check for convergence
        if np.linalg.norm(new_authority_scores - authority_scores) < tolerance and \
           np.linalg.norm(new_hub_scores - hub_scores) < tolerance:
            break
        
        authority_scores = new_authority_scores
        hub_scores = new_hub_scores
    
    return hub_scores, authority_scores

# Define a simple web graph as an adjacency matrix
web_graph = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 0]
])

# Compute HITS scores for the web pages
hub_scores, authority_scores = hits_algorithm(web_graph)
print("Hub Scores:", hub_scores)
print("Authority Scores:", authority_scores)
