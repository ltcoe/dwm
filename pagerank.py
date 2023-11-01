import numpy as np

def pagerank(graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
    # Number of web pages
    n = len(graph)

    # Create the transition matrix M
    M = np.zeros((n, n))
    for i in range(n):
        count = np.count_nonzero(graph[i])
        for j in range(n):
            if count == 0:
                M[i][j] = 1 / n  # Handle pages with no links
            else:
                M[i][j] = (damping_factor * graph[i][j] / count) + (1 - damping_factor) / n

    # Initialize the PageRank vector
    pagerank_vector = np.full(n, 1.0 / n)

    # PageRank iteration
    for _ in range(max_iterations):
        new_pagerank_vector = np.dot(M, pagerank_vector)
        if np.linalg.norm(new_pagerank_vector - pagerank_vector) < tolerance:
            break
        pagerank_vector = new_pagerank_vector

    return pagerank_vector

# Define a simple web graph as an adjacency matrix
# In this example, we have 4 web pages
web_graph = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 0]
])

# Compute PageRank scores for the web pages
page_rank_scores = pagerank(web_graph)
print("PageRank Scores:", page_rank_scores)
