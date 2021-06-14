from sample import Sample
from cluster import Cluster


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link
        self.clusters = []
        j = 0
        for i in samples:
            self.clusters.append(Cluster(j, i))
            j = j+1


    def compute_silhoeutte(self, distance_list):
        silhoeutte_samples = {}
        out_val = []
        for c in self.clusters:
            for s in c.samples:
                in_val = c.compute_in(s, distance_list)
                for c1 in self.clusters:
                    if c1!=c:
                        out_val.append(c1.compute_in(s, distance_list))
                out = min(out_val)
                silhoeutte_samples[s.s_id] = out-in_val/max(out,in_val)
                out_val = []
        return silhoeutte_samples


    def compute_summery_silhoeutte(self , distance_list):
        silhoeutte_dict = self.compute_silhoeutte(distance_list)
        summery_silhoeutte = {}
        for cluster in self.clusters:
            sum_sil = 0
            for sample in cluster.samples:
                sum_sil = sum_sil +silhoeutte_dict[sample.s_id]
                if len(cluster.samples)<=1:
                    summery_silhoeutte[cluster.c_id]=0
                else:
                    summery_silhoeutte[cluster.c_id] = round(sum_sil/len(cluster.samples))
        return summery_silhoeutte










