# fizzbuzz
# Built with Seahorse v0.1.6
#
# On-chain, persistent FizzBuzz!

from seahorse.prelude import *

# This is your program's public key and it will update
# automatically when you build the project.
declare_id('CrCJxyNHffjZtG6H6puaQvV3T6pdsq9aZEvakxi7mJBk');

class Calculator(Account):
  owner: Pubkey
  display: i64

class Operation(Enum):
  ADD = 0
  SUB = 1
  MUL = 2
  DIV = 3

@instruction
def init_calculator(owner: Signer, calculator: Empty[Calculator]):
   calculator = calculator.init(
    payer = owner,
    seeds = ['calculator-account', owner]
  ) 
   calculator.owner = owner.key()

@instruction
def reset_calculator(owner: Signer, calculator: Calculator):
  print(owner.key(), 'is resetting', calculator.key())
  # Verify owner
  assert owner.key() == calculator.owner, 'This is not your calculator!'
  calculator.display = 0

@instruction
def do_operation(owner: Signer, calculator: Calculator, op: Operation, num: i64):
  # Verify owner, like before
  assert owner.key() == calculator.owner, 'This is not your calculator!'
  if op == Operation.ADD:
    calculator.display += num
  elif op == Operation.SUB:
    calculator.display -= num
  elif op == Operation.MUL:
    calculator.display *= num
  elif op == Operation.DIV:
    calculator.display //= num



