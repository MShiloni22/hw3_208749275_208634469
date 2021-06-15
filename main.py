import sys
import data
import link
import clustering_agglomerative


def main(argv):
    data_dict = data.Data(argv[1])
    samples_list = data_dict.create_samples()
    distance_list = data_dict.create_distance_matrix(samples_list)
    max_clusters = 7

    print("single link:")
    single_link = link.SingleLink
    runner_single = clustering_agglomerative.AgglomerativeClustering(single_link, samples_list)
    runner_single.run(max_clusters, distance_list)
    print()

    print("complete link:")
    complete_link = link.CompleteLink
    runner_complete = clustering_agglomerative.AgglomerativeClustering(complete_link, samples_list)
    runner_complete.run(max_clusters, distance_list)


if __name__ == '__main__':
    main(sys.argv)
