#STUDENT_REPORT

name=input("Enter Student Name :")
name=name.strip()
subject=input("Enter Subject :")
subject=subject.strip()
marks=float(input("Enter Marks :"))

print("="*40)
print("         STUDENT REPORT")
print("="*40)
print(f"Student Name: {name}")
print(f"Subject: {subject}")
print(f"Marks: {marks:.2f}")
print("="*40)

