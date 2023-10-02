from django.db import models

# Create your models here.


class Raid_tool(models.Model):
    tool_name = models.CharField(max_length=64)
    tool_val = models.CharField(max_length=64)
    tool_img = models.ImageField(upload_to='tool_images')
    tool_res = models.JSONField()
    tool_drop_id = models.IntegerField(default=0)

    def __str__(self):
        return self.tool_name


class Raid_object(models.Model):
    obj_name = models.CharField(max_length=64)
    obj_val = models.CharField(max_length=64)
    obj_img = models.ImageField(upload_to='obj_images')
    obj_raid = models.JSONField()
    obj_drop_id = models.IntegerField(default=0)

    def __str__(self):
        return self.obj_name


class Resource(models.Model):
    res_name = models.CharField(max_length=64)
    res_val = models.CharField(max_length=64)
    res_img = models.ImageField(upload_to='res_images')
    res_sort_id = models.IntegerField(default=0)   #id приоритета расположения ресурсов на странице

    def __str__(self):
        return self.res_name
