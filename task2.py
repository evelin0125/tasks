class HospitalManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self):
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        gender = input("Enter Patient Gender (M/F): ")
        disease = input("Enter Patient Disease/Condition: ")
        patient_id = len(self.patients) + 1
        patient_data = {
            "ID": patient_id,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Disease": disease,
        }
        self.patients.append(patient_data)
        print(f"Patient {name} added successfully with ID {patient_id}.\n")

    def view_patients(self):
        if not self.patients:
            print("No patient records found.\n")
        else:
            print("Patient Records:")
            for patient in self.patients:
                print(f"ID: {patient['ID']}, Name: {patient['Name']}, Age: {patient['Age']}, Gender: {patient['Gender']}, Disease: {patient['Disease']}")
            print()

    def delete_patient(self):
        try:
            patient_id = int(input("Enter Patient ID to delete: "))
            patient = next((p for p in self.patients if p["ID"] == patient_id), None)
            if patient:
                self.patients.remove(patient)
                print(f"Patient with ID {patient_id} deleted successfully.\n")
            else:
                print("Patient ID not found.\n")
        except ValueError:
            print("Invalid input. Please enter a valid ID.\n")

    def menu(self):
        while True:
            print("Hospital Patient Management System")
            print("1. Add Patient")
            print("2. View Patients")
            print("3. Delete Patient")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.view_patients()
            elif choice == "3":
                self.delete_patient()
            elif choice == "4":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    system = HospitalManagementSystem()
    system.menu()
	
