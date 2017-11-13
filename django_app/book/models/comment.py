import re
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import redirect
from django_extensions.db.models import TimeStampedModel
from django_messages.forms import ComposeForm

from book.models import SellBookRegister

MyUser = get_user_model()


class Comment(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    sell_book = models.ForeignKey(
        SellBookRegister,
        on_delete=models.CASCADE,
    )

    content = models.TextField()
    star_score = models.IntegerField()

    def send_message_after_making_name_tag(self):
        p = re.compile(r'(^@\w+)')
        tag_name_list = re.findall(p, self.content)
        ori_content = self.content

        for tag_name in tag_name_list:
            tag = tag_name.replace('@', '')
            change_tag = "<a href='#' class='name-tag'>{tag_name}</a>".format(
                tag_name=tag_name,
            )
            ori_content = ori_content.replace(tag_name, change_tag)
            user = MyUser.objects.get(nickname=tag)

            data = {
                'recipient': user.username,
                'subject': '회원님이 언급되었습니다.',
                'body': self.content,
            }
            compose_form = ComposeForm(data)
            sender = MyUser.objects.get(pk=1)

            if compose_form.is_valid():
                compose_form.save(sender=sender)

        self.content = ori_content
        return self.content

    def save(self, *args, **kwargs):
        try:
            self.send_message_after_making_name_tag()
        except MyUser.DoesNotExist:
            return redirect('book:sell_book_detail', sell_pk=self.sell_book.pk)
        super().save(*args, **kwargs)



