import Pyro4

uri = input("URI Object? ").strip()
generate = input("Deseja gerar uma etiqueta? (s/n)").strip()

generator_tags = Pyro4.Proxy(uri)
print(generator_tags.generate_tags(generate))

while generate == "s":
  generate = input("Deseja gerar uma etiqueta? (s/n)").strip()
  print(generator_tags.generate_tags(generate))

