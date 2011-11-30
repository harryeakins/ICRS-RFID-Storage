from django.db import models

USER_TYPES = (
	("admin", "Administrator"),
	("user", "Normal User"),
	("basic_user", "Basic User"),
)
class User(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	serial_number = models.CharField(max_length=50)
	email_address = models.EmailField()
	user_type = models.CharField(max_length=30, choices=USER_TYPES)
	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name)

class StorageLocation(models.Model):
	name = models.CharField(max_length=200)
	human_readable_name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)

class ItemType(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

class Item(models.Model):
	barcode = models.CharField(max_length=50)
	storage_location = models.ForeignKey(StorageLocation)
	item_type = models.ForeignKey(ItemType)
	present = models.BooleanField()
	working = models.BooleanField()

class BorrowingRecord(models.Model):
	storage_location = models.ForeignKey(User)
	storage_location = models.ForeignKey(Item)
	borrow_timestamp = models.DateTimeField(auto_now_add=True)
	return_timestamp = models.DateTimeField()

	
