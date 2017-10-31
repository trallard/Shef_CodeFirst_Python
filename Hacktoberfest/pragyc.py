# Starbucks bot
name=input("Can I have your name please?")
order=input("Can I have your order please?")
milk=input("Would you like whole milk or almond milk with your order?")

def starbucks_bot(name,order,milk):
  print("Your name is {}. You would like {} with {} milk. Thank you, please wait while we get your order prepared".format(name, order, milk))

starbucks_bot(name,order,milk)
