
import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image_01.jpg','Virat Kohli'),
      ('image_02.jpg','Mahendra singh dhoni'),
      ('image_03.jpg','Shubhman Gill'),
      ('image_04.jpg','Rohit Sharma'),
      ('image_05.jpg','Narendra Modi'),
      ('image_06.jpg','A.P.J.Abdul Kalam'),
      ('image_07.jpg','Mohammad Shami'),
      ('image_08.jpg','KL Rahul'),
      ('image_09.jpg','Swami Vivekanand'),
      ('image_10.jpg','Ravindra Jadeja'),
      ('image_11.jpg','Shreyas Iyer'),
      ('image_12.jpg','Kuldeep Yadav'),
      ('image_13.jpg','Jasprit Bumrah'),
      ('image_14.jpg','Bhushan Pradhan'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('testansarbucket','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
