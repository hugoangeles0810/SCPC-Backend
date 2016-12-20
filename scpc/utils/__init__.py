def setallattr(obj, **kwargs):
  for k in kwargs:
    setattr(obj, k, kwargs.get(k))