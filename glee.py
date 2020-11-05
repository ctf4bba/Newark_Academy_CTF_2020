import angr
import claripy

length = 0x40
p = angr.Project("./glee")
flag = claripy.BVS("flag", length*8)
state = p.factory.entry_state(args=[p.filename, flag])

for i, x in enumerate(flag.chop(8)):
  if i == length - 1:
    state.add_constraints(x == b'}')
    continue

  if i < 6:
    state.add_constraints(x == b'nactf{'[i])
  else:
    flag_format = claripy.Or(
      claripy.And(x >= b'A', x <= b'Z'),
      claripy.And(x >= b'a', x <= b'z'),
      claripy.And(x >= b'0', x <= b'9'),
      x == b'_',
      x == b'+',
      x == b'-',
      x == b'&',
      x == b'!',
      x == b'?'
    )
    state.add_constraints(flag_format)

simgr = p.factory.simulation_manager(state)

simgr.explore(find=0x40128a, avoid=[0x4012b6])

try:
  simstate = simgr.found[0]

  print(simstate.posix.dumps(1))
  print(simstate.solver.eval(flag, cast_to=bytes))
except Exception as e:
  print(e)