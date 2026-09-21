UMR_MANADO: float = 3_500_000.0

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name: str = name
        self.__salary: float = 0.0          
        self.set_salary(salary)             

    # ---------- Setter ----------
    def set_salary(self, value: float) -> None:
        """Validasi: gaji tidak boleh di bawah UMR."""
        if value < UMR_MANADO:
            print(f"  [PERINGATAN] Gaji {self.name} (Rp{value:,.2f}) di bawah "
                  f"UMR (Rp{UMR_MANADO:,.2f}). Input ditolak, gaji tidak diubah.")
        else:
            self.__salary = value

    # ---------- Getter ----------
    def get_salary(self) -> float:
        """Baca gaji privat tanpa membuka akses tulis langsung."""
        return self.__salary

    def __repr__(self) -> str:
        return f"Employee(name='{self.name}', salary=Rp{self.__salary:,.2f})"


class Company:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.__employees: list[Employee] = []   # enkapsulasi array karyawan

    # ---------- Metode Publik (Antarmuka) ----------
    def add_employee(self, employee: object) -> None:
        """Hanya menerima objek yang benar-benar instance dari Employee."""
        if isinstance(employee, Employee):
            self.__employees.append(employee)
            print(f"  [OK] {employee.name} berhasil ditambahkan ke {self.name}.")
        else:
            print(f"  [GAGAL] Objek '{employee}' bukan instance dari Employee, "
                  f"ditolak masuk ke inventaris.")

    def get_employee_count(self) -> int:
        return len(self.__employees)

    def print_payroll_report(self) -> None:
        """Satu-satunya jalur resmi bagi pihak luar untuk melihat hasil payroll.
        Method ini memanggil _calculate_payroll() dari dalam class sendiri."""
        total = self._calculate_payroll()
        print(f"\n=== Laporan Payroll {self.name} ===")
        for emp in self.__employees:
            print(f"  - {emp.name:<15} Rp{emp.get_salary():,.2f}")
        print(f"  {'TOTAL':<17} Rp{total:,.2f}\n")

    # ---------- Private Method ----------
    def _calculate_payroll(self) -> float:
        """Logika internal penjumlahan gaji. Secara konvensi Python (single
        underscore) method ini menandakan 'jangan dipanggil dari luar class',
        meskipun Python tetap mengizinkan akses (gentleman's agreement)."""
        return sum(emp.get_salary() for emp in self.__employees)


# =============================================================
# LIVE DEMO: Akses Aman (via method) vs Akses Langsung/Invalid
# =============================================================
if __name__ == "__main__":
    company = Company("PT Info Sejahtera")

    print("--- 1. Menambahkan Karyawan Valid ---")
    e1 = Employee("Peke", 4_500_000)
    e2 = Employee("Rian", 3_800_000)
    company.add_employee(e1)
    company.add_employee(e2)

    print("\n--- 2. Kasus Kegagalan: Setter menolak gaji di bawah UMR ---")
    e3 = Employee("Budi", 2_000_000)      # otomatis ditolak oleh set_salary()
    company.add_employee(e3)              # tetap masuk list, tapi gaji tetap 0.0

    print("\n--- 3. Kasus Kegagalan: isinstance() menolak objek bukan Employee ---")
    company.add_employee("Bukan Objek Employee")   # string, bukan Employee
    company.add_employee({"name": "Palsu"})        # dict, bukan Employee

    print("\n--- 4. Akses Resmi (Aman): lewat method publik ---")
    company.print_payroll_report()

    print("--- 5. Akses Langsung (Tidak Disarankan): Name Mangling ---")
    try:
        print(company.__employees)        # AttributeError, atribut tersembunyi
    except AttributeError as err:
        print(f"  Error: {err} -> Terbukti list karyawan terlindungi dari akses luar.")

    # Akses via name mangling tetap mungkin, tapi melanggar kontrak:
    print(f"  (Contoh pelanggaran kontrak) company._Company__employees = "
          f"{company._Company__employees}")

    print("\n--- 6. Private Method tetap 'terlihat' tapi TIDAK direkomendasikan dipanggil ---")
    hasil_manual = company._calculate_payroll()   # bisa dipanggil, tapi melanggar konvensi
    print(f"  Total dihitung manual dari luar (TIDAK DISARANKAN): Rp{hasil_manual:,.2f}")
    print(f"  Total dihitung resmi dari getter jumlah karyawan: {company.get_employee_count()} karyawan")
