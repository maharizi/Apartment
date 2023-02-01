from datetime import datetime


class Log_manage:

    def __init__(self):
        self.f = None
        self.time = datetime.now().strftime(" %d/%m/%Y %H:%M:%S ")

    def open_file(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: open logs file
                Return: Null"""
        try:
            self.f = open('logs', 'a')
            return 1
        except FileExistsError:
            print('')

    def write_to_log(self, city, message, value):
        """Author: Maor Maharizi,
                Created: 30.01.2023,
                Detail: write to logs file
                Return: Null"""
        self.f.write(f"\n {city} ! --- {message} --- value : {value} --- " + self.time)
        self.f.write("")
        self.f.flush()

    def close_log_file(self):
        """Author: Maor Maharizi,
                Created: 22.01.2023,
                Detail: close logs file
                Return: Null"""
        self.f.close()
