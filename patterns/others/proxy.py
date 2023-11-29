import time


class Producer:
	"""Define the resource intensive object to instantiate"""

	def produce(self):
		print("Producer is working hard!")

	def meet(self):
		print("Producer has time to meet you now")


class Proxy:
	"""Define the relatively less resource intensive proxy"""

	def __init__(self):
		self.occupied = 'No'
		self.producer = None

	def produce(self):
		"""Check if producer is available"""
		print("Artist checking if Producer is available")

		if self.occupied == 'No':
			# if producer is available, create a producer object
			self.producer = Producer()
			time.sleep(2)
			# make the producer meet the guest
			self.producer.meet()
			return True
		else:
			# otherwise don't instantiate a producer
			time.sleep(2)
			print("Producer is busy!")
		return False