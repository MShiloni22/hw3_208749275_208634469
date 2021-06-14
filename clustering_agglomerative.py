from sample import Sample

class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link
        self.samples = samples
        self.distance_list = {}
        for i in samples:
            for j in samples:
                self.distance_list[(i.s_id, j.s_id)] = Sample.compute_euclidean_distance(i, j)



    def compute_silhoeutte(self):
        return
