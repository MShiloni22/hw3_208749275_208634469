class Cluster:
    def __init__(self, c_id, samples):
        """
        build a new Cluster instance
        :param c_id: cluster's name, in the beginning it's the sample's id
        :param samples: list of samples which are in the cluster
        """
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        """
        merges two clusters, gives the minimum name
        :param other: a second cluster to be merged with the current (self) cluster
        """
        self.c_id = min(self.c_id, other.c_id)
        self.samples.extend(other.samples)
        self.samples.sort(key=lambda x: x.s_id)

    def compute_in(self, s_sample, distance_list):
        """
        computes the average distance between a sample and the samples in a given cluster
        :param s_sample: a specific cluster
        :param distance_list: a similarity matrix
        :return: average distance between a sample and the samples in a given cluster
        """
        in_val = 0
        for s in self.samples:
            if s.s_id != s_sample.s_id:
                in_val = in_val + distance_list[(s_sample.s_id, s.s_id)]
        if s_sample in self.samples:
            if len(self.samples) == 1:
                return 0
            return in_val / (len(self.samples)-1)
        else:
            return in_val / (len(self.samples))

    def print_details(self, silhouette):
        """
        prints the details for each cluster
        :param silhouette: the silhouette of the cluster
        """
        count = 0
        dominant_label = ""
        id_list = []
        labels = {"B-CELL_ALL": 0, "B-CELL_ALL_TCF3-PBX1": 0, "B-CELL_ALL_HYPERDIP": 0, "B-CELL_ALL_HYPO": 0,
                  "B-CELL_ALL_MLL": 0, "B-CELL_ALL_T-ALL": 0, "B-CELL_ALL_ETV6-RUNX1": 0}
        # אולי צריך "" במקום ''
        for s in self.samples:
            labels[s.label] += 1
            id_list.append(s.s_id)
        for i in labels:
            if labels[i] > count:
                count = labels[i]
                dominant_label = i
            if labels[i] == count:
                if i < dominant_label:
                    count = labels[i]
                    dominant_label = i

        print("Cluster", self.c_id, ": ", id_list, ", dominant label = ", dominant_label, ", silhouette = ", silhouette,
              sep='')
