

class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        self.c_id = min(self.c_id, other.c_id)
        self.samples.append(other.samples)
        self.samples.sort(key=lambda x: x.s_id)
        del other

    def print_details(self, silhouette):
        count = 0
        dominant_label = ""
        id_list = []
        labels = {'B - CELL_ALL': 0, 'B - CELL_ALL_TCF3 - PBX1': 0, 'B - CELL_ALL_HYPERDIP': 0, 'B - CELL_ALL_HYPO': 0,
                  'B - CELL_ALL_MLL': 0, 'B - CELL_ALL_T - ALL': 0, 'B - CELL_ALL_ETV6 - RUNX1': 0}
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

        print("Cluster", self.c_id, ":[", id_list, "], dominant label =", dominant_label, ", silhouette =", silhouette)








