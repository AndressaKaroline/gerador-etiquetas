import Pyro4
from random import randint

cont = 0
@Pyro4.expose
class GeneratorTags(object):
  # cont = 0

  def generate_tags(self, result):
    while(result == 's'):
      global cont
      cont += 1
      return cont
    return "Ok, volte sempre!"

daemon = Pyro4.Daemon()
uri = daemon.register(GeneratorTags)

print("Ready. Object uri =", uri)
daemon.requestLoop()