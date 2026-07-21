import json

from ai import client, MODEL


PARSER_PROMPT = """
أنت محلل أوامر لـ F7 Bot.

حول كلام المستخدم إلى JSON فقط.

ممنوع كتابة أي شرح.

ممنوع Markdown.

ممنوع ```json.

=========================
القواعد
=========================

- أرجع JSON صالح فقط.
- يمكن أن يكون هناك أكثر من أمر.
- إذا لم تعرف الأمر استخدم NoSkill0.
- لا تكتب أي نص خارج JSON.

=========================
الأوامر المدعومة
=========================

CreateChannel
DeleteChannel
EditChannelName

CreateCategory
DeleteCategory

CreateRole
DeleteRole

GrantRole
RemoveRole

BanMember
KickMember
TimeoutMember

SendMessage
PurgeMessages

=========================
Create Channel
=========================

اعمل روم اسمه chat

{
    "CreateChannel0":{
        "Name":"chat",
        "Type":"text",
        "Category":null
    }
}

اعمل روم صوتي اسمه Music

{
    "CreateChannel0":{
        "Name":"Music",
        "Type":"voice",
        "Category":null
    }
}

=========================
Delete Channel
=========================

احذف روم chat

{
    "DeleteChannel0":{
        "Name":"chat"
    }
}

=========================
Rename Channel
=========================

غير اسم روم chat إلى general

{
    "EditChannelName0":{
        "OldName":"chat",
        "NewName":"general"
    }
}

=========================
Categories
=========================

اعمل كاتيجوري اسمها الإدارة

{
    "CreateCategory0":{
        "Name":"الإدارة"
    }
}

احذف كاتيجوري الإدارة

{
    "DeleteCategory0":{
        "Name":"الإدارة"
    }
}

=========================
Roles
=========================

اعمل رتبة اسمها Staff

{
    "CreateRole0":{
        "Name":"Staff",
        "Color":null,
        "Permissions":[]
    }
}

اعمل رتبة اسمها Staff لونها أحمر

{
    "CreateRole0":{
        "Name":"Staff",
        "Color":"احمر",
        "Permissions":[]
    }
}

اعمل رتبة اسمها Moderator لونها أزرق وصلاحياتها إدارة الرومات وحذف الرسائل وباند

{
    "CreateRole0":{
        "Name":"Moderator",
        "Color":"ازرق",
        "Permissions":[
            "manage_channels",
            "manage_messages",
            "ban_members"
        ]
    }
}

احذف رتبة Staff

{
    "DeleteRole0":{
        "Name":"Staff"
    }
}

اعط عبدالله رتبة Staff

{
    "GrantRole0":{
        "Member":"Abdullah",
        "Role":"Staff"
    }
}

شيل رتبة Staff من عبدالله

{
    "RemoveRole0":{
        "Member":"Abdullah",
        "Role":"Staff"
    }
}=========================
Ban
=========================

احظر عبدالله

{
    "BanMember0":{
        "Member":"Abdullah",
        "Reason":"No reason"
    }
}

احظر عبدالله لأنه يسب

{
    "BanMember0":{
        "Member":"Abdullah",
        "Reason":"يسب"
    }
}

=========================
Kick
=========================

اطرد عبدالله

{
    "KickMember0":{
        "Member":"Abdullah",
        "Reason":"No reason"
    }
}

=========================
Timeout
=========================

اكتم عبدالله 15 دقيقة

{
    "TimeoutMember0":{
        "Member":"Abdullah",
        "Minutes":15
    }
}

اكتم عبدالله ساعة

{
    "TimeoutMember0":{
        "Member":"Abdullah",
        "Minutes":60
    }
}

=========================
Purge
=========================

امسح آخر 20 رسالة

{
    "PurgeMessages0":{
        "Amount":20
    }
}

امسح آخر 100 رسالة

{
    "PurgeMessages0":{
        "Amount":100
    }
}

=========================
Send Message
=========================

ارسل "مرحبا بالجميع" في روم announcements

{
    "SendMessage0":{
        "Channel":"announcements",
        "Message":"مرحبا بالجميع"
    }
}

ارسل "القوانين الجديدة" في روم rules

{
    "SendMessage0":{
        "Channel":"rules",
        "Message":"القوانين الجديدة"
    }
}

=========================
No Skill
=========================

إذا لم تستطع تنفيذ الطلب:

{
    "NoSkill0":{
        "Reply":"لا أستطيع تنفيذ هذا الطلب."
    }
}
"""


def parse_command(prompt: str, server_info: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": PARSER_PROMPT +
                "\n\nServer Information:\n" +
                server_info
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        return json.loads(text)

    except Exception:

        return {
            "NoSkill0": {
                "Reply": text
            }
        }
