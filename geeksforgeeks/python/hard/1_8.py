Create Bucket Policy in AWS S3 Bucket with Python



Bucket policy of s3 bucket means permission and action which can be applied on
the particular bucket. AWS S3 has an optional policy that can be used to
restrict or grant access to an S3 bucket resource. It is important to note
that bucket policies are defined in JSON format.

For creating a bucket policy in python we will follow the below steps:

  *  **Step 1:** The first step for creating a bucket policy is we need to import python SDK boto3. This will provide methods to us by that we can access the resources of the AWS. And for the policy string dumping, we need to also import JSON. ****

    
    
    import json
    import boto3

  *  **Step 2:** The Second step will be we need to create a policy string. Policy string is a key-value pair dictionary. In which the first key will be the Version. And the second key will be the statement in the statement first key will be the _sid_ which will store how to type the policy we want to add. And the second key will be the Effect which will store the access status and the third key will be the permission which will store who have permission to access and the fourth key will be an action which will what type of operation we can perform and the last parameter in this Resource on which we will apply this policy.

 ****

**Example:**

    
    
    bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AddPerm",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": ["s3:*"],
                    "Resource": ["arn:aws:s3:::gfgbucket/*"]
                }
            ]
        }

 **Step 3:** The third step will need to convert the bucket policy string in
JSON.

  

  

    
    
    json.dumps(bucket_policy)

 **Step 4:** The fourth step will be for putting bucket policy to the bucket
we need to call _put_bucket_policy()_ function .this function will take the
first parameter the bucket name and the second parameter will be the policy
string.

    
    
    put_bucket_policy(Bucket,policy)

 **Step 5:** The last step will be to go to **AWS-
>S3->Bucket->Permission->Bucket policy **and **verify**.

 ****

**Complete code:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import json

import boto3

BUCKET_NAME='gfgbucket'

def create_bucket_policy():

 bucket_policy = {

 "Version": "2012-10-17",

 "Statement": [

 {

 "Sid": "AddPerm",

 "Effect": "Allow",

 "Principal": "*",

 "Action": ["s3:*"],

 "Resource": ["arn:aws:s3:::gfgbucket/*"]

 }

 ]

 }

 

 policy_string = json.dumps(bucket_policy)

 

 s3_client().put_bucket_policy(

 Bucket=BUCKET_NAME,

 Policy=policy_string

 )  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210304154547/Screenshot20210304at33220PM.jpg)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

