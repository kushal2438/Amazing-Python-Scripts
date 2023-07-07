import requests

def doh_dns_lookup(domain, record_type):
    url = f"https://cloudflare-dns.com/dns-query?name={domain}&type={record_type}"
    headers = {
        "Accept": "application/dns-json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


