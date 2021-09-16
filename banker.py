import csv
from transaction import Transaction

class Banker:
  transactions = []

  def readFile(self, csvFilePath):
    with open(csvFilePath, newline='') as csvFile:
      reader = csv.DictReader(csvFile)
      for row in reader:
        newTransaction = Transaction()
        newTransaction.date = row['Date']
        newTransaction.personFrom = row['From']
        newTransaction.personTo = row['To']
        newTransaction.narrative = row['Narrative']
        newTransaction.amount = int(float(row['Amount']) * 100.0)
        self.transactions.append(newTransaction)

  def printAllAccounts(self):
    accounts = {}
    for transaction in self.transactions:
      if accounts.get(transaction.personFrom) is None:
        accounts[transaction.personFrom] = 0
      if accounts.get(transaction.personTo) is None:
        accounts[transaction.personTo] = 0
      accounts[transaction.personFrom] -= transaction.amount
      accounts[transaction.personTo] += transaction.amount

    for account in accounts:
      amount = float(accounts[account]) / 100
      if amount >= 0:
        print(f'{account} is owed £{amount} from the bank')
      else:
        print(f'{account} owes £{-amount} to the bank')

  def printAllTransactions(self, person):
    print(f'Showing all transactions for {person}')
    for transaction in self.transactions:
      if (transaction.personFrom.lower() == person.lower() or
              transaction.personTo.lower() == person.lower()):
        print(transaction)
