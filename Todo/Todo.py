# fizzbuzz
# Built with Seahorse v0.2.1
#
# On-chain, persistent FizzBuzz!

from seahorse.prelude import *

# This is your program's public key and it will update
# automatically when you build the project.
declare_id('816ES5PuccseqmtEdJkHnDT2cDwF5cppDu6Xh4s6ahRS');


class UserProfile(Account):
  owner: Pubkey
  last_todo:u8
  todo_count:u8

class TodoAccount(Account):
  owner: Pubkey
  idx:u8
  content:str
  marked:bool

@instruction
def init_tasks(owner:Signer,tasks:Empty[Tasks]):
  tasks=tasks.init(
    payer=owner,
    seeds=['tasks-account',owner]
  )

@instruction
def init_userprofile(owner:Signer,userprofile:Empty[UserProfile]):
  userprofile=userprofile.init(
    payer=owner,
    seeds=['userprofile',owner])
  userprofile.owner=owner.key()
  userprofile.last_todo=0
  userprofile.todo_count=0

@instruction
def init_todoaccount(owner:Signer,todoaccount:Empty[TodoAccount],num:u64):
  todoaccount=todoaccount.init(
    payer=owner,
    seeds=['todoaccount',owner]
  )
  
@instruction
def add_task(owner:Signer,userprofile:UserProfile,todoaccount:TodoAccount,task:Tasks,content:str):
  todoaccount.content=content
  todoaccount.idx=userprofile.last_todo
  todoaccount.owner=owner.key()
  userprofile.last_todo+=1
  userprofile.todo_count+=1

@instruction
def mark_task(owner:Signer,userprofile:UserProfile,todoaccount:TodoAccount):
  todoaccount.marked=True
  userprofile.todo_count-=1
  todoaccount.idx=userprofile.last_todo

