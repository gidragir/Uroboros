class functions:
  def requestSerialization(data):
       
    items = data.items()
        
    serialization = {}
    
    for item in items:
      serialization[item[0]] = item[1]

    return serialization
