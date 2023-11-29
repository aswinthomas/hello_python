from abc import ABC, abstractmethod


class JSONLogger(ABC):
	"""Target interface"""

	@abstractmethod
	def log_message(self, message: str) -> None:
		pass


# Create a concrete class that implements JSONLogger
class ConcreteJSONLogger(JSONLogger):
	def log_message(self, message: str) -> None:
		print(f"Logging JSON: {message}")


class XMLLogger:
	"""Adaptee"""

	def log(self, xml_message: str) -> None:
		print(f"Logging XML: {xml_message}")


class LoggerAdapter(JSONLogger):
	"""Adapter"""

	def __init__(self, xml_logger: XMLLogger) -> None:
		self.xml_logger = xml_logger

	def log_message(self, message: str) -> None:
		self.xml_logger.log(f"<message>{message}</message>")


# Existing client code that expects JSONLogger
def client_code(logger: JSONLogger, message: str) -> None:
	logger.log_message(message)


# Using JSONLogger with the existing client code
json_logger = ConcreteJSONLogger()
client_code(json_logger, "Hello, JSON!")

# Introducing XMLLogger using the adapter
xml_logger = XMLLogger()
json_adapter_logger = LoggerAdapter(xml_logger)
client_code(json_adapter_logger, "Hello, XML!")
