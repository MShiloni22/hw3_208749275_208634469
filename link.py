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
        distance = []
        for point_from_cluster in cluster.samples:
            for point_from_other in other.samples:
                distance.append(distance_list[(point_from_cluster.s_id, point_from_other.s_id)])
        minimum_distance = min(distance)
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
        distance = []
        for point_from_cluster in cluster.samples:
            for point_from_other in other.samples:
                distance.append(distance_list[(point_from_cluster.s_id, point_from_other.s_id)])
        maximum_distance = max(distance)
        return maximum_distance
