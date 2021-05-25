import pandas
import sample


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
        genes_list = []
        keys_list = self.data.keys()
        for i in self.data["samples"]:
            for j in keys_list:
                if j != "samples" and j != "type":
                    genes_list.append(self.data[j][i])
            new_sample = sample.Sample(self.data["samples"][i], genes_list, self.data["type"][i])
            samples.append(new_sample)
