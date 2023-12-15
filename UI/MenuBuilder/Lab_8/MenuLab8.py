"""
Module defining the MenuLab8 class, which represents the menu for Lab 8 operations.
"""

from Classes.Lab_8.data_processor import DataProcessor
from Shared.BuilderMenu.BuilderMenu import BuilderMenu
from UI.MenuBuilder.Lab_8.Commands import *
from Shared.Console.Input import (InputValue, SelectObjectWithDictCommand)
from Shared.Constants import COLORS, FONTS, DATA_METHODS


class MenuLab8(BuilderMenu):
    """
    Class representing the menu for Lab 8 operations.
    Inherits from BuilderMenu.
    """
    def __init__(self):
        super().__init__()
        self._data_processor = DataProcessor()
        self.__method = InputValue(message="Choose method")

    def _configure_package_name(self):
        """
        Configure the package name for Lab 8.
        """
        self._package_name = 'Lab_8'

    def run_menu(self):
        self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__method, DATA_METHODS))
        if self.__method.value == 'EXPLORE DATA':
            self._menu_builder.instant_command(ExploreData(self._data_processor))
        elif self.__method.value == 'VISUALIZE DATA':
            self._menu_builder.instant_command(VisualizeData(self._data_processor))
        try:
            self._configure_save_subsystem()
        except BaseException as e:
            self._result = e.__str__()

    # def _configure_lab_subsystem(self):
    #     """
    #     Configure the subsystems for Lab 8 menu.
    #     """
    #     self.__configure_request_subsystem()
    #     self.__configure_header_color_subsystem()
    #     self.__configure_header_font_subsystem()
    #     self.__configure_build_request_subsystem()

    # def __configure_request_subsystem(self):
    #     """
    #     Configure the request subsystem for Lab 8 menu.
    #     """
    #     self._menu_builder.instant_command(InputTextCommand(self.__site))
    #     self._menu_builder.instant_command(SetSiteCommand(self.__request, self.__site.value))
    #
    # def _convert_obj_to_result_subsystem(self):
    #     """
    #     Convert the result subsystem to a string.
    #     """
    #     self._result = self.__request.__str__()
    #
    # def __configure_header_color_subsystem(self):
    #     """
    #     Configure the header color subsystem for Lab 8 menu.
    #     """
    #     self._menu_builder.instant_command(SetInputMessageCommand(self._subsystem_status,
    #                                                               "Do you want to set header color (1/0:)"))
    #     self._configure_check_subsystem()  # color
    #     if self._subsystem_status.value:
    #         self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__color, COLORS))
    #         self._menu_builder.instant_command(SetColorCommand(self.__request, self.__color.value))
    #
    # def __configure_header_font_subsystem(self):
    #     """
    #     Configure the header font subsystem for Lab 8 menu.
    #     """
    #     self._menu_builder.instant_command(SetInputMessageCommand(self._subsystem_status,
    #                                                               "Do you want to set header font (1/0:)"))
    #     self._configure_check_subsystem()  # font
    #     if self._subsystem_status.value:
    #         self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__font, FONTS))
    #         self._menu_builder.instant_command(SetFontCommand(self.__request, self.__font.value))
    #
    # def __configure_custom_header_build_request_subsystem(self):
    #     """
    #     Configure the custom header build request subsystem for Lab 8 menu.
    #     """
    #     self._menu_builder.instant_command(SetInputMessageCommand(self._subsystem_status,
    #                                                               "Do you want to set select header (1/0:)"))
    #     self._configure_check_subsystem()  # select header
    #     if self._subsystem_status.value:
    #         self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__font, FONTS))
    #
    # def __configure_build_request_subsystem(self):
    #     """
    #     Configure the build request subsystem for Lab 8 menu.
    #     """
    #     self._menu_builder.instant_command(SelectObjectWithDictCommand(self.__data_type, DATA_TYPE))
    #     if self.__data_type.value == 'LIST':
    #         self._menu_builder.instant_command(BuildListCommand(self.__request))
    #     else:
    #         self._menu_builder.instant_command(BuildTableCommand(self.__request))
