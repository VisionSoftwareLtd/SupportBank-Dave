class Transaction:
  date = ''
  personFrom = ''
  personTo = ''
  narrative = ''
  amount = 0

  def __str__(self):
    return f'{self.date:<10} | {self.personFrom:<10} | {self.personTo:<10} | {self.narrative:<20} | £{float(self.amount) / 100:.2f}'