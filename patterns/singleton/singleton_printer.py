import threading


class PrinterService:
	_instance_lock = threading.Lock()
	_unique_instance = None

	def __init__(self):
		self.mode = None

	def __new__(cls, *args, **kwargs):
		with cls._instance_lock:
			if cls._unique_instance is None:
				cls._unique_instance = super(PrinterService, cls).__new__(cls)
				cls._unique_instance._init_printer_service()
		return cls._unique_instance

	def _init_printer_service(self):
		self.mode = "GrayScale"

	def get_printer_status(self):
		return self.mode

	def set_mode(self, mode):
		self.mode = mode
		print(f"Mode changed to {mode}")


pool1 = PrinterService()
pool2 = PrinterService()

pool1.set_mode("Color")
pool2.set_mode("Grayscale")

print(pool1.get_printer_status())
print(pool2.get_printer_status())