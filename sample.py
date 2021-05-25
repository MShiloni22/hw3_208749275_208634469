# define class sample
class Sample:
    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label

    def compute_euclidean_distance(self, other):
        """
        computes euclidean distance between two vectors
        :param other: another vector
        :return: distance between the current point and the input point, l2-norm
        """
        distance = 0
        squared_components_distance_sum = 0
        for i in self.genes:
            squared_components_distance_sum += (self.genes[i] - other.genes[i])**2
        distance += squared_components_distance_sum**0.5
        return distance
