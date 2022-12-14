class DefaultDict(dict):

  def __init__(self, default):
    if isinstance(default, type):
      self.default_value = None
      self.default_func = None
      self.default_type = default
    elif callable(default):
      self.default_value = None
      self.default_func = default
      self.default_type = None
    else:
      self.default_value = default
      self.default_func = None
      self.default_type = None

  def __missing__(self, key):
    if self.default_value is not None:
      self[key] = self.default_value
    elif self.default_func is not None:
      self[key] = self.default_func(key)
    else:
      self[key] = self.default_type()
    return self[key]
