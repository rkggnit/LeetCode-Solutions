# LeetCode-Solutions
## 🔄 Maintenance: How to Renew Session Cookies

Session cookies for HackerRank and LeetCode expire periodically. If a scheduled GitHub Action fails with an authorization error, follow these quick steps to update the secrets:

### 1. HackerRank Setup
* **Get the Cookie:** Log into [HackerRank](https://www.hackerrank.com). Open Developer Tools (`F12`), go to the **Network** tab, refresh the page, and click the first request (e.g., `dashboard`). Look under **Request Headers**, find `cookie:`, and copy the entire raw string.
* **Update GitHub:** Go to **Settings** > **Secrets and variables** > **Actions**. Edit the `HRANK_SESSION` secret and paste the new value.

### 2. LeetCode Setup
* **Get the Cookies:** Log into [LeetCode](https://leetcode.com). Open Developer Tools (`F12`), go to the **Application** (or **Storage**) tab, and expand **Cookies** on the left menu.
* **Update GitHub:** * Copy the value of the `LEETCODE_SESSION` cookie and save it to your GitHub secret named **`LEETCODE_SESSION`**.
  * Copy the value of the `csrftoken` cookie and save it to your GitHub secret named **`LEETCODE_CSRF_TOKEN`**.

### 3. Verify the Sync
Go to the **Actions** tab in this repository, select either the **HackerRank Sync** or **LeetCode Sync** workflow, and click **Run workflow** to test the connection manually.
