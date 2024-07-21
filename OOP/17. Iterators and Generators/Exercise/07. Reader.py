def read_next(*args):

    for seq in args:
      for item in seq:
          yield item

for item in read_next('abc', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
    print(item)