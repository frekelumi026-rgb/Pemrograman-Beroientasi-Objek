UMR = 3_500_000

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.__salary = 0
        self.set_salary(salary)

    def set_salary(self, value: float) -> None:
        if value < UMR:
            print(f"Gagal: gaji {self.name} di bawah UMR")
        else:
            self.__salary = value

    def get_salary(self) -> float:
        return self.__salary


class Company:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__employees = []

    def add_employee(self, employee) -> None:
        if isinstance(employee, Employee):
            self.__employees.append(employee)
        else:
            print("Gagal: bukan objek Employee")

    def _calculate_payroll(self) -> float:
        total = 0
        for emp in self.__employees:
            total += emp.get_salary()
        return total

    def show_payroll(self) -> None:
        print(f"Total gaji: Rp{self._calculate_payroll():,.0f}")


# --- Contoh Pemakaian ---
company = Company("PT Info Sejahtera")

company.add_employee(Employee("Peke", 4_500_000))
company.add_employee(Employee("Saya", 3_800_000))
company.add_employee("bukan employee")   # akan ditolak isinstance()

company.show_payroll()
