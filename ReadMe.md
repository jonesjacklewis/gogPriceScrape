# Gog Price Alert

## Stages

1. Install Required Modules (below)
2. Update `main.ini` with the relevant values
3. Get a google app password (if using gmail)
   1. [https://support.google.com/accounts/answer/185833](https://support.google.com/accounts/answer/185833)

## Modules

| Name     | Usage                           |
| -------- | ------------------------------- |
| requests | Make HTTP Request to target url |
| bs4      | Select class element for price  |
| configparser | Parse config file |
| smtplib | Sending Emails |
| email | Create Email |

## Details Needed

- These should be filled out in `main.ini`

### gog

| Field       | Description                              |
| ----------- | ---------------------------------------- |
| `url`       | Url to game you want alerts for          |
| `max_price` | The maximum price you are willing to pay |

### email

| Field      | Description                          |
| ---------- | ------------------------------------ |
| `password` | Password/App Password for the sender |
| `from`     | The sender email address             |
| `host`     | The smtp address of the email host   |
| `to`       | The recipient email address          |