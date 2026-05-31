import os
import requests
import time
import re

LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
CSRF_TOKEN = os.environ.get("LEETCODE_CSRF_TOKEN")

HEADERS = {
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRF_TOKEN};",
    "x-csrftoken": CSRF_TOKEN,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://leetcode.com"
}

GRAPHQL_URL = "https://leetcode.com/graphql/"

EXTENSION_MAP = {
    'python': 'py', 'python3': 'py', 'c': 'c', 'cpp': 'cpp', 'java': 'java',
    'javascript': 'js', 'typescript': 'ts', 'csharp': 'cs', 'php': 'php',
    'ruby': 'rb', 'swift': 'swift', 'golang': 'go', 'rust': 'rs',
    'scala': 'scala', 'kotlin': 'kt', 'mysql': 'sql', 'mssql': 'sql', 'oraclesql': 'sql'
}

def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def clean_html(html_content):
    if not html_content:
        return "Description not found."
    html_content = re.sub(r'<style[^>]*>[\s\S]*?</style>', '', html_content)
    html_content = re.sub(r'<script[^>]*>[\s\S]*?</script>', '', html_content)
    html_content = re.sub(r'\n\s*\n', '\n\n', html_content)
    return html_content.strip()

def fetch_submissions(offset, limit):
    query = """
    query submissionList($offset: Int!, $limit: Int!) {
      submissionList(offset: $offset, limit: $limit) {
        hasNext
        submissions {
          id
          title
          titleSlug
          statusDisplay
          lang
        }
      }
    }
    """
    resp = requests.post(GRAPHQL_URL, headers=HEADERS, json={"query": query, "variables": {"offset": offset, "limit": limit}})
    if resp.status_code == 200:
        return resp.json()
    return None

def fetch_submission_code(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
      }
    }
    """
    resp = requests.post(GRAPHQL_URL, headers=HEADERS, json={"query": query, "variables": {"submissionId": submission_id}})
    if resp.status_code == 200:
        data = resp.json().get('data', {}).get('submissionDetails')
        if data:
            return data.get('code')
    return ''

def fetch_question_data(title_slug):
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        content
      }
    }
    """
    resp = requests.post(GRAPHQL_URL, headers=HEADERS, json={"query": query, "variables": {"titleSlug": title_slug}})
    if resp.status_code == 200:
        data = resp.json().get('data', {}).get('question')
        if data:
            return data.get('content')
    return None

def sync_leetcode():
    os.makedirs("LeetCode", exist_ok=True)
    offset = 0
    limit = 20
    
    print("Connecting to LeetCode...")
    while True:
        print(f"Fetching batch from offset {offset}...")
        data = fetch_submissions(offset, limit)
        
        if not data or 'data' not in data:
            print("Authorization failed. Your LEETCODE_SESSION or LEETCODE_CSRF_TOKEN might be invalid.")
            break
            
        submission_data = data['data'].get('submissionList', {})
        submissions = submission_data.get('submissions', [])
        
        if not submissions:
            print("No more submissions found.")
            break
            
        for sub in submissions:
            if sub['statusDisplay'] == 'Accepted':
                raw_title = sub['title']
                clean_title = clean_filename(raw_title)
                slug = sub['titleSlug']
                lang = sub['lang']
                ext = EXTENSION_MAP.get(lang, lang)
                
                folder_path = os.path.join("LeetCode", clean_title)
                os.makedirs(folder_path, exist_ok=True)
                
                code_file_path = os.path.join(folder_path, f"{clean_title}.{ext}")
                readme_path = os.path.join(folder_path, "README.md")
                
                # Skip if already downloaded
                if os.path.exists(code_file_path):
                    continue
                    
                print(f"   -> Downloading Code and Question for: {clean_title}")
                
                # Fetch Code
                code = fetch_submission_code(sub['id'])
                if code:
                    with open(code_file_path, "w", encoding="utf-8") as f:
                        f.write(code)
                        
                # Fetch Question Details
                html_content = fetch_question_data(slug)
                cleaned_body = clean_html(html_content)
                readme_content = f"# {raw_title}\n\n{cleaned_body}"
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(readme_content)
                        
                time.sleep(1)
                
        if not submission_data.get('hasNext'):
            print("Reached the end of submissions.")
            break
            
        offset += limit

if __name__ == "__main__":
    sync_leetcode()
