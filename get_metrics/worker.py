# from django.dispatch import receiver
# from django.db import models
# from collect_opinions.models import Feedback
# from get_metrics.models import Metrics


# @receiver(models.signals.post_save, sender=Feedback)
# def create_empty_metrics(instance, **kwargs):
#     Metrics.objects.create(
#         feedback=instance
#     )

# @receiver(models.signals.post_delete, sender=Photo)
# def delete_images(instance, **kwargs):
#     if instance.image:
#         if os.path.isfile(instance.image.path):
#             os.remove(instance.image.path)

#     if instance.thumbnail:
#         if os.path.isfile(instance.thumbnail.path):
#             os.remove(instance.thumbnail.path)
