from cluster import Cluster


class AgglomerativeClustering:
    def __init__(self, link, samples):
        """
        build a new AgglomerativeClustering instance
        :param link: a linkage method - single/complete
        :param samples: list of samples
        """
        self.link = link
        self.samples = samples
        self.clusters = []
        for i in samples:
            samples_list = [i]
            self.clusters.append(Cluster(i.s_id, samples_list))

    def compute_silhoeutte(self, distance_list):
        """
        computes the silhouette of a point
        :param distance_list: a similarity matrix
        :return: a dictionary of all samples' silhouettes
        """
        silhoeutte_samples = {}
        out_val = []
        for c in self.clusters:
            for s in c.samples:
                in_val = c.compute_in(s, distance_list)
                for c1 in self.clusters:
                    if c1 != c:
                        out_val.append(c1.compute_in(s, distance_list))
                out = min(out_val)
                out_val.clear()
                if out == 0 and in_val == 0:
                    silhoeutte_samples[s.s_id] = 0.0
                    continue
                silhoeutte_samples[s.s_id] = round((out-in_val)/max(out, in_val), 3)
        return silhoeutte_samples

    def compute_summery_silhoeutte(self, distance_list):
        """
        computes a silhouette for clusters
        :param distance_list: a similarity matrix
        :return: a dictionary, holds silhouette per cluster
        """
        silhoeutte_dict = self.compute_silhoeutte(distance_list)
        summery_silhoeutte = {}
        for cluster in self.clusters:
            sum_sil = 0
            for sample in cluster.samples:
                sum_sil = sum_sil + silhoeutte_dict[sample.s_id]
                if len(cluster.samples) <= 1:
                    summery_silhoeutte[cluster.c_id] = 0.0
                else:
                    summery_silhoeutte[cluster.c_id] = round(sum_sil/len(cluster.samples), 3)
        summery_silhoeutte[0] = silhoeutte_dict
        return summery_silhoeutte

    def compute_rand_index(self):
        """
        computes the rand index of the clustering algorithm
        :return: the rand index of the clustering algorithm
        """
        tp = 0
        fp = 0
        for c in self.clusters:
            for s1 in c.samples:
                for s2 in c.samples:
                    if s1.s_id == s2.s_id:
                        continue
                    if s1.label == s2.label:
                        tp = tp+1
                    else:
                        fp = fp+1
        tn = 0
        fn = 0
        for c1 in self.clusters:
            for s1 in c1.samples:
                for c2 in self.clusters:
                    if c1.c_id == c2.c_id:
                        continue
                    for s2 in c2.samples:
                        if s1.label == s2.label:
                            fn = fn+1
                        else:
                            tn = tn+1
        ri = (tp+tn)/(tp+tn+fp+fn)
        return ri

    def run(self, max_clusters, distance_list):
        """
        runs the clustering algorithm, given a specific linkage method and prints the results
        :param max_clusters: number of final clusters number
        :param distance_list: a similarity matrix
        """
        while len(self.clusters) > max_clusters:
            min_distance = self.link.compute(self.clusters[0], self.clusters[1], distance_list)
            list_names_clusters = [self.clusters[0], self.clusters[1]]
            for c1 in self.clusters:
                for c2 in self.clusters:
                    if c1.c_id != c2.c_id:
                        distance = self.link.compute(c1, c2, distance_list)
                        if distance < min_distance:
                            min_distance = distance
                            list_names_clusters[0] = c1
                            list_names_clusters[1] = c2

            list_names_clusters[0].merge(list_names_clusters[1])
            self.clusters.remove(list_names_clusters[1])
        final_clusters = self.compute_summery_silhoeutte(distance_list)
        for i in self.clusters:
            i.print_details(final_clusters[i.c_id])
        final = self.compute_silhoeutte(distance_list)
        sum1 = sum(final.values())
        length = len(final.values())
        total_silhoeutte = sum1/length
        print("Whole data: silhouette = ", round(total_silhoeutte, 3), ", RI = ", round(self.compute_rand_index(), 3))
