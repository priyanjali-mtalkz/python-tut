class Subject:
    def __init__(self,sub_name,year,department):
        self.sub_name = sub_name
        self.year = year
        self.department = department
    def sub(self):
        return f'Subject_name : {self.sub_name}' \
            f'Year : {self.year}' \
                f'Deaprtment : {self.department}'



