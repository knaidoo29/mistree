from scipy.sparse import csr_matrix


def graph2data(graph):
    """Returns the index and data of a sparse csr_matrix

    Parameters
    ----------
    graph : csr_matrix
        A sparse matrix of the edges in a graph and corresponding node indexes.

    Returns
    -------
    ind1, ind2 : array
        Graph edge node indices.
    weight : array
        Weights for each edge.
    """
    graph = graph.tocoo()
    weights = graph.data
    ind1 = graph.row
    ind2 = graph.col
    return ind1, ind2, weights


def data2graph(ind1, ind2, weights, Nnodes):
    """Returns the sparse matrix of a graph given the indices and data.

    Parameters
    ----------
    ind1, ind2 : array
        Node indices of the graph.
    weights : array
        An array of the weights of each edge in the graph.
    Nnodes : int
        Total number of nodes.

    Returns
    -------
    graph : csr_matrix
        A sparse matrix of the edges in a graph and corresponding node indices.
    """
    graph = csr_matrix((weights, (ind1, ind2)), shape=(Nnodes, Nnodes))
    return graph
