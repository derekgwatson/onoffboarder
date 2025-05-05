from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import GOOGLE_CREDENTIALS_FILE, GOOGLE_ADMIN_USER


SCOPES = ['https://www.googleapis.com/auth/admin.directory.group.member']


def get_google_service():
    """Create and return an authenticated Google Admin SDK service."""
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_CREDENTIALS_FILE, scopes=SCOPES
    ).with_subject(GOOGLE_ADMIN_USER)

    return build('admin', 'directory_v1', credentials=credentials)


def get_group_members(group_email):
    """Return a list of current member emails in the specified group."""
    service = get_google_service()
    result = service.members().list(groupKey=group_email).execute()
    members = result.get('members', [])
    return [m['email'] for m in members]


def remove_from_group(group_email, member_email):
    """Remove a member from the group."""
    service = get_google_service()
    service.members().delete(groupKey=group_email, memberKey=member_email).execute()
