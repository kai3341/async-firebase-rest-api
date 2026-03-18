from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from typing import NotRequired, Literal, Annotated


class ActionCodeSettings(TypedDict):
    continueUrl: str  # url
    canHandleCodeInApp: "NotRequired[bool]"  # handle_code_in_app
    dynamicLinkDomain: "NotRequired[str]"  # dynamic_link_domain
    linkDomain: "NotRequired[str]"  # link_domain
    iOSBundleId: "NotRequired[str]"  # ios_bundle_id
    androidPackageName: "NotRequired[str]"  # android_package_name
    androidMinimumVersion: "NotRequired[str]"  # android_minimum_version
    androidInstallApp: "NotRequired[bool]"  # android_install_app


class ProviderUserInfo(TypedDict):
    rawId: str
    displayName: "NotRequired[str]"
    email: "NotRequired[str]"
    phoneNumber: "NotRequired[str]"
    photoUrl: "NotRequired[str]"
    providerId: "NotRequired[str]"
    # === Not listed by firebase_admin:
    federatedId: "NotRequired[str]"


class UserRecord(TypedDict):
    localId: str
    displayName: "NotRequired[str]"
    email: "NotRequired[str]"
    phoneNumber: "NotRequired[str]"
    photoUrl: "NotRequired[str]"
    emailVerified: "NotRequired[bool]"
    disabled: "NotRequired[Literal[True]]"
    validSince: "NotRequired[Annotated[str, 'int | datetime.date.fromtimestamp']]"
    # <=== user_metadata
    lastRefreshAt: "NotRequired[Annotated[str, 'datetime.datetime.fromisoformat']]"
    createdAt: "NotRequired[Annotated[str, 'int | div(1000) | datetime.datetime.fromtimestamp']]"
    lastLoginAt: "NotRequired[Annotated[str, 'int | div(1000) | datetime.datetime.fromtimestamp']]"
    # user_metadata ===>
    providerUserInfo: "NotRequired[list[ProviderUserInfo]]"
    customAttributes: "NotRequired[Annotated[str, 'json']]"
    tenantId: "NotRequired[str]"
    # === Not listed by firebase_admin:
    passwordUpdatedAt: "NotRequired[Annotated[str, 'int | div(1000) | datetime.datetime.fromtimestamp']]"
    passwordHash: "NotRequired[Annotated[str, 'base64']]"


class ExportedUserRecord(UserRecord):
    # passwordHash provided by UserRecord
    salt: "NotRequired[Annotated[str, 'base64']]"
