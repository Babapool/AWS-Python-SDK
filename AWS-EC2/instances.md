# How to setup AWS Python SDK 

## **In Linux**

1. I would suggest you that one should install AWS CLI for Linux x86 (64-bit) :
  + Installation
    - ``` curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" ```
    - ``` unzip awscliv2.zip ```
    - ``` sudo ./aws/install ```
    -  Confirm the version installed by running: ```aws --version```
  + To install for Linux ARM visit the [Linux ARM Installation Section.](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

  + To configure the AWS CLI visit [Quick configuration with aws configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

2. Install python in your system
3. Then install `boto3` with the help og the following commands:
      ```pip install boto3``` or ```pip3 install boto3```
      

## **In Windows**

1. I would suggest you that one should install AWS CLI for Windows:
  + Installation
    - Download [AWS CLI MSI installer for Windows (64-bit)](https://awscli.amazonaws.com/AWSCLIV2.msi)  
                                          **OR** 
     - Run the following command: ```msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi```
     - Confirm the version installed by running: ```aws --version```
     
   ***Remeber you should have a 64-bit of Windows XP or later running on your system***

  + To configure the AWS CLI visit [Quick configuration with aws configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

2. Install python in your system
3. Then install `boto3` with the help og the following commands:
      ```pip install boto3``` or ```pip3 install boto3```





To view how the code was written you can visit [boto3 example documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-examples.html)
