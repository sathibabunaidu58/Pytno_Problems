class YourException(Exception):
  def __init__(self, message):
    self.message = message

try:
  raise YourException("Something is fishy")

except YourException as err:
  # perform any action on YourException instance
  print("Message:", err.message)