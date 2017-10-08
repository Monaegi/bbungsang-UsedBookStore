from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django_messages.forms import ComposeForm
from django_messages.models import Message
from django.utils.translation import ugettext as _


def delete_message(request, message_id, ):
    if request.method == 'POST':
        pass


def create_reply(request, message_id, template_name='django_messages/compose.html',
                 success_url=None, subject_template=_(u"Re: %(subject)s")):

    parent = get_object_or_404(Message, id=message_id)

    if parent.sender != request.user and parent.recipient != request.user:
        raise Http404

    if request.method == "POST":
        data = {
            'recipient': request.POST.get('recipient', ''),
            'subject': request.POST.get('subject', ''),
            'body': request.POST.get('body', ''),
        }

        compose_form = ComposeForm(data)

        if compose_form.is_valid():
            compose_form.save(sender=request.user, parent_msg=parent)
            messages.info(request, _(u"Message successfully sent."))
            if success_url is None:
                success_url = reverse('messages_inbox')
            return HttpResponseRedirect(success_url)

    context = {
        'message_id': message_id,
        'subject': subject_template % {'subject': parent.subject},
        'recipient': parent.sender.username,
    }

    return render(request, template_name, context)


def inbox(request, template_name='django_messages/inbox.html'):
    all_message_lists = Message.objects.inbox_for(request.user)
    p = Paginator(all_message_lists, 7)
    page_num = request.GET.get('page')

    try:
        message_list = p.page(page_num)
    except PageNotAnInteger:
        message_list = p.page(1)
    except EmptyPage:
        message_list = p.page(p.num_pages)

    return render(request, template_name, {
        'message_list': message_list,
    })
