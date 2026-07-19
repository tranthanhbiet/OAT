class BaseExporter:
    """
    Base class for exporters.
    """

    def write(self, genome, filename):
        """
        Export a genome.
        """
        raise NotImplementedError