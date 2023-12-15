from Shared.Command.Command import Command
from Classes.Lab_8.data_processor import DataProcessor


class ExploreData(Command):
    """
    Command can implement create art .
    """

    def __init__(self, executor: DataProcessor):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.explore_data()
