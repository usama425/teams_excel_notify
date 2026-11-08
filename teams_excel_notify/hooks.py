app_name = "teams_excel_notify"
app_title = "Teams Excel Notify"
app_publisher = "ERC IT"
app_description = "Posts a Microsoft Teams message when someone changes a department's Excel file"
app_email = "it@example.com"
app_license = "MIT"

# Check every watched file once a minute.
scheduler_events = {
	"cron": {
		"* * * * *": ["teams_excel_notify.tasks.poll_all"],
	},
}

# Don't write a Scheduled Job Log row every minute (errors still go to the Error Log).
after_sync = ["teams_excel_notify.install.quiet_scheduler_log"]
after_migrate = ["teams_excel_notify.install.quiet_scheduler_log"]
