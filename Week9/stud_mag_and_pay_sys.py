## stundent_marks should be in between 0-100 in number format
import random
import time



class InvalidMarksError(Exception):
    "Raised when the marks are not in between 0-100"
    pass

class InsufficientBalanceError(Exception):
    "Raised when the balance is less than exam fee "
    pass

def get_valid_marks(subject_name: str) -> float:
    """Get valid marks from the user, Validate marks must be in between 0-100"""

    while True:
        try:

            raw_marks = input(f"Enter the marks for {subject_name} in between 0-100:")
            marks = float(raw_marks)

            if marks < 0 or marks > 100:
                raise InvalidMarksError(f"Invalid marks for {subject_name}, must be in between 0-100")

            return marks 

        except ValueError as e:
            print(f"Error: {e}")
        except InvalidMarksError as e:
            print(f"Error: {e}")


def simulate_bank_api(amount:float) -> str:

    """ Simulated Bank API Payment Processing, 50% chance of seccuss, 50% chance of failure"""

    if random.choice([True, False]):
        raise ConnectionError("Bank API is not available / Bank Gateway Timeout / Network Interrupted")

    return f"Payment of ruppes {amount:.2f} processed successfully"

def process_payment_with_retry(amount: float, max_attempt: int = 3 ) -> str :
    """ Process payment with retry, if payment fails, retry with exponential backoff"""
    
    for attempt in range(1, max_attempt + 1):
        try:
            print(f"Attempt {attempt} of {max_attempt} to processing payment of rupees {amount:.2f}")
            result = simulate_bank_api(amount)
            return result
        except ConnectionError as e:
            print(f"Attempt {attempt} of Failed: {e}")

            if attempt < max_attempt:
                wait = 2 **(attempt -1)
                time.sleep(wait)
            else:
                raise ConnectionError("Max attempt reached, payment failed..!")

def main():
    print("="*50)
    print("Wel-Come to the Student Marks and Payment System")
    print("="*50)

    student_bank_balance = 1000.00
    per_subject_exam_fee = 200

    try:
        marks_phy = get_valid_marks("Physics")
        marks_che = get_valid_marks("Chemistry")
        marks_math = get_valid_marks("Maths")

        total_marks = marks_phy + marks_che + marks_math
        percentage = (total_marks / 300) * 100

        if percentage < 50  or marks_phy < 50 or marks_che < 50 or marks_math < 50 :
            print("Sorry, You are failed in the exam")
            print("You need to pay the exam fee again")
        else:
            print(f"Congratulatiions, You are passed in the exam with {percentage:.2f}%")
            print("You don't need to pay exam fee again...!")
            return None

        total_fee = per_subject_exam_fee * 3

        if student_bank_balance < total_fee:
            raise InsufficientBalanceError(f"Insufficient balance is the bank account, you need to pay {total_fee:.2f}rupees")

        receipt = process_payment_with_retry(total_fee)
        #print(receipt)

    except InsufficientBalanceError as e:
        print(f"Registration is Canceled: {e}")
    except ConnectionError as e:
        print(f"Network Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else:
        print("Registration Successful")
        print(f"Student registration receipt: {receipt}")

    finally:
        print("Session closed securly. Thank you for using our system...!")


if __name__ == "__main__":
    
    main()