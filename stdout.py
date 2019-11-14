class Cout:
  def __lshift__(s, v):
    print(v)
    return v


class Endl:
  def __lshift__(s, v):
    return str(v) + '\n'

  def __rlshift__(s,v):
    return str(v) + '\n'

cout = Cout()
endl = Endl()

cout << 'Hello, world!' << endl;
