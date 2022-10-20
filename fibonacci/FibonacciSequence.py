from seahorse.prelude import *

# This is your program's public key and it will update
# automatically when you build the project.
declare_id('5ZcrBhwVeYroRKqJjCTSbHnD7JCy5nSBiJwfckQzxP44');

class Seq(Account):
  data:Array[i64,2]

@instruction
def init_account(owner:Signer,seq:Empty[Seq]):
  seq=seq.init(
    payer=owner,
    seeds=['seq-account',owner]
  )
  seq.data[0]=0
  seq.data[1]=1

@instruction
def reset(seq:Seq):
  seq.data[0]=0
  seq.data[1]=1

@instruction
def advance(seq:Seq):
  print("Next Value : ",seq.data[0])
  seq.data[0]=seq.data[1]
  seq.data[1]=seq.data[0]+seq.data[1]

  
