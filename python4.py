class FeeCalculator:
    def __init__(self, name, rollno, fee, percentage):
        self.name = name
        self.rollno = rollno
        self.fee = fee
        self.percentage = percentage

    def TotalFee(self):
        if self.percentage <= 50:
            return self.fee + (0.20 * self.fee)
        elif self.percentage <= 75:
            return self.fee + (0.15 * self.fee)
        else:
            return self.fee


# Input section
name = input()
rollno = int(input())
fee = int(input())
percentage = float(input())

# Create object using constructor
student1 = FeeCalculator(name, rollno, fee, percentage)

# Print result with 1 decimal
print(f"{student1.TotalFee():.1f}")
