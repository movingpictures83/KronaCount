import sys

class KronaCountPlugin:
    def input(self, filename):
        self.kronafile = open(filename, 'r')

    def run(self):
       self.count = 0.0
       for line in self.kronafile:
          contents = line.strip().split('\t')
          self.count += float(contents[0])

    def output(self, filename):
       print(self.count)
