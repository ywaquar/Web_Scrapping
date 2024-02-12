import os
from datetime import datetime

class SaveFile:
    @staticmethod
    def generate_output_filename(extension):
        Spider_Name = os.path.basename(os.getcwd())
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")
        outputfile = "{}_{}".format(Spider_Name, formatted_datetime)
        return outputfile + extension

    @staticmethod
    def json_file():
        return SaveFile.generate_output_filename(".json")

    @staticmethod
    def xlsx_file():
        return SaveFile.generate_output_filename(".xlsx")