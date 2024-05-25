# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    # savings_balance = float(input("Please enter the account balance for Savings "))
    # savings_interest = float(input("Please enter the Saving interest rate "))
    # savings_maturity = int(input("Please enter the term in months for Saving "))
    savings_balance = 100
    savings_interest = 5
    savings_maturity = 10

    
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"You have earned ${interest_earned:,.2f} and your Saving account balance is ${updated_savings_balance:,.2f}.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    # cd_balance = float(input("Please enter the account balance for your CD "))
    # cd_interest = float(input("Please enter the CD interest rate "))
    # cd_maturity = int(input("Please enter the term in months for your CD "))
  
    cd_balance = 100
    cd_interest = 5
    cd_maturity = 100

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"You have earned ${interest_earned:,.2f} and your CD balance is ${updated_cd_balance:,.2f}.")

if __name__ == "__main__":
    # Call the main function.
    main()