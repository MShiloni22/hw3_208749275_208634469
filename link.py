from sample import Sample


class Link:
    def compute(self, cluster, other, distance_list):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class SingleLink(Link):
    def compute(self, cluster, other, distance_list):
        """
        computes the distance between two clusters, according to single link method
        :param cluster: first cluster
        :param other: second cluster
        :param distance_list: dictionary of all distances
        :return: the distance between the clusters, according to single link method
        """
        minimum_distance = Sample.compute_euclidean_distance(cluster.samples[0], other.samples[0])
        for point_from_cluster in cluster.samples:
            for point_from_other in other.samples:
                distance = distance_list[(point_from_cluster, point_from_other)]
                if distance < minimum_distance:
                    minimum_distance = distance
        return minimum_distance


class CompleteLink(Link):
    def compute(self, cluster, other, distance_list):
        """
                computes the distance between two clusters, according to single link method
                :param cluster: first cluster
                :param other: second cluster
                :param distance_list: dictionary of all distances
                :return: the distance between the clusters, according to single link method
                """
        maximum_distance = Sample.compute_euclidean_distance(cluster.samples[0], other.samples[0])
        for point_from_cluster in cluster.samples:
            for point_from_other in other.samples:
                distance = distance_list[(point_from_cluster, point_from_other)]
                if distance > maximum_distance:
                    maximum_distance = distance
        return maximum_distance
