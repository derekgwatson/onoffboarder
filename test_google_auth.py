from services.google_workspace import get_group_members


def test_google_group():
    group_email = 'all-staff@watsonblinds.com.au'
    try:
        members = get_group_members(group_email)
        print(f"✅ Success! Found {len(members)} members in '{group_email}'")
        for m in members:
            print(f"{m}")
    except Exception as e:
        print("❌ Failed to fetch group members:")
        print(e)


if __name__ == "__main__":
    test_google_group()
