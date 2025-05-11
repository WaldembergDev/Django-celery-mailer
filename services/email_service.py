from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from io import BytesIO
from .image_service import save_image


def send_mail(name: str, title: str, recipients: list):
    html_content = render_to_string(
        'emails/my_email.html',
        context={'name': name}
    )

    text_content = strip_tags(html_content)

    msg = EmailMultiAlternatives(
        title,
        text_content,
        settings.DEFAULT_FROM_EMAIL,
        recipients,
        headers={'List-Unsubscribe': '<mailto:unsub@example.com>'}
    )

    # gerar a imagem na memória
    image_buffer = save_image(name)

    # Anexar a imagem como conteúdo embutido (inline)
    msg.attach(
        'image.png',  # Nome do arquivo
        image_buffer.read(),  # Conteúdo da imagem
        'image/png'  # Tipo MIME
    )
    msg.mixed_subtype = 'related'  # Define o subtipo como "related" para conteúdo inline

    # Substituir o placeholder no HTML pelo identificador correto
    html_content_with_image = html_content.replace('cid:image_placeholder', 'cid:image.png')
    msg.attach_alternative(html_content_with_image, 'text/html')

    msg.send()
