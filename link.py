class Link:
    def compute(self, cluster, other):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class SingleLink(Link):
    def compute(self, cluster, other):
        # need to implement!
        print("hello")
