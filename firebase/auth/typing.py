from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from typing import NotRequired


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
    providerId: str
    federatedId: str
    email: str
    rawId: str


class UserRecord(TypedDict):
    localId: str
    email: str
    passwordHash: str
    emailVerified: bool
    passwordUpdatedAt: int
    providerUserInfo: list[ProviderUserInfo]
