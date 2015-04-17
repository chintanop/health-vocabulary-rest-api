from django.db import models

class MRREL (models.Model):
	CUI1 	= models.CharField(max_length=8)
	REL  	= models.CharField(max_length=2)
	RELA  	= models.CharField(max_length=100)
	CUI2 	= models.CharField(max_length=8)
	SAB 	= models.CharField(max_length=20)

	class Meta:
		db_table = 'MRREL'

class MRCONSO (models.Model):
	CUI 	= models.CharField(max_length=8)
	STR 	= models.TextField()
	CODE 	= models.CharField(max_length=50)
	LAT 	= models.CharField(max_length=3)
	ISPREF  = models.CharField(max_length=1)
	SAB 	= models.CharField(max_length=20)
	class Meta:
		db_table = 'MRCONSO'

class ISA(models.Model):
	""" The expanded ISA table """
	CHILD_CUI 	= models.CharField(max_length=8, db_index=True)
	PARENT_CUI 	= models.CharField(max_length=8, db_index=True)
	SAB 		= models.CharField(max_length=20, db_index=True)
	class Meta:
		db_table = 'ISA'


"""class MRSTY (models.Model):
	CUI 	= models.CharField(max_length=8)
	TUI 	= models.CharField(max_length=3)
	STY 	= models.CharField(max_length=50)
	class Meta:
		db_table = 'MRSTY

class MRCOC (models.Model):
	CUI1 	= models.CharField(max_length=8)
	CUI2 	= models.CharField(max_length=8)
	COF 	= models.IntegerField()
	CVF 	= models.IntegerField()
	class Meta:
		db_table = 'MRCOC'
'"""


