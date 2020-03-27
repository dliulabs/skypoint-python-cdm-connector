import abc


class Writer(metaclass=abc.ABCMeta):

        @abc.abstractmethod
        def write_df(self, location, dataframe):()

        @abc.abstractmethod
        def write_json(self, location, json_dict): ()