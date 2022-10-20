
from seahorse.prelude import *

# This is your program's public key and it will update
# automatically when you build the project.
declare_id('3hLgLPpKnatHxRADfNTWGUbgk4oVx8zqceWcicqYhbgd');

class Greeting(Account):
  counter: i64

@instruction
def init_account(owner:Signer,greet:Empty[Greeting]):
  greet = greet.init(
    payer = owner,
    seeds = ['greet-account',owner ]
  ) 
  
@instruction
def increment_count(owner:Signer,greet:Greeting):
  greet.counter+=1

@instruction
def decrement_count(owner:Signer,greet:Greeting):
  greet.counter-=1
