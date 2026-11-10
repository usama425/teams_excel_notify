## Teams Excel Notify

A Frappe v16 app that watches department Excel files in Microsoft 365 and posts a
message to each department's Teams channel when someone changes them: who edited,
when, and exactly which cells changed (old → new), rows added, removed or moved.

It only reads data from Microsoft 365 (application permission `Files.Read.All`) and
does not touch ERPNext data. It runs on any Frappe v16 site, including Frappe Cloud.

### How it works

- Every minute the scheduler asks Microsoft Graph for each watched file's content tag.
- When the tag changes, the app downloads the workbook, compares it with the previous
  version and remembers who saved it.
- When nobody has edited for the quiet period (default 5 minutes), it posts one
  Adaptive Card to the channel through a Teams Workflows webhook and keeps a
  Teams Excel Change Log entry.

### Setup (short version)

1. Register an app in Microsoft Entra ID, add the Microsoft Graph **application**
   permission `Files.Read.All`, grant admin consent, and create a client secret.
2. In each department channel add the Workflows template
   "Send webhook alerts to a channel" and copy its URL.
3. Install this app on the site, then open **Teams Notify Settings**, enter the
   tenant ID, client ID and secret, and click **Test connection**.
4. Create a **Teams Excel Watch** per file: paste the file's link and the workflow URL, save.

The full step-by-step guide is in the setup document that came with this app.

### Tests

```
bench --site <site> set-config allow_tests true
bench --site <site> run-tests --app teams_excel_notify
```

The comparison engine has no Frappe dependency and can also be tested with
`python -m pytest teams_excel_notify/tests/test_differ.py`.

#### License

MIT
