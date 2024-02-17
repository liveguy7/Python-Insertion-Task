
def insert(arr, element):
  arr.append(element)

if __name__ == '__main__':
  collection = [0,0,0]
  x = 0
  print("Array before insertion: ")
  for x in range(len(collection)):
    print("collection", [x], " = ", collection[x])
    
  print("inserting...")
  for x in range(len(collection)):
    collection.append(x)
    collection[x] = x + 1
    
  for x in range(len(collection)):
    print("collection", [x], " = ", collection[x])


