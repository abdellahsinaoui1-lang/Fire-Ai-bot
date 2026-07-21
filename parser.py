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

=========================
الأوامر
=========================

CreateChannel
DeleteChannel

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
Category
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

=========================
Grant Role
=========================

اعط أحمد رتبة Staff

{
    "GrantRole0":{
        "Member":"Ahmed",
        "Role":"Staff"
    }
}

شيل رتبة Staff من أحمد

{
    "RemoveRole0":{
        "Member":"Ahmed",
        "Role":"Staff"
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
Ban
=========================

احظر أحمد

{
    "BanMember0":{
        "Member":"Ahmed",
        "Reason":"No reason"
    }
}

احظر أحمد لأنه يسب

{
    "BanMember0":{
        "Member":"Ahmed",
        "Reason":"يسب"
    }
}

=========================
Kick
=========================

اطرد أحمد

{
    "KickMember0":{
        "Member":"Ahmed",
        "Reason":"No reason"
    }
}

=========================
Timeout
=========================

اكتم أحمد 15 دقيقة

{
    "TimeoutMember0":{
        "Member":"Ahmed",
        "Minutes":15
    }
}

اكتم أحمد ساعة

{
    "TimeoutMember0":{
        "Member":"Ahmed",
        "Minutes":60
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
