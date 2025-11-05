from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, empid, name, dob, date_hired, address, m_number):
        self.__empid = empid
        self.__name = name
        self.__dob = dob
        self.__date_hired = date_hired
        self.__address = address
        self.__m_number = m_number

    @abstractmethod
    def get_annual_leave(self):
        pass

    def get_cpf_contribution(self):
        return 10  # Just to get by

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Employee) == False:
            return False
        return self.__empid == other.__empid


class ProfessionalEmp(Employee):
    def __init__(self, empid, name, dob, date_hired, address, m_number, prof_position, working_days):
        super().__init__(empid, name, dob, date_hired, address, m_number)
        self.__prof_position = prof_position
        self.__working_days = working_days

    def get_annual_leave(self):
        return 15  # Just to get by


class AcademicEmp(Employee):
    def __init__(self, empid, name, dob, date_hired, address, m_number, acad_position):
        super().__init__(empid, name, dob, date_hired, address, m_number)
        self.__acad_position = acad_position
        self.__tsubjects = []
        self.__rsubjects = []

    def get_annual_leave(self):
        return 0


class School:
    def __init__(self, name):
        self.__name = name
        self.__employees = []

    def add_emp(self, employee):
        if employee in self.__employees:
            return False
        else:
            self.__employees.append(employee)
            return True


def main():
    uow = School('UOW')
    uow.add_emp(ProfessionalEmp('e1', 'n1', 'dob1', 'dh1', 'add1', 'm1', 'p', 5))
    uow.add_emp(AcademicEmp('e2', 'n1', 'dob1', 'dh1', 'add1', 'm1', 'p'))
    result = uow.add_emp(AcademicEmp('e2', 'n1', 'dob1', 'dh1', 'add1', 'm1', 'p'))
    print(result)


if __name__ == "__main__":
    main()