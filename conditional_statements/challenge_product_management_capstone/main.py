# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

is product_type == "perishable":
  if (days_until_expiration <= 3 and stock_level < 50):
      print ("Apply 30% discount")
      
    