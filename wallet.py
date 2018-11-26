#Wallet Program
#A program that allows the user to add user wallets.  
#User can view wallets and withdraw or deposit money.

class Wallet:
	def __init__(self, name, money):
		self.name = name
		self.money = money

	def withdraw(self, withdraw):
		self.money = self.money - withdraw
		print("%s has withdrawn %s and now has $%d remaining" % (self.name, withdraw, self.money))

	def deposit(self, deposit):
		self.money = self.money + deposit
		print("%s has deposited %s and now has $%d remaining" % (self.name, deposit, self.money))

#initalize wallet dictionary
walletDict = {}

def main():

	while(True):
		print("\nWhat would you like to do?\n", 
		"1. Add Wallet\n",
		"2. View Wallets\n",
		"3. Withdraw Money\n", 
		"4. Deposit Money\n", 
		"5. Exit")

		#Selection Validation
		while True:
			try:
				uInput = int(input("Selection: "))
			except ValueError:
				print("Enter a Valid Number.")
				continue
			break
		
		#Selection 1
		if uInput == 1:
			uName = input("Owner Name: ")
			walletDict[uName] = Wallet(uName, 0) 

		#Selection 2
		elif uInput == 2:
			print()
			for key,val in walletDict.items():
				print(key, "Balance:", val.money)
		
		#Selection 3
		elif uInput == 3:
			print("Withdraw from which owner?")
			uName = input("Owner: ")
			
			if uName not in walletDict:
				print("Owner does not exist.")
			
			else:
				while(True):
					try:
						amount = int(input("How much would you like to withdraw?\n"))
					except ValueError:
						print("Enter a Valid Number.")
						continue
					break	
				walletDict[uName].withdraw(amount)

		#Selection 4
		elif uInput == 4:
			print("Deposit to which owner?")
			uName = input("Owner: ")
			
			if uName not in walletDict:
				print("Owner does not exist.")
			
			else:
				while(True):
					try:
						amount = int(input("How much would you like to deposit?\n"))
					except ValueError:
						print("Enter a Valid Number.")
						continue
					break	
				walletDict[uName].deposit(amount)

		#Selection 5 
		elif uInput == 5:
			break;
		
		#Invalid Selection
		else:
			print("Invalid Input")

if __name__ == "__main__":
	main()


#Testing Class
"""
joey = Wallet("Joey", 400)
susan = Wallet("Susan", 3000)

susan.withdraw(300)
joey.withdraw(44)
susan.withdraw(32)
joey.withdraw(46)

"""
