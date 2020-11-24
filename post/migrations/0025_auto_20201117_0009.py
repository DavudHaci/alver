# Generated by Django 3.0.7 on 2020-11-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_auto_20201020_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('mnz', 'Mənzillər'), ('tv', 'TV'), ('ovo', 'Obyektlər və ofislər'), ('trp', 'Torpaq'), ('qrj', 'Qarajlar'), ('vvb', 'Villalar, bağ evləri'), ('mvi', 'Mebel və interyer'), ('tvt', 'Temir Ve Tikinti'), ('btk', 'Bitkiler'), ('mt', 'Məişət texnikası'), ('qab', 'Qab-qacaq və mətbəx ləvazimatları'), ('ka', 'Komputer Aksesuarlari'), ('nvn', 'Noutbuklar və Netbuklar'), ('pc', 'Masaüstü kompüterlər'), ('nvs', 'Nömrələr və SİM-kartlar'), ('mnt', 'Komponentlər və monitorlar'), ('ft', 'Foto texnika'), ('vls', 'Velosipedlər'), ('ma', 'Musiqi alətləri'), ('iva', 'İdman və asudə'), ('tlf', 'Telefonlar'), ('pve', 'Planşet və elektron kitablar'), ('oav', 'Ofis avadanlığı və istehlak'), ('op', 'Oyunlar Pultlar ve programlar'), ('ehv', 'Ehtiyat hissələri və aksesuarlar'), ('afv', 'Avtobuslar və xüsusi texnika'), ('avt', 'Avtomobillər'), ('aqr', 'Aqrotexnika'), ('mvm', 'Motoskiletler Ve Mopedler'), ('sn', 'Su nəqliyyatı'), ('itl', 'İtlər'), ('huv', 'Hevanlar ücün Məhsullar'), ('dh', 'Digər heyvanlar'), ('psk', 'Pişiklər'), ('qsl', 'Quşlar'), ('avb', 'Akvarium və balıqlar'), ('dgr', 'Digər')], default=None, max_length=3, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='articlecategory',
            name='category',
            field=models.CharField(choices=[('mnz', 'Mənzillər'), ('tv', 'TV'), ('ovo', 'Obyektlər və ofislər'), ('trp', 'Torpaq'), ('qrj', 'Qarajlar'), ('vvb', 'Villalar, bağ evləri'), ('mvi', 'Mebel və interyer'), ('tvt', 'Temir Ve Tikinti'), ('btk', 'Bitkiler'), ('mt', 'Məişət texnikası'), ('qab', 'Qab-qacaq və mətbəx ləvazimatları'), ('ka', 'Komputer Aksesuarlari'), ('nvn', 'Noutbuklar və Netbuklar'), ('pc', 'Masaüstü kompüterlər'), ('nvs', 'Nömrələr və SİM-kartlar'), ('mnt', 'Komponentlər və monitorlar'), ('ft', 'Foto texnika'), ('vls', 'Velosipedlər'), ('ma', 'Musiqi alətləri'), ('iva', 'İdman və asudə'), ('tlf', 'Telefonlar'), ('pve', 'Planşet və elektron kitablar'), ('oav', 'Ofis avadanlığı və istehlak'), ('op', 'Oyunlar Pultlar ve programlar'), ('ehv', 'Ehtiyat hissələri və aksesuarlar'), ('afv', 'Avtobuslar və xüsusi texnika'), ('avt', 'Avtomobillər'), ('aqr', 'Aqrotexnika'), ('mvm', 'Motoskiletler Ve Mopedler'), ('sn', 'Su nəqliyyatı'), ('itl', 'İtlər'), ('huv', 'Hevanlar ücün Məhsullar'), ('dh', 'Digər heyvanlar'), ('psk', 'Pişiklər'), ('qsl', 'Quşlar'), ('avb', 'Akvarium və balıqlar'), ('dgr', 'Digər')], max_length=50, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='elan',
            name='status',
            field=models.CharField(choices=[('mnz', 'Mənzillər'), ('tv', 'TV'), ('ovo', 'Obyektlər və ofislər'), ('trp', 'Torpaq'), ('qrj', 'Qarajlar'), ('vvb', 'Villalar, bağ evləri'), ('mvi', 'Mebel və interyer'), ('tvt', 'Temir Ve Tikinti'), ('btk', 'Bitkiler'), ('mt', 'Məişət texnikası'), ('qab', 'Qab-qacaq və mətbəx ləvazimatları'), ('ka', 'Komputer Aksesuarlari'), ('nvn', 'Noutbuklar və Netbuklar'), ('pc', 'Masaüstü kompüterlər'), ('nvs', 'Nömrələr və SİM-kartlar'), ('mnt', 'Komponentlər və monitorlar'), ('ft', 'Foto texnika'), ('vls', 'Velosipedlər'), ('ma', 'Musiqi alətləri'), ('iva', 'İdman və asudə'), ('tlf', 'Telefonlar'), ('pve', 'Planşet və elektron kitablar'), ('oav', 'Ofis avadanlığı və istehlak'), ('op', 'Oyunlar Pultlar ve programlar'), ('ehv', 'Ehtiyat hissələri və aksesuarlar'), ('afv', 'Avtobuslar və xüsusi texnika'), ('avt', 'Avtomobillər'), ('aqr', 'Aqrotexnika'), ('mvm', 'Motoskiletler Ve Mopedler'), ('sn', 'Su nəqliyyatı'), ('itl', 'İtlər'), ('huv', 'Hevanlar ücün Məhsullar'), ('dh', 'Digər heyvanlar'), ('psk', 'Pişiklər'), ('qsl', 'Quşlar'), ('avb', 'Akvarium və balıqlar'), ('dgr', 'Digər')], default=None, max_length=3, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='elancategory',
            name='category',
            field=models.CharField(choices=[('mnz', 'Mənzillər'), ('tv', 'TV'), ('ovo', 'Obyektlər və ofislər'), ('trp', 'Torpaq'), ('qrj', 'Qarajlar'), ('vvb', 'Villalar, bağ evləri'), ('mvi', 'Mebel və interyer'), ('tvt', 'Temir Ve Tikinti'), ('btk', 'Bitkiler'), ('mt', 'Məişət texnikası'), ('qab', 'Qab-qacaq və mətbəx ləvazimatları'), ('ka', 'Komputer Aksesuarlari'), ('nvn', 'Noutbuklar və Netbuklar'), ('pc', 'Masaüstü kompüterlər'), ('nvs', 'Nömrələr və SİM-kartlar'), ('mnt', 'Komponentlər və monitorlar'), ('ft', 'Foto texnika'), ('vls', 'Velosipedlər'), ('ma', 'Musiqi alətləri'), ('iva', 'İdman və asudə'), ('tlf', 'Telefonlar'), ('pve', 'Planşet və elektron kitablar'), ('oav', 'Ofis avadanlığı və istehlak'), ('op', 'Oyunlar Pultlar ve programlar'), ('ehv', 'Ehtiyat hissələri və aksesuarlar'), ('afv', 'Avtobuslar və xüsusi texnika'), ('avt', 'Avtomobillər'), ('aqr', 'Aqrotexnika'), ('mvm', 'Motoskiletler Ve Mopedler'), ('sn', 'Su nəqliyyatı'), ('itl', 'İtlər'), ('huv', 'Hevanlar ücün Məhsullar'), ('dh', 'Digər heyvanlar'), ('psk', 'Pişiklər'), ('qsl', 'Quşlar'), ('avb', 'Akvarium və balıqlar'), ('dgr', 'Digər')], max_length=50, verbose_name='Category'),
        ),
    ]
