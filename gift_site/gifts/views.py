# gifts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Gift, GiftItem
from .forms import GiftForm, GiftItemForm
from django.conf import settings

def home(request):
    if request.method == 'POST':
        link_name = request.POST.get('link_name')
        gift_form = GiftForm(request.POST, request.FILES)
        if gift_form.is_valid():
            gift = gift_form.save(commit=False)
            gift.link_name = link_name
            gift.save()

            # Обработка подарков
            gift_items = request.POST.getlist('gift_name')
            gift_links = request.POST.getlist('gift_link')
            gift_images = request.FILES.getlist('gift_image')

            for i in range(len(gift_items)):
                if gift_items[i] or gift_links[i] or (i < len(gift_images) and gift_images[i]):
                    gift_item = GiftItem(
                        gift=gift,
                        name=gift_items[i],
                        link=gift_links[i],
                        image=gift_images[i] if i < len(gift_images) else None
                    )
                    gift_item.save()

            return redirect(f'/{link_name}/')
    else:
        gift_form = GiftForm()
        gift_item_form = GiftItemForm()

    return render(request, 'home.html', {'gift_form': gift_form, 'gift_item_form': gift_item_form})

def gift_list(request, link_name):
    gift = get_object_or_404(Gift, link_name=link_name)
    avatar_url = gift.gift_image.url if gift.gift_image else settings.STATIC_URL + 'images/default_avatar.png'
    return render(request, 'gift_list.html', {'gift': gift, 'avatar_url': avatar_url})