# Generated by Django 3.1.7 on 2021-03-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_sources_saml", "0008_auto_20201112_2016"),
    ]

    operations = [
        migrations.AlterField(
            model_name="samlsource",
            name="name_id_policy",
            field=models.TextField(
                choices=[
                    ("urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress", "Email"),
                    (
                        "urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
                        "Persistent",
                    ),
                    (
                        "urn:oasis:names:tc:SAML:2.0:nameid-format:X509SubjectName",
                        "X509",
                    ),
                    (
                        "urn:oasis:names:tc:SAML:2.0:nameid-format:WindowsDomainQualifiedName",
                        "Windows",
                    ),
                    (
                        "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
                        "Transient",
                    ),
                ],
                default="urn:oasis:names:tc:SAML:2.0:nameid-format:persistent",
                help_text="NameID Policy sent to the IdP. Can be unset, in which case no Policy is sent.",
            ),
        ),
    ]
