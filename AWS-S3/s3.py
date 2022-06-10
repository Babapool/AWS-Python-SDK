import boto3

s3=boto3.client('s3')
S3=boto3.resource('s3')

def createBucket():
    bucketName=input("Enter the bucket name:")
    response=s3.create_bucket(Bucket=bucketName)
    print("Bucket has been created")

def addObject():
    bucketName=input("Enter the bucket name:")
    filePath=input("Enter the file path:")
    objectName=input("Enter the name you want to save the file as:")
    with open(filePath, 'rb') as data:
        s3.upload_fileobj(data,bucketName,objectName)

    print("file has been uploaded")

def deleteObject():
    bucketName=input("Enter the bucket name:")
    objectName=input("Enter the name of the object you want to delete:")
    response=s3.delete_object(Bucket=bucketName,Key=objectName)
    print("File has been deleted")

def deleteBucket():
    bucketName=input("Enter the bucket Name:")
    response=s3.delete_bucket(Bucket=bucketName)

    print("Bucket has been deleted")

def listObjects():
    bucketName=input("Enter the bucket whose object you want to see:")
    bucket=S3.Bucket(bucketName)
    print('Listing Amazon S3 Bucket objects/files:')
    for obj in bucket.objects.all():
        print(f'-- {obj.key}')

def listBuckets():
    iterator=S3.buckets.all()
    print("Listing Amazon S3 Buckets:")
    for bucket in iterator:
        print(f"-- {bucket.name}")

def downloadObject():
    bucketName=input("Enter the bucket name:")
    objectName=input("Enter the name of the object:")
    fileName=input("Enter the name of the file you want to save:")
    object=S3.Object(bucketName,objectName)
    object.download_file(fileName)
    print('S3 object download complete')
    
while True:
    print ("\nAWS S3  Menu")
    print ("\n1. Create Bucket")
    print ("\n2. Upload Object")
    print ("\n3. Delete Object")
    print ("\n4. Delete Bucket")
    print ("\n5. listObjects")
    print ("\n6. listBuckets")
    print ("\n7. downloadObject")
    print ("\n8. Exit")
    choice = int(input("\nEnter the Choice: "))

    if choice==1:
        createBucket()

    elif choice==2:
        addObject()

    elif choice==3:
        deleteObject()

    elif choice==4:
        deleteBucket()

    elif choice==5:
        listObjects()

    elif choice==6:
        listBuckets()

    elif choice==7:
        downloadObject()

    elif choice==8:
        break

    else:
        print ("Provide a Valid Input")

