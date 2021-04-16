class inputProcessor:
  bindings = {}
  active_keys = set([])

  def __init__(self):
    raw_binding = open('input-mapping', 'r').read().split('\n')
    for bind in raw_binding:
      bind = bind.split(',')
      self.bindings[bind[0].strip()] = bind[1].strip()
  
  def press_key(self, key):
    if key in self.active_keys:
      return
    
    print(f'pressed {key}')
    self.active_keys.add(key)

  def release_key(self, key):
    self.active_keys.remove(key)
  
  def process_input(self, key_input):
    try:
      key, status = key_input.split('$')
      key = key.upper()
      if not(key in self.bindings.keys()):
        return
      key = self.bindings[key]

      if status == '1':
        self.press_key(key)
      else:
        self.release_key(key)
    except:
      pass