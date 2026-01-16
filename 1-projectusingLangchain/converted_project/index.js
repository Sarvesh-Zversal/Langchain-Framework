const { SendEmailCommand } = require('@aws-sdk/client-ses');
const sesClient = require('./sesClient');

async function sendEmail(toAddress, subject, body) {
  const params = {
    Source: 'verified-email@example.com',
    Destination: {
      ToAddresses: [toAddress],
    },
    Message: {
      Body: {
        Text: {
          Data: body,
        },
      },
      Subject: {
        Data: subject,
      },
    },
  };

  try {
    const data = await sesClient.send(new SendEmailCommand(params));
    console.log('Email sent successfully:', data);
  } catch (err) {
    console.error('Error sending email:', err);
  }
}

module.exports = sendEmail;