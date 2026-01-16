# AWS SES Email Project
This project uses the AWS SES SDK v3 to send emails.

## Verifying Email Identities in AWS SES Console
To verify an email identity in the AWS SES console, follow these steps:
1. Log in to the AWS Management Console.
2. Navigate to the Amazon SES dashboard.
3. In the navigation pane, choose **Identities**.
4. Choose **Create a new identity**.
5. Enter the email address you want to verify and choose **Create identity**.
6. Follow the instructions to verify the email address.

## Running the Project Locally
To run the project locally, follow these steps:
1. Clone the repository to your local machine.
2. Create a new file named `.env` and add your AWS access key ID and secret access key.
3. Install the dependencies by running `npm install`.
4. Run the project by executing `npm start`.
5. Call the `sendEmail` function with the recipient's email address, subject, and body to send an email.