import requests
from config import EH_API_KEY, EH_BASE_URL


def _get_active_employees():
    """Fetch active employee email addresses from Employment Hero."""
    url = f"{EH_BASE_URL}/employees"
    headers = {
        "Authorization": f"Bearer {EH_API_KEY}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Adjust these keys to match your actual API response structure
    return [
        emp['email']
        for emp in data.get('data', [])
        if emp.get('status') == 'active' and emp.get('email')
    ]


def get_active_employees():
    """Mocked: Return a list of known active staff emails."""
    return [
        "1983.j.baird@gmail.com",
        "ampa83@hotmail.com",
        "angwindhill@yahoo.co.uk",
        "Blake.eather93@outlook.com",
        "cfo@watsonblinds.com.au",
        "clare.weinhonig@watsonblinds.com.au",
        "cuf.livio90@gmail.com",
        "fariahumaira@gmail.com",
        "ian.fletcher@watsonblinds.com.au",
        "katrina@designerdrapes.com.au",
        "kevin.watson@watsonblinds.com.au",
        "kim.davey61@outlook.com",
        "masoomaeftekhari79@gmail.com",
        "naughtyfatima784@gmail.com",
        "outbackreid@hotmail.com",
        "parthvig1598@gmail.com",
        "pemba002@gmail.com",
        "qasimmehmood67@gmail.com",
        "Rohan.watson@watsonblinds.com.au",
        "rouj.perez@watsonblinds.com.au",
        "smallen14@outlook.com",
        "t.khambai@gmail.com",
        "wickedwendy66@hotmail.com",
        "tabishkayani19@gmail.com",
        "new@gmail.com"
    ]
