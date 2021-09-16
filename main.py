from banker import Banker
from constants import *

def printCommands():
  print()
  print('Commands available:')
  print('List All - Lists all accounts')
  print('List <person> - Lists all transactions for that person')
  print('Quit - End program')

def isValidCommand(command) -> bool:
  if command.lower().startswith('list '):
    return True
  if command.lower() == 'quit':
    return True
  print('Invalid command')
  return False

def getCommand() -> str:
  command = ''
  while not isValidCommand(command):
    command = input('Please enter command: ')
  return command

def performCommand(command, banker):
  if command.lower() == 'list all':
    banker.printAllAccounts()
  elif command.startswith('list '):
    banker.printAllTransactions(command[5:])

def main():
  banker = Banker()
  banker.readFile(CSV_FILE_PATH)
  command = ''
  while command.lower() != 'quit':
    printCommands()
    command = getCommand()
    performCommand(command, banker)

if __name__ == "__main__":
  main()