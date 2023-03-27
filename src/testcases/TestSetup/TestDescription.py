def description(desc):
  def decorator(func):
      func.__doc__ = desc
      return func
  return decorator
