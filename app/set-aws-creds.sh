#!/bin/bash
#If there are existing environment variables set, this can cause issues so we unset them first
unset AWS_SESSION_TOKEN
unset AWS_SECRET_ACCESS_KEY
unset AWS_ACCESS_KEY_ID

# Variables
profile=${profile:-default}

while [ $# -gt 0 ]; do
   if [[ $1 == *"--"* ]]; then
        param="${1/--/}"
        declare $param="$2"
        # echo $1 $2 // Optional to see the parameter:value result
   fi
  shift
done

if [[ "$profile" == "corps-cloud" ]];
then
     TOKEN_SERIAL_NUMBER="arn:aws:iam::839135435328:mfa/will.b"
else
     TOKEN_SERIAL_NUMBER="arn:aws:iam::038611608639:mfa/Wil.Breitkreutz"
fi

#Get the code from the MFA device
echo "Please enter MFA code"
read code

# Get Session Token
creds=`aws sts get-session-token --profile $profile --serial-number $TOKEN_SERIAL_NUMBER --token-code $code`

#Parse the response into separate variables
access_key=`echo $creds | jq .Credentials.AccessKeyId`
secret_key=`echo $creds | jq .Credentials.SecretAccessKey`
session_token=`echo $creds | jq .Credentials.SessionToken`

#Display the keys to the user for reference/confirm proper working
# echo $access_key
# echo $secret_key
# echo $session_token

#Set the appropriate environment variables -- The sed statement is needed to strip the quotation marks
export AWS_ACCESS_KEY_ID=`echo $access_key | sed -e 's/^"//' -e 's/"$//'`
export AWS_SECRET_ACCESS_KEY=`echo $secret_key | sed -e 's/^"//' -e 's/"$//'`
export AWS_SESSION_TOKEN=`echo $session_token | sed -e 's/^"//' -e 's/"$//'`

echo $AWS_ACCESS_KEY_ID