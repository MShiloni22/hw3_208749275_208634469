import pandas
import sample
from sample import Sample


# define Data class
class Data:
    def __init__(self, path):
        """
        creates a data object with a given path
        :param path: the given path
        """
        self.path = path
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        """
        creates a list of all the samples, based on the dataset
        :return: a list of all the samples
        """
        samples = []
        keys_list = self.data.keys()
        for i in range(len(self.data["samples"])):
            genes_list = []
            for j in keys_list:
                if j != "samples" and j != "type":
                    genes_list.append(self.data[j][i])
            new_sample = sample.Sample(self.data["samples"][i], genes_list, self.data["type"][i])
            samples.append(new_sample)
        return samples

    def create_distance_matrix(self, samples_list):
        """
        creates a similarity matrix for all the samples
        :return: a similarity matrix
        """
        distance_matrix = {}
        for i in samples_list:
            for j in samples_list:
                if i == j:
                    continue
                distance_matrix[(i.s_id, j.s_id)] = i.compute_euclidean_distance(j)
        return distance_matrix
