from marshmallow import Schema, fields


class URLSchema(Schema):
    url = fields.Url(
        required=True,
        error_messages={
            "required": "URL is required.",
            "invalid": "Please provide a valid URL."
        }
    )