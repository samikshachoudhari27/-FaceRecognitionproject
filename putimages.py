
import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image_01.jpg','Virat Kohli'),
      ('image_02.jpg','Mahendra singh dhoni'),
      ('image_03.jpg','Shubhman Gill'),
      ('image_04.jpeg','Rohit Sharma'),
      ('image_05.jpeg','Narendra Modi'),
      ('image_06.jpeg','A.P.J.Abdul Kalam'),
      ('image_07.jpeg','Mohammad Shami'),
      ('image_08.jpeg','KL Rahul'),
      ('image_09.jpeg','Swami Vivekanand'),
      ('image_10.jpeg','Ravindra Jadeja'),
      ('image_11.jpeg','Shreyas Iyer'),
      ('image_12.jpeg','Kuldeep Yadav'),
      ('image_13.jpeg','Jasprit Bumrah'),
      ('image_14.jpeg','Bhushan Pradhan'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('testansarbucket','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
