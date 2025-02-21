from drf_yasg import openapi

error_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "status": openapi.Schema(
            type=openapi.TYPE_STRING, description="Response error status"
        ),
        "message": openapi.Schema(
            type=openapi.TYPE_STRING, description="Response error message"
        ),
    },
)

successful_response_without_data = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "status": openapi.Schema(
            type=openapi.TYPE_STRING, description="Response error status"
        ),
        "message": openapi.Schema(
            type=openapi.TYPE_STRING, description="Response error message"
        ),
        "data": openapi.Schema(type=openapi.TYPE_OBJECT, nullable=True),
    },
)


coach_profile_properties = (
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description="Coach profile information",
        properties={
            "email": openapi.Schema(
                type=openapi.TYPE_STRING, description="User email", nullable=True
            ),
            "user__uuid": openapi.Schema(
                type=openapi.TYPE_STRING, description="User UUID", nullable=True
            ),
            "full_name": openapi.Schema(
                type=openapi.TYPE_STRING, description="Full name", nullable=True
            ),
            "date_of_birth": openapi.Schema(
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
                description="Date of birth",
                nullable=True,
            ),
            "education": openapi.Schema(
                type=openapi.TYPE_STRING, description="Education", nullable=True
            ),
            "specialization": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Specialization",
                nullable=True,
            ),
            "license": openapi.Schema(
                type=openapi.TYPE_STRING, description="License", nullable=True
            ),
            "experience": openapi.Schema(
                type=openapi.TYPE_STRING, description="Experience", nullable=True
            ),
            "slogan": openapi.Schema(
                type=openapi.TYPE_STRING, description="Slogan", nullable=True
            ),
            "avatar": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Profile image URL",
                nullable=True,
            ),
            "mobile": openapi.Schema(
                type=openapi.TYPE_STRING, description="Phone number", nullable=True
            ),
            "additional_mobile": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Additional phone number",
                nullable=True,
            ),
            "facebook_account": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Facebook account",
                nullable=True,
            ),
            "instagram_account": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Instagram account",
                nullable=True,
            ),
            "additional_account": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Additional account",
                nullable=True,
            ),
        },
    ),
)


player_profile_properties = (
    openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "email": openapi.Schema(
                type=openapi.TYPE_STRING, description="User email", nullable=True
            ),
            "user__uuid": openapi.Schema(
                type=openapi.TYPE_STRING, description="User UUID", nullable=True
            ),
            "full_name": openapi.Schema(
                type=openapi.TYPE_STRING, description="Full name", nullable=True
            ),
            "date_of_birth": openapi.Schema(
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_DATE,
                description="Date of birth",
                nullable=True,
            ),
            "weight": openapi.Schema(
                type=openapi.TYPE_STRING, description="Weight", nullable=True
            ),
            "height": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Height",
                nullable=True,
            ),
            "avatar": openapi.Schema(
                type=openapi.TYPE_STRING, description="Avatar", nullable=True
            ),
            "mobile": openapi.Schema(
                type=openapi.TYPE_STRING, description="Phone number", nullable=True
            ),
            "additional_mobile": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Additional phone number",
                nullable=True,
            ),
            "facebook_account": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Facebook account",
                nullable=True,
            ),
            "instagram_account": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Instagram account",
                nullable=True,
            ),
            "additional_account": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Additional account",
                nullable=True,
            ),
        },
    ),
)
